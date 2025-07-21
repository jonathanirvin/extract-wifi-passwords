# 🔐 Extract Wi-Fi Passwords (Linux + Windows)

This repository provides simple Python scripts to extract **saved Wi-Fi SSIDs and their passwords** from the local system.

- ✅ **Linux**: Uses `nmcli` to extract from NetworkManager
- ✅ **Windows**: Uses `netsh` to extract from saved WLAN profiles

> ⚠️ For **educational and authorized use only**. Do **not** use these scripts on devices you do not own or without explicit permission.

---

## 📁 Contents

- `extract-wifi-passwords-linux.py` – For extracting Wi-Fi passwords on Linux
- `extract-wifi-passwords-windows.py` – For extracting Wi-Fi passwords on Windows

---

## 🐧 Linux: `extract-wifi-passwords-linux.py`

### 🔧 Requirements

- Python 3.x
- `nmcli` (comes with NetworkManager on most Linux distros)

### ▶️ Usage

```bash
python3 extract-wifi-passwords-linux.py
