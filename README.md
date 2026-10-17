# Kindle Paperwhite 2 Revival & Sustainability Guide
### *Giving 10+ Year Old E-Readers a Second Life & Reducing E-Waste*

> A complete, field-tested guide to revitalizing the **Kindle Paperwhite 2 (Model EY21)** running final firmware **5.12.2.2** by liberating it from proprietary bloat, installing **KUAL**, and deploying **KOReader** in a lightweight, energy-efficient **No-Framework** mode with wireless macOS Finder transfers.

> [!TIP]
> **🤖 Pair-Programming with a Local CLI AI Agent:**
> Because this revival process involves multi-stage payload staging, checksum validation, volume management, and precise timing, it is **highly recommended to use a CLI-based autonomous AI agent** (such as Google Antigravity, Claude Code, Aider, or similar tools with direct terminal or PowerShell access).
> 
> **How to use:** Simply pass this GitHub repository URL (`https://github.com/ars-codelab/kindle-sustainability-project`) to your CLI agent as context. The agent can read this guide directly and handle or guide you through most steps end-to-end:
> * **Safely Automate Backups:** Detect volume mounts and perform bit-for-bit local backups automatically (`rsync`).
> * **Download & Verify Packages:** Fetch the exact firmware-matched exploit files, verify MD5 checksums, and stage directories without manual errors.
> * **Clean OS Metadata & Manage Drives:** Automatically strip hidden OS artifacts (e.g., macOS `dot_clean`, AppleDouble files) and safely unmount/eject storage.
> * **Step-by-Step Guidance:** Dynamically troubleshoot in real time (e.g., recognizing gesture timing, handling application popups, configuring wireless SFTP).

---

## ✨ What You Get: The Payoff (Why It’s Worth the Effort)

Before embarking on this multi-step process, here is exactly what your Kindle Paperwhite 2 will look like once finished:

* ⚡ **Blazing Fast Performance:** RAM consumption drops from **~85% down to under 25%** by suspending Amazon’s heavy Java operating stack (`lab126_gui`). Menus, library navigation, and page turns become instantaneous.
* 📖 **Universal Format Freedom:** Full native support for **EPUB, PDF, CBZ, CBR, FB2, MOBI, and TXT**. No more converting files through Calibre or Amazon Send-to-Kindle services.
* 📶 **Zero-Cable Wireless Sync:** Mount your Kindle directly inside **macOS Finder** as a network drive over your home Wi-Fi (`Cmd + K` via SFTP). Drag and drop books without ever needing a physical USB cable again.
* 🔋 **Extended Battery Life & Zero Distractions:** Strips out background ad tracking, store analytics, and battery-draining indexing loops. Leaves you with a 100% distraction-free reading machine.
* 🛠️ **Modern E-Reader Feature Suite:** Highly granular typography controls, automated margin cropping for PDFs, dual-page mode, dictionary lookups, reading statistics, and cross-device reading progress sync (KOReader Sync).
* ♻️ **10+ More Years of Usable Life:** Eliminates e-waste by turning a 2013 device into a modern, responsive daily driver that outperforms many budget 2026 e-readers.

---

## 🌍 Why This Project Exists: Fighting Planned Obsolescence & E-Waste

Consumer electronics are frequently abandoned not because the hardware has failed, but because modern proprietary software outgrows older hardware constraints.

* **The Hardware Still Shines:** The Kindle Paperwhite 2 features an exceptional 212 PPI Carta e-ink display, durable LED front-lighting, and solid battery life that can easily last for weeks.
* **The Software Bottleneck:** Out of the box, Amazon's proprietary Java application stack (`lab126_gui`), background telemetry, indexing services, and store integrations consume **75% to 85% of the device's modest RAM** (256 MB / 512 MB) at idle. This causes sluggish UI response, battery drain, and limits you to Amazon-approved document formats.
* **The Sustainable Solution:** Rather than discarding functional e-readers into landfills, we can remove unwanted background packages, bypass legacy software constraints, and install **KOReader**—a blazing-fast, open-source document viewer. 
* **The Result:** Memory usage drops from **~85% down to under 25%**, page turns become instantaneous, battery life improves, and the device gains native support for open standards (EPUB, CBZ, PDF) and wireless LAN transfers.

---

## ⚠️ DISCLAIMER — PROCEED AT YOUR OWN RISK ⚠️

> **READ THIS CAREFULLY BEFORE CONTINUING:**
> 
> * **Hardware Modification Risks:** While this process is tested and verified, modifying your Kindle's root filesystem and boot scripts carries an inherent risk of soft-bricking or bootlooping the device.
> * **No Liability:** Neither the authors of this guide nor the open-source developers of WatchThis, KUAL, MRPI, or KOReader assume any responsibility for damaged hardware, lost data, or bricked devices.
> * **Model Compatibility:** This guide is specifically written and tested for the **Kindle Paperwhite 2 (Model EY21)** on official firmware **`5.12.2.2`**. Do **NOT** follow these exact payloads on different hardware models without consulting the appropriate device trees on MobileRead.
> * **Mandatory Backup:** Always create a complete, bit-for-bit local backup of your device's flash storage before making any filesystem modifications.

