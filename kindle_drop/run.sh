#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DIR/.." && pwd)"

if [ ! -d "$ROOT_DIR/app_env" ]; then
    echo "Creating virtual environment and installing dependencies..."
    python3 -m venv "$ROOT_DIR/app_env"
    "$ROOT_DIR/app_env/bin/pip" install --quiet paramiko flask "qrcode[pil]" pillow
fi

echo "=========================================================="
echo "  📖 Starting Kindle Drop — Wireless Book Uploader"
echo "=========================================================="

# Open default browser after a brief delay in the background
(sleep 1.2 && open "http://localhost:5050") &

# Run app
exec "$ROOT_DIR/app_env/bin/python3" "$DIR/app.py"
