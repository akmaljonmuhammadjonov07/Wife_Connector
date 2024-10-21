import subprocess

def get_wifi_passwords():
    profiles = subprocess.check_output('netsh wlan show profiles', encoding='utf-8').split('\n')
    for profile in profiles:
        if "All User Profile" in profile:
            wifi_name = profile.split(":")[1].strip()
            password_data = subprocess.check_output(f'netsh wlan show profile "{wifi_name}" key=clear', encoding='utf-8')
            for line in password_data.split('\n'):
                if "Key Content" in line:
                    print(f'Wi-Fi: {wifi_name}, Password: {line.split(":")[1].strip()}')
                    break

get_wifi_passwords()