# Kindle Basic 3 (KT4) Revival & Sustainability Guide
### *Giving Aging E-Readers a Second Life & Reducing E-Waste*

> A complete, field-tested guide to revitalizing the **Kindle Basic 3 (2019, 10th generation, codename `KT4`, serial prefix `G09 10L`)** running firmware **`5.18.1.1.1`** by liberating it from proprietary bloat, installing **KUAL**, and deploying **KOReader** in a lightweight, energy-efficient **No-Framework** mode with wireless macOS Finder transfers.

> [!TIP]
> **🤖 Pair-Programming with a Local CLI AI Agent:**
> Because this revival process involves multi-stage payload staging, checksum validation, volume management, and precise timing, it is **highly recommended to use a CLI-based autonomous AI agent** (such as Google Antigravity, Claude Code, Aider, or similar tools with direct terminal or PowerShell access).
> 
> **How to use:** Simply pass this GitHub repository URL (`https://github.com/ars-codelab/kindle-sustainability-project`) to your CLI agent as context. The agent can read this guide directly and handle or guide you through most steps end-to-end:
> * **Safely Automate Backups:** Detect volume mounts and perform bit-for-bit local backups automatically (`rsync`).
> * **Download & Verify Packages:** Fetch the exact firmware-matched exploit files, verify MD5 checksums, and stage directories without manual errors.
> * **Clean OS Metadata & Manage Drives:** Automatically strip hidden OS artifacts (e.g., macOS `dot_clean`, AppleDouble files) and safely unmount/eject storage.
> * **Step-by-Step Guidance:** Dynamically troubleshoot in real time (e.g., recognizing Store timing, handling application popups, configuring wireless SFTP).

---

## ✨ What You Get: The Payoff (Why It’s Worth the Effort)

Before embarking on this multi-step process, here is exactly what your Kindle Basic 3 (KT4) will look like once finished:

* ⚡ **Blazing Fast Performance:** RAM consumption drops from **~85% down to under 25%** by suspending Amazon’s heavy Java operating stack (`lab126_gui`). Menus, library navigation, and page turns become instantaneous.
* 📖 **Universal Format Freedom:** Full native support for **EPUB, PDF, CBZ, CBR, FB2, MOBI, and TXT**. No more converting files through Calibre or Amazon Send-to-Kindle services.
* 📶 **Zero-Cable Wireless Sync:** Mount your Kindle directly inside **macOS Finder** as a network drive over your home Wi-Fi (`Cmd + K` via SFTP). Drag and drop books without ever needing a physical USB cable again.
* 🔋 **Extended Battery Life & Zero Distractions:** Strips out background ad tracking, store analytics, and battery-draining indexing loops. Leaves you with a 100% distraction-free reading machine.
* 🛠️ **Modern E-Reader Feature Suite:** Highly granular typography controls, automated margin cropping for PDFs, dual-page mode, dictionary lookups, reading statistics, and cross-device reading progress sync (KOReader Sync).
* ♻️ **10+ More Years of Usable Life:** Eliminates e-waste by turning a 2013 device into a modern, responsive daily driver that outperforms many budget 2026 e-readers.

---

## 🌍 Why This Project Exists: Fighting Planned Obsolescence & E-Waste

Consumer electronics are frequently abandoned not because the hardware has failed, but because modern proprietary software outgrows older hardware constraints.

* **The Hardware Still Shines:** The Kindle Basic 3 (2019) features a 6" 167 PPI e-ink display, built-in front-lighting, Wi-Fi, and a battery that can easily last for weeks.
* **The Software Bottleneck:** Out of the box, Amazon's proprietary Java application stack (`lab126_gui`), background telemetry, indexing services, and store integrations consume **75% to 85% of the device's modest 512 MB of RAM** at idle. This causes sluggish UI response, battery drain, and limits you to Amazon-approved document formats.
* **The Sustainable Solution:** Rather than discarding functional e-readers into landfills, we can remove unwanted background packages, bypass legacy software constraints, and install **KOReader**—a blazing-fast, open-source document viewer. 
* **The Result:** Memory usage drops from **~85% down to under 25%**, page turns become instantaneous, battery life improves, and the device gains native support for open standards (EPUB, CBZ, PDF) and wireless LAN transfers.