---

## Device & Target Specifications

| Parameter | Specification |
| :--- | :--- |
| **Target Hardware** | Kindle Paperwhite 2 (6th Generation, Model `EY21`, late 2013–2014) |
| **Processor** | Freescale/NXP i.MX6 SoloLite (1 GHz ARM Cortex-A9) |
| **System Memory** | 256 MB or 512 MB (Stock Amazon Java UI idles at ~75–85% utilization) |
| **Firmware Target** | `5.12.2.2` (Final official software release for PW2) |
| **Revival Vector** | **WatchThis** (Demo mode package injection method) |
| **Primary Reader** | **KOReader** in **No-Framework** mode (Amazon Java UI suspended) |
| **E-Waste Impact** | Extends device lifespan indefinitely; adds modern EPUB/PDF reading & Wi-Fi sync |

---

## Required Packages & Downloads

Each package serves a distinct, critical purpose in the revival pipeline:

1. **WatchThis Exploit Package (`watchthis-jailbreak-r03.zip`):**
   * *What it does:* The initial software exploit. Leverages a vulnerability in the Kindle's Demo Mode setup to bypass signature verification and execute custom code on firmware `5.12.2.2`.
2. **WatchThis Custom Hotfix (`Update_hotfix_watchthis_custom.bin`):**
   * *What it does:* Included inside the WatchThis archive. It cleanly exits Demo Mode, applies partition patches, and installs custom developer keys into the device keystore so open-root capability survives reboots.
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
BACKUP_DIR="$HOME/Kindle_PW2_Backup_$(date +%Y%m%d_%H%M%S)"
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

## Step 3: Factory Reset & Enter Demo Mode

1. **Unplug the USB cable** from the Kindle.
2. Go to **Settings** (gear or `⋮` menu) → tap `⋮` again → tap **Reset** (or **Reset Device**). Confirm and allow the device to format and restart (1–2 minutes).
3. **Crucial Language Choice:** On the language setup screen, **you MUST select `English (United Kingdom)` (`en_GB`)**. The exploit structure expects British English system paths.
4. **Skip Wi-Fi Setup:** When the Wi-Fi list appears, tap any network, then tap **Cancel** to bring up the **Set Up Later** option. Do not connect to Wi-Fi yet.

### ⚠️ Real-World Issue #2: `;enter_demo` Shows No Response
* **The Symptom:** You tap the search bar, type `;enter_demo`, press Search/Enter, and nothing happens on screen.
* **The Reality:** This command **provides zero visual feedback or confirmation**. It silently flips an internal system flag.
* **The Fix:** Immediately after tapping Enter, **hold down the power button for 20–30 seconds** until the screen flashes and restarts. Upon booting, it will automatically launch the Demo Setup Wizard.

---

## Step 4: Demo Setup & Bypassing Demo Lockout

1. In the Demo Wizard:
   * Skip Wi-Fi setup when prompted.
   * Enter dummy store information (e.g. `1234`).
   * Skip searching for a demo payload.
   * Select the **Standard** demo type.
   * At the *"sideload content"* prompt, tap **Done**.

### ⚠️ Real-World Issue #3: Blank White Screen After Demo Setup
* **The Symptom:** The Kindle screen goes completely blank white and appears frozen.
* **The Fix:** The demo launcher simply failed to trigger an e-ink screen refresh. **Press the physical power button once briefly** (quick click) to sleep/wake the screen and force an e-ink redraw.

### ⚠️ Real-World Issue #4: "Configure Device - Missing Content" Lockout
* The screen displays: *"This demonstration device is either missing content or is disconnected from the network."*

### ⚠️ Real-World Issue #5: How to Execute the Secret Bypass Gesture
The bypass gesture is a **two-step timing combo** that requires specific technique on e-ink touchscreens:
1. **Step 1:** Tap the **bottom-right corner** of the screen with **two fingers simultaneously** (index & middle fingers together), then immediately lift them.
2. **Step 2:** In quick succession (within 0.5s), **swipe with one finger from right to left** across the bottom half of the screen.
3. *Rhythm tip:* *"tap-tap (with two fingers) ➔ swipe (with one finger)"*.

Once bypassed, the top search bar will appear!

---

## Step 5: Stage the WatchThis Payload

1. In the search bar on your Kindle, type:
   ```text
   ;demo
   ```
   and tap Enter.
2. Tap the **Sideload Content** option on screen.
3. **Plug the Kindle into your Mac via USB.**
4. From the extracted `watchthis-jailbreak-r03.zip`, copy the exact files for Paperwhite 2 (5.12.2.2):
   * Create directory `/Volumes/Kindle/.demo`
   * Copy `PW2-5.12.2.2.zip` directly into `/Volumes/Kindle/.demo/` (**DO NOT EXTRACT IT**)
   * Copy `demo.json` directly into `/Volumes/Kindle/.demo/`
   * Create an empty directory `/Volumes/Kindle/.demo/goodreads`
