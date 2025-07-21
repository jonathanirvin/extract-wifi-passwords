import subprocess
import re

def get_saved_wifi_profiles():
    try:
        result = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles'],
            text=True,
            stderr=subprocess.DEVNULL
        )
        profiles = re.findall(r"All User Profile\s*:\s(.*)", result)
        return [profile.strip() for profile in profiles]
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving profiles: {e}")
        return []

def get_wifi_password(profile_name):
    try:
        result = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'],
            text=True,
            stderr=subprocess.DEVNULL
        )
        match = re.search(r"Key Content\s*:\s(.*)", result)
        return match.group(1).strip() if match else "(none or not saved)"
    except subprocess.CalledProcessError:
        return "(access denied or invalid profile)"

def main():
    profiles = get_saved_wifi_profiles()
    if not profiles:
        print("❌ No saved Wi-Fi profiles found.")
        return

    print("Saved Wi-Fi Networks and Passwords:\n")
    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"� SSID: {profile}")
        print(f"� Password: {password}")
        print("-" * 40)

if __name__ == "__main__":
    main()
