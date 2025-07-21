# 🔐 Extract Wi-Fi Passwords (Linux + Windows)

This repository provides Python scripts to extract **saved Wi-Fi SSIDs and their passwords** from the local system.

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
```

### 📋 What It Does

- Lists all saved Wi-Fi profiles using `nmcli`
- Extracts stored passwords (WPA/WPA2)
- Prints SSID and password pairs directly to the terminal

---

## 🪟 Windows: `extract-wifi-passwords-windows.py`

### 🔧 Requirements

- Python 3.x
- Windows 10 or 11

### ▶️ Usage

```bash
python extract-wifi-passwords-windows.py
```

### 📋 What It Does

- Uses the built-in `netsh` command to list saved Wi-Fi profiles
- Extracts plaintext passwords for each one (if saved)
- Outputs results to the terminal in a clean format

---

## 💻 Example Output

```text
📶 SSID: MyHomeNetwork
🔑 Password: supersecret123
----------------------------------------
📶 SSID: CoffeeShopFree
🔑 Password: (none or not saved)
----------------------------------------
```

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as long as attribution is preserved.

---

## ⚠️ Legal Notice

These scripts are intended for:

- Security education
- Personal use (e.g. recovering your own Wi-Fi passwords)
- Red team or penetration testing **with explicit authorization**

**Do not** use these tools on machines or networks you do not own or have permission to test. Unauthorized use may violate laws such as the CFAA and GDPR.

---

## 🙌 Author

Created by Jonathan Irvin  
Contributions welcome — feel free to fork, enhance, and open pull requests!