5. Eject cleanly:
   ```bash
   dot_clean /Volumes/Kindle
   diskutil eject /Volumes/Kindle
   ```

---

## Step 6: Trigger the Liberation Exploit

1. Tap **Done** at the "sideload content" prompt on the Kindle screen.

### ⚠️ Real-World Issue #6: "Application Error" When Exiting Demo Mode
* **The Symptom:** Tapping Exit pops up an alert: *"Application error: Please try again"* with only a "Close" button.
* **The Fix:**
  * Tap **Close**.
  * Check the top navigation bar: if the **Store (shopping cart) icon** is visible, proceed directly!
  * If frozen, perform a hard reboot (hold power button for 15s), re-open `;demo` → **Sideload Content** → tap **Done** (files are already safely on the device).
2. **Paperwhite 2 Trigger:** Tap the **Store icon (shopping cart)** at the top of the screen.
3. Select **Help & User Guides** → tap **Get Started**.
4. The device will flash, display the exploit overlay on screen, and reboot into an open-root state!

---

## Step 7: Install WatchThis Custom Hotfix

The Kindle will reboot back into Demo Mode. To permanently exit demo mode and preserve root access:

1. Perform the bypass gesture (two-finger tap bottom right, swipe left).
2. In the search bar, type:
   ```text
   ;uzb
   ```
   and tap Enter (forces USB mass storage mode).
3. Connect the Kindle to your Mac.
4. Copy `Update_hotfix_watchthis_custom.bin` to the root of `/Volumes/Kindle/`.
5. Eject and unplug cleanly:
   ```bash
   dot_clean /Volumes/Kindle
   diskutil eject /Volumes/Kindle
   ```
6. In the search bar on the Kindle, type:
   ```text
   ;dsts
   ```
   and tap Enter (opens Device Settings).
7. Tap **Update Your Kindle** (now clickable).
8. The Kindle will install the hotfix, exit demo mode permanently, and reboot to the clean, stock home screen with root keys installed.

---

## Step 8: Deploy KUAL, Root Hotfix & KOReader via MRPI

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

## Step 9: Running KOReader in "No-Framework" Mode

1. Open **KUAL** from your library.
2. Tap **KOReader** → select **"Start KOReader (no framework)"**.
3. The screen will briefly flash black as the Amazon GUI shuts down.

### ⚠️ Real-World Issue #7: Why Exiting KOReader Restarts the Kindle
* **The Symptom:** When you tap Exit inside KOReader, the screen flashes and the Kindle reboots / reloads the interface.
* **The Reason:** In "No-Framework" mode, KOReader executes `stop lab126_gui` on launch, shutting down Amazon's bloated Java system to free up **~70% of the device's RAM** (dropping memory usage from ~85% to under 25%).
* When you exit KOReader, the wrapper script executes `start lab126_gui`, which prompts Upstart to reload the Amazon environment. This warm restart is completely normal and intentional.

---

## Step 10: Wireless EPUB Transfer via macOS Finder (Zero Cables!)

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
| **`;enter_demo` does nothing** | Silent flag; provides no popup | Hold power button for 25s immediately to reboot into Demo Wizard. |
| **Blank white screen** | E-ink screen refresh lag | Click power button once briefly to sleep/wake and redraw screen. |
| **Demo lockout screen** | Demo mode missing content | Perform secret gesture: 2-finger tap bottom-right ➔ swipe left. |
| **"Application error" on exit** | Demo framework glitch | Tap Close and look for Store icon; or hard reboot (15s) and re-open `;demo`. |
| **Kindle restarts on KOReader exit** | Normal "No-Framework" behavior | Expected: restarting Amazon Java GUI (`lab126_gui`) after exit. |
| **USB mode not popping up in KOReader** | Amazon daemons suspended | Expected in No-Framework mode: use Kindle Drop / Wi-Fi SFTP, or exit KOReader. |
| **KOReader crashes back to home menu** | FAT32 corruption (`FSCK0000.REN` files) | Caused by pulling cable or dead battery. Reinstall clean KOReader files while preserving `settings/`. |
| **Wireless book sync** | Avoids fragile micro-USB port wear | Turn on SSH server in KOReader; use Kindle Drop GUI or macOS Finder (`Cmd+K`). |

---

## License & Credits

* **WatchThis Exploit:** Created by **katadelos** (MobileRead)
* **MobileRead Package Installer & Hotfix:** Maintained by **NiLuJe** (MobileRead)
* **KUAL:** Developed by **twobob**, **StepK**, **coplate**, **NiLuJe**
* **KOReader:** The open-source KOReader development team ([koreader.rocks](https://koreader.rocks))
