import requests
from datetime import datetime
import os

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Banner
def banner():
    os.system("clear")
    print(f"""{CYAN}
   ▄████  ██▓███   ▄▄▄       ██▀███   ▄▄▄      ▓█████ ▒██   ██▒
  ██▒ ▀█▒▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▓█   ▀ ▒▒ █ █ ▒░
 ▒██░▄▄▄░▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▒███   ░░  █   ░
 ░▓█  ██▓▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓█  ▄  ░ █ █ ▒ 
 ░▒▓███▀▒▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▒▒██▒ ▒██▒
  ░▒   ▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░░ ▒░ ░▒▒ ░ ░▓ ░
   ░   ░ ░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ░  ░░░   ░▒ ░
 ░ ░   ░ ░░         ░   ▒     ░░   ░   ░   ▒      ░    ░    ░  
       ░               ░  ░   ░           ░  ░   ░  ░ ░    ░  
              {YELLOW}By Rishabh | R_IPinfofetch{RESET}
""")

# IP Tracker
def track_ip(ip):
    try:
        print(f"{GREEN}[+] Fetching data for IP: {ip}{RESET}")
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()

        if "bogon" in data:
            print(f"{RED}[!] Invalid or local IP address!{RESET}")
            return

        ip_data = {
            "IP": data.get("ip", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location": data.get("loc", "N/A"),
            "Org": data.get("org", "N/A"),
            "Timezone": data.get("timezone", "N/A"),
            "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        print(f"""{CYAN}
---------------------------
IP Address     : {ip_data['IP']}
City           : {ip_data['City']}
Region         : {ip_data['Region']}
Country        : {ip_data['Country']}
Location       : {ip_data['Location']}
ISP/Org        : {ip_data['Org']}
Timezone       : {ip_data['Timezone']}
Timestamp      : {ip_data['Timestamp']}
---------------------------{RESET}
        """)

        with open("ip_logs.txt", "a") as f:
            f.write(f"{ip_data['Timestamp']} - {ip_data['IP']} - {ip_data['City']}, {ip_data['Region']}, {ip_data['Country']} - {ip_data['Org']}\n")

    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")

# Main
def main():
    banner()
    while True:
        ip = input(f"{YELLOW}Enter IP to track (or 'exit' to quit): {RESET}")
        if ip.lower() == "exit":
            print(f"{GREEN}Exiting...{RESET}")
            break
        track_ip(ip)

if __name__ == "__main__":
    main()
