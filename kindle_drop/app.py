#!/usr/bin/env python3
import os
import sys
import json
import socket
import io
import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request, jsonify, send_file, Response
import paramiko
import qrcode

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max upload

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "kindle_ip": "",
        "port": 2222,
        "username": "root",
        "remote_books_dir": "/mnt/us/books"
    }

def save_config(cfg):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(cfg, f, indent=2)
    except Exception as e:
        print(f"Error saving config: {e}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def get_sftp_client(ip=None, port=None, username=None):
    cfg = load_config()
    ip = ip or cfg.get("kindle_ip")
    port = port or cfg.get("port", 2222)
    username = username or cfg.get("username", "root")

    if not ip:
        raise ValueError("Kindle IP address is not configured.")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # KOReader's Dropbear uses -n (allows empty password or any password)
    # Paramiko handles empty password connection cleanly
    try:
        ssh.connect(
            hostname=ip,
            port=int(port),
            username=username,
            password="",
            timeout=5.0,
            look_for_keys=False,
            allow_agent=False
        )
    except Exception:
        # Retry with username only or none
        ssh.connect(
            hostname=ip,
            port=int(port),
            username=username,
            timeout=5.0
        )
        
    sftp = ssh.open_sftp()
    return ssh, sftp

def format_size(bytes_val):
    if bytes_val < 1024:
        return f"{bytes_val} B"
    elif bytes_val < 1024 * 1024:
        return f"{bytes_val / 1024:.1f} KB"
    elif bytes_val < 1024 * 1024 * 1024:
        return f"{bytes_val / (1024 * 1024):.1f} MB"
    else:
        return f"{bytes_val / (1024 * 1024 * 1024):.1f} GB"

@app.route("/")
def index():
    cfg = load_config()
    local_ip = get_local_ip()
    port = 5050
    phone_url = f"http://{local_ip}:{port}"
    return render_template("index.html", config=cfg, phone_url=phone_url, local_ip=local_ip)

@app.route("/api/qr")
def qr_code():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:5050"
    qr = qrcode.QRCode(box_size=6, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/api/config", methods=["GET", "POST"])
def config_endpoint():
    if request.method == "POST":
        data = request.json or {}
        cfg = load_config()
        if "kindle_ip" in data:
            cfg["kindle_ip"] = data["kindle_ip"].strip()
        if "port" in data:
            cfg["port"] = int(data["port"])
        if "username" in data:
            cfg["username"] = data["username"].strip()
        save_config(cfg)
        return jsonify({"status": "ok", "config": cfg})
    return jsonify(load_config())

@app.route("/api/status")
def status_endpoint():
    ip = request.args.get("ip")
    cfg = load_config()
    target_ip = ip or cfg.get("kindle_ip")
    if not target_ip:
        return jsonify({"connected": False, "error": "No IP configured"})

    ssh = None
    try:
        ssh, sftp = get_sftp_client(ip=target_ip)
        
        # Check storage space using df
        stdin, stdout, stderr = ssh.exec_command("df -h /mnt/us")
        df_output = stdout.read().decode().strip().split("\n")
        storage_info = "Unknown"
        if len(df_output) > 1:
            parts = df_output[1].split()
            if len(parts) >= 5:
                storage_info = f"{parts[3]} free of {parts[1]} ({parts[4]} used)"

        # Count books in directory
        remote_dir = cfg.get("remote_books_dir", "/mnt/us/books")
        try:
            items = sftp.listdir(remote_dir)
            book_files = [f for f in items if not f.startswith(".") and not f.endswith(".sdr")]
            book_count = len(book_files)
        except Exception:
            book_count = 0

        # Save active IP if successful
        if ip and ip != cfg.get("kindle_ip"):
            cfg["kindle_ip"] = ip
            save_config(cfg)

        return jsonify({
            "connected": True,
            "ip": target_ip,
            "storage": storage_info,
            "books_count": book_count
        })
    except Exception as e:
        return jsonify({"connected": False, "ip": target_ip, "error": str(e)})
    finally:
        if ssh:
            ssh.close()

@app.route("/api/scan", methods=["POST"])
def scan_network():
    local_ip = get_local_ip()
    subnet_prefix = ".".join(local_ip.split(".")[:3])
    cfg = load_config()
    target_port = cfg.get("port", 2222)

    found_ips = []

    def probe(host):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        try:
            s.connect((host, target_port))
            s.close()
            return host
        except Exception:
            return None

    # Scan 1..254 concurrently
    with ThreadPoolExecutor(max_workers=60) as executor:
        hosts = [f"{subnet_prefix}.{i}" for i in range(1, 255)]
        results = executor.map(probe, hosts)
        for res in results:
            if res:
                found_ips.append(res)

    return jsonify({"found": found_ips})

@app.route("/api/books")
def list_books():
    ssh = None
    try:
        cfg = load_config()
        remote_dir = cfg.get("remote_books_dir", "/mnt/us/books")
        ssh, sftp = get_sftp_client()
        
        # Ensure remote_dir exists
        try:
            sftp.stat(remote_dir)
        except IOError:
            sftp.mkdir(remote_dir)

        files_list = []
        for attr in sftp.listdir_attr(remote_dir):
            if attr.filename.startswith(".") or attr.filename.endswith(".sdr"):
                continue
            ext = os.path.splitext(attr.filename)[1].lower().replace(".", "")
            files_list.append({
                "filename": attr.filename,
                "size_bytes": attr.st_size,
                "size_fmt": format_size(attr.st_size),
                "mtime": attr.st_mtime,
                "format": ext.upper() if ext else "BOOK"
            })
            
        files_list.sort(key=lambda x: x["mtime"], reverse=True)
        return jsonify({"status": "ok", "books": files_list})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if ssh:
            ssh.close()

@app.route("/api/upload", methods=["POST"])
def upload_books():
    if "files" not in request.files:
        return jsonify({"status": "error", "message": "No files provided"}), 400

    uploaded_files = request.files.getlist("files")
    if not uploaded_files or uploaded_files[0].filename == "":
        return jsonify({"status": "error", "message": "Empty file list"}), 400

    ssh = None
    transferred = []
    errors = []

    try:
        cfg = load_config()
        remote_dir = cfg.get("remote_books_dir", "/mnt/us/books")
        ssh, sftp = get_sftp_client()

        # Ensure directory exists
        try:
            sftp.stat(remote_dir)
        except IOError:
            sftp.mkdir(remote_dir)

        for file_obj in uploaded_files:
            filename = os.path.basename(file_obj.filename)
            if not filename or filename.startswith("."):
                continue
                
            remote_path = f"{remote_dir}/{filename}"
            try:
                # Direct stream upload to Kindle via SFTP
                with sftp.file(remote_path, "wb") as remote_file:
                    file_obj.seek(0)
                    while True:
                        chunk = file_obj.read(64 * 1024)
                        if not chunk:
                            break
                        remote_file.write(chunk)
                transferred.append(filename)
            except Exception as e:
                errors.append(f"{filename}: {str(e)}")

        return jsonify({
            "status": "ok" if transferred else "error",
            "transferred": transferred,
            "errors": errors
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if ssh:
            ssh.close()

@app.route("/api/delete", methods=["POST"])
def delete_book():
    data = request.json or {}
    filename = data.get("filename")
    if not filename:
        return jsonify({"status": "error", "message": "Filename required"}), 400

    ssh = None
    try:
        cfg = load_config()
        remote_dir = cfg.get("remote_books_dir", "/mnt/us/books")
        ssh, sftp = get_sftp_client()

        target_file = f"{remote_dir}/{filename}"
        sftp.remove(target_file)
        
        # Also clean .sdr directory if it exists
        sdr_folder = f"{remote_dir}/{filename}.sdr"
        try:
            for f in sftp.listdir(sdr_folder):
                sftp.remove(f"{sdr_folder}/{f}")
            sftp.rmdir(sdr_folder)
        except Exception:
            pass

        return jsonify({"status": "ok", "deleted": filename})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if ssh:
            ssh.close()

if __name__ == "__main__":
    port = 5050
    local_ip = get_local_ip()
    print("=" * 60)
    print("🚀 Kindle Drop — Wireless Book Uploader is Running!")
    print(f"💻 Mac URL:    http://localhost:{port}")
    print(f"📱 Phone URL:  http://{local_ip}:{port}")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, debug=False)