---

## ⚠️ DISCLAIMER — PROCEED AT YOUR OWN RISK ⚠️

> **READ THIS CAREFULLY BEFORE CONTINUING:**
> 
> * **Hardware Modification Risks:** While this process is tested and verified, modifying your Kindle's root filesystem and boot scripts carries an inherent risk of soft-bricking or bootlooping the device.
> * **No Liability:** Neither the authors of this guide nor the open-source developers of SpringBreak, KUAL, MRPI, or KOReader assume any responsibility for damaged hardware, lost data, or bricked devices.
> * **Model Compatibility:** This guide is specifically written and tested for the **Kindle Basic 3 (2019, codename KT4, serial prefix `G09 10L`)** on firmware **`5.18.1.1.1`**. The exploit used (**SpringBreak**) officially supports **KT4/PW4 on 5.18.1.1.1**. Do **NOT** follow these exact steps on other models/firmware without checking the [KindleModding jailbreak wizard](https://kindlemodding.org/jailbreaking/).
> * **Mandatory Backup:** Always create a complete, bit-for-bit local backup of your device's flash storage before making any filesystem modifications.

---

## Device & Target Specifications

| Parameter | Specification |
| :--- | :--- |
| **Target Hardware** | Kindle Basic 3 (2019, 10th Generation, codename `KT4`, serial prefix `G09 10L`) |
| **Processor** | Freescale/NXP i.MX6 SoloLite (1 GHz ARM Cortex-A9) |
| **System Memory** | 512 MB (Stock Amazon Java UI idles at ~75–85% utilization) |
| **Firmware Target** | `5.18.1.1.1` (build `476967 023`) |
| **Revival Vector** | **SpringBreak** (filler-file + Kindle Store vector) |
| **Primary Reader** | **KOReader** in **No-Framework** mode (Amazon Java UI suspended) |
| **E-Waste Impact** | Extends device lifespan indefinitely; adds modern EPUB/PDF reading & Wi-Fi sync |

---

## Required Packages & Downloads

Each package serves a distinct, critical purpose in the revival pipeline:

1. **SpringBreak Exploit (`springbreak.zip`):**
   * *What it does:* The initial software exploit, released by **Penguins184** (KindleModding). It fills the Kindle with thousands of nested folders, then abuses the Kindle Store / `com.lab126.fts` + `com.lab126.winmgr` path to schedule a `SET.SCFG` ToDo document that runs KindleModding's online `jb.sh` jailbreak script. Officially supports **KT4/PW4 on 5.18.1.1.1**.
2. **KindleModding `jb.sh` / Jailbreak Hotfix:**
   * *What it does:* Downloaded and applied automatically by the SpringBreak payload. It installs the jailbreak hotfix, blocks OTA updates, and installs the KPM package manager so open-root capability survives reboots.
3. **MobileRead Package Installer / MRPI (`kual-mrinstaller-*.tar.xz`):**
   * *What it does:* A specialized command-line package manager for Kindle. Invoked on-device via `;log mrpi` to safely verify, extract, and flash signed `.bin` packages directly into the root partition.
4. **KUAL Booklet (`KUAL-*-coplate.tar.xz`):**
   * *What it does:* *Kindle Unified Application Launcher*. Installs a touch-friendly launcher document directly into your Kindle home library, allowing you to launch custom utilities, shell scripts, and KOReader.
5. **JailBreak Root Hotfix (`JailBreak-*-FW-5.x-hotfix.zip`):**
   * *What it does:* A permanent root persistence package maintained by NiLuJe. It secures system keys and boot hooks to ensure your device stays open and liberated even if system settings are reset.
6. **KOReader for Kindle (`koreader-kindle-v*.zip`):**
   * *What it does:* The core open-source reading engine (Legacy Kindle ARM build). Replaces the stock Amazon reading app with a fast, customizable reader featuring full EPUB/PDF support and built-in SSH/SFTP servers.

---

## Step 1: Pre-Flight Check & Full Flash Backup

### ⚠️ Real-World Issue #1: Kindle Not Detected in macOS Finder
* **The Symptom:** You plug the Kindle into your Mac with a USB cable, the orange charging LED lights up, but no volume appears in Finder or `/Volumes/`.
* **The Cause:** 
  1. **Charge-Only Micro-USB Cable:** A vast majority of older micro-USB cables only have power wires and lack internal data lines (`D+`/`D-`). If the Kindle screen does not switch to **"USB Drive Mode"**, the cable cannot transfer data.
  2. **macOS "Allow accessory to connect" prompt:** On Apple Silicon Macs, macOS blocks USB devices until you manually click **"Allow"** in the top-right notification banner.
  3. **USB-C Hub / Dongle:** Certain multi-port dongles fail to negotiate USB 2.0 mass storage properly.
* **The Fix:** Switch to a verified data cable, approve the macOS security banner, and plug directly into your Mac.

### Perform a Bit-for-Bit Local Backup
Once `/Volumes/Kindle` mounts, create an immutable local backup on your computer before touching anything:

```bash
BACKUP_DIR="$HOME/Kindle_KT4_Backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR/user_storage"

# Mirror complete user storage
rsync -av --progress \
  --exclude='.Spotlight-V100' \
  --exclude='.fseventsd' \
  --exclude='.Trashes' \
  /Volumes/Kindle/ "$BACKUP_DIR/user_storage/"

# Save firmware and partition metadata
echo "VERSION: $(cat /Volumes/Kindle/system/version.txt)" > "$BACKUP_DIR/device_info.txt"
diskutil info /Volumes/Kindle >> "$BACKUP_DIR/device_info.txt"
```

---

## Step 2: Prevent Unwanted OTA Updates

To stop background Amazon processes from downloading unwanted updates or reverting modifications:

```bash
# Create an immutable dummy update directory (blocks OTA downloader)
mkdir -p /Volumes/Kindle/update.bin.tmp.partial
```

---

## Step 3: Jailbreak with SpringBreak

> **Why SpringBreak?** On firmware **5.18.1.1.1**, the older Mesquito/WinterBreak vector **does not work** ("Winterbreak/Mesquito does NOT work on firmware 5.18.1 and beyond"). SpringBreak is the method that officially supports **KT4/PW4 on 5.18.1.1.1**.

> ⚠️ **Do NOT fill the Kindle beforehand** (unlike WinterBreak). SpringBreak creates thousands of nested folders itself and needs free space. Stay off Wi-Fi until the Store step.

1. **Unplug the Kindle**, put it in **Airplane Mode**, then **reboot** it (hold the power button → *Restart*).
2. **Re-plug** the Kindle into your computer. For the tool to detect it, the volume must be **mounted**:
   * **macOS:** it mounts automatically at `/Volumes/Kindle`.
   * **Linux:** open it once in your file manager, or run `udisksctl mount -b /dev/sdX1` (it then appears under `/run/media/<user>/Kindle`).
   * The Kindle screen must show the plain "USB drive" screen — **not** a "disconnect" button. If it shows the latter, the device/firmware is not supported.
3. **Download and unzip SpringBreak** on your computer:
   ```bash
   curl -L https://github.com/KindleModding/SpringBreak/releases/latest/download/springbreak.zip -o springbreak.zip
   python3 -m zipfile -e springbreak.zip springbreak/   # or use 7-Zip / unzip
   ```
4. **Run the binary** matching your OS and select your Kindle from the list:
   * **Linux:** `chmod +x ./springbreak-linux && ./springbreak-linux`
   * **Windows:** double-click `springbreak.exe`
   * **macOS:** `chmod +x ./springbreak-darwin && ./springbreak-darwin`
5. The tool fills the Kindle with nested filler folders. **This takes a while** (considerably longer on Windows than on Linux).
6. **Unplug** the Kindle. On the home screen, tap the **Store (shopping cart)** icon. When prompted, **turn off Airplane Mode** (Wi-Fi **is** required). You can turn Wi-Fi back off as soon as SpringBreak has loaded.
7. SpringBreak loads inside the Store and text streams down the screen. After a few seconds the **success screen** appears and the Kindle reboots into an **open-root (jailbroken) state**.

### ⚠️ Real-World Issue #2: Opening the Store Shows "Application Error"
* **The Symptom:** After unplugging, tapping the Store icon throws an *"Application Error"*.
* **The Fix:** Unplug and re-plug the Kindle once or twice until the Store loads correctly, then tap the Store icon again.

### ⚠️ Real-World Issue #3: The Kindle Is Not Listed by SpringBreak
* **The Cause:** The Kindle volume is not mounted, or a charge-only cable is in use.
* **The Fix:** Use a data cable and make sure the volume is mounted (Linux: open it in your file manager first; macOS: verify `/Volumes/Kindle` exists).

### ⚠️ Real-World Issue #4: Filling Fails Due to Lack of Space
* **The Cause:** Not enough free space for the nested filler folders.
* **The Fix:** Delete some existing content, re-run the script once to remove any partial fillers, then retry.

---

## Step 4: Clean Up After SpringBreak

**This step is mandatory** — skipping it makes the Kindle take **15+ minutes** to boot because the filler folders are still present.

1. Wait until the Kindle has rebooted back to the **home screen** and the UI has settled.
2. **Plug the Kindle back in**, run the **same binary** again, select the Kindle, and let it **clean up** (it removes the filler folders).
3. Unplug cleanly.
4. Remove any leftover update files with a **`.bin`** extension from the Kindle root, if present.
5. **Verify:** the device boots in a normal amount of time and the jailbreak is active (OTA updates are now blocked automatically).

---

## Step 5: Deploy KUAL, Root Hotfix & KOReader via MRPI

1. Connect the Kindle to your Mac via USB.
2. Extract the utility packages onto `/Volumes/Kindle/`:
   * **MRPI:** Extracts `extensions/MRInstaller/` to root.
   * **Payloads:** Copy `Update_jailbreak_hotfix_*.bin` and `Update_KUALBooklet_*.bin` into `/Volumes/Kindle/mrpackages/`.
   * **KOReader:** Extract `koreader/` and `extensions/koreader/` directly onto the root.
   * **Books:** Create `/Volumes/Kindle/books/` for your EPUBs.
3. Eject and unplug cleanly:
   ```bash
   dot_clean /Volumes/Kindle
   diskutil eject /Volumes/Kindle
   ```
4. On your Kindle home screen, tap the search bar, type:
   ```text
   ;log mrpi
   ```
   and tap Enter.
5. The screen will invoke the MobileRead Package Installer, displaying terminal text as it installs KUAL Booklet and the permanent root hotfix.
6. The device will reboot. Once booted, a new **KUAL** booklet will appear in your library!

---

## Step 6: Running KOReader in "No-Framework" Mode

1. Open **KUAL** from your library.
2. Tap **KOReader** → select **"Start KOReader (no framework)"**.
3. The screen will briefly flash black as the Amazon GUI shuts down.

### ⚠️ Real-World Issue #5: Why Exiting KOReader Restarts the Kindle
* **The Symptom:** When you tap Exit inside KOReader, the screen flashes and the Kindle reboots / reloads the interface.
* **The Reason:** In "No-Framework" mode, KOReader executes `stop lab126_gui` on launch, shutting down Amazon's bloated Java system to free up **~70% of the device's RAM** (dropping memory usage from ~85% to under 25%).
* When you exit KOReader, the wrapper script executes `start lab126_gui`, which prompts Upstart to reload the Amazon environment. This warm restart is completely normal and intentional.

---

## Step 7: Wireless EPUB Transfer via macOS Finder (Zero Cables!)

Once inside KOReader, you never need to connect a physical micro-USB cable again:

1. In KOReader, tap the very top edge of the screen to reveal the menu.
2. Tap the **Network (Globe / Wi-Fi icon)** tab.
3. Tap **Wi-Fi connection** to connect to your home Wi-Fi.
4. Tap the arrow `>` next to **SSH server**:
   * Turn **SSH server** to **ON**.
   * Ensure **"Allow login without password"** is enabled.
5. KOReader will display an alert with your Kindle's IP address (e.g., `192.168.1.50`, port `2222`).

### Mount Directly in macOS Finder
1. On your Mac, open **Finder**.
2. Press **`Cmd + K`** (or click menu bar: **Go** → **Connect to Server...**).
3. Enter the server address:
   ```text
   sftp://<YOUR_KINDLE_IP>:2222
   ```
4. Click **Connect** (Username: `root`, leave Password blank).
5. Your Kindle mounts in Finder like an external network drive! Drag and drop any `.epub`, `.pdf`, or `.mobi` files straight into `/books/`.

---

## 📱 Bonus App: Kindle Drop — Wireless Web GUI (Mac & Phone)

Included in this repository is **Kindle Drop**, a lightweight, responsive web app that allows you to drag-and-drop books from your **Mac** or upload directly from your **iPhone / Android phone**:

### Features
* 📱 **Mobile-Friendly Phone Uploader:** Generates a local QR code on your Mac screen—scan with your phone camera to instantly open the uploader in your mobile browser.
* 🔍 **Auto-Detection:** Scans your local home network to discover your Kindle's IP automatically.
* 📚 **Drag-and-Drop Dropzone:** Multi-file upload with live progress bars directly to `/mnt/us/books/`.
* 📖 **Remote Library Explorer:** View, search, and delete books stored on your Kindle without touching the device.

### How to Run
```bash
./kindle_drop/run.sh
```
* **On Mac:** Automatically opens `http://localhost:5050` in your browser.
* **On Phone:** Connect to the same Wi-Fi and scan the on-screen QR code (or visit `http://<YOUR_MAC_IP>:5050`).

---

## Troubleshooting Quick-Reference

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **Not detected in Finder** | Charge-only cable or macOS USB permission | Use a data micro-USB cable; allow accessory on macOS Apple Silicon. |
| **SpringBreak does not list my Kindle** | Volume not mounted, or charge-only cable | Mount the volume (Linux: open it in your file manager) and use a data USB cable. |
| **Store shows "Application Error"** | Store cache glitch after unplug | Unplug and re-plug the Kindle once or twice, then reopen the Store. |
| **Kindle takes 15+ min to boot** | Filler folders not cleaned up | Re-run the SpringBreak binary and let it perform clean-up (Step 4). |
| **SpringBreak filling fails** | Not enough free space | Free up space, re-run once to clear partial fillers, then retry. |
| **Kindle restarts on KOReader exit** | Normal "No-Framework" behavior | Expected: restarting Amazon Java GUI (`lab126_gui`) after exit. |
| **USB mode not popping up in KOReader** | Amazon daemons suspended | Expected in No-Framework mode: use Kindle Drop / Wi-Fi SFTP, or exit KOReader. |
| **KOReader crashes back to home menu** | FAT32 corruption (`FSCK0000.REN` files) | Caused by pulling cable or dead battery. Reinstall clean KOReader files while preserving `settings/`. |
| **Wireless book sync** | Avoids fragile micro-USB port wear | Turn on SSH server in KOReader; use Kindle Drop GUI or macOS Finder (`Cmd+K`). |

---

## License & Credits

* **SpringBreak Exploit:** Created by **Penguins184** (KindleModding) — [write-up](https://penguins184.xyz/blog/springbreak-jailbreak/)
* **Initial LPE & core ideas:** **Hhhhhhhhh**; filler-file vector credited to **Hackerdude**
* **MobileRead Package Installer & Hotfix:** Maintained by **NiLuJe** (MobileRead)
* **KUAL:** Developed by **twobob**, **StepK**, **coplate**, **NiLuJe**
* **KOReader:** The open-source KOReader development team ([koreader.rocks](https://koreader.rocks))
