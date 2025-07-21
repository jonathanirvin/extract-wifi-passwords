import subprocess

def get_saved_wifi_profiles():
    try:
        result = subprocess.check_output(
            ['nmcli', '-t', '-f', 'NAME,TYPE', 'connection', 'show'],
            text=True
        )
        profiles = [
            line.split(':')[0]
            for line in result.strip().split('\n')
            if ':802-11-wireless' in line
        ]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error listing profiles: {e}")
        return []

def get_wifi_password(profile_name):
    try:
        result = subprocess.check_output(
            ['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', profile_name],
            text=True
        ).strip()
        return result if result else "(none)"
    except subprocess.CalledProcessError:
        return "(none or not saved)"

def main():
    profiles = get_saved_wifi_profiles()
    if not profiles:
        print("❌ No saved Wi-Fi profiles found.")
        return

    print("Saved Wi-Fi Networks and Passwords:\n")
    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"📶 SSID: {profile}")
        print(f"🔑 Password: {password}")
        print("-" * 40)

if __name__ == "__main__":
    main()

