import subprocess
from colorama import Fore

ip_list = {
    'Inf 1': '192.168.71.2',
    'Inf 2': '192.168.71.3',
    'Inf 3': '192.168.71.4',
    'Inf 4': '192.168.71.5',
    'Est 1': '192.168.71.9',
    'Far 1': '192.168.71.10',
    'Cli 1': '192.168.71.11',
    'Mat 1': '192.168.71.12',
    'Mat 2': '192.168.71.13',
    'Con 1': '192.168.71.14',
    'Gua 1': '192.168.71.15',
    'Gua 2': '192.168.71.16',
    'Ima 1': '192.168.183.3',
    'Lab 1': '192.168.184.3',
}


for name, ip in ip_list.items():
    res = subprocess.run(["ping", ip, "-c", "1"], stdout=subprocess.DEVNULL)
    if res.returncode == 0:
        print(f"{Fore.RESET} {name} | {ip} | Status: {Fore.GREEN} UP")
    else:
        print(f"{Fore.RESET} {name} | {ip} | Status: {Fore.RED} DOWN")
        subprocess.run(["notify-send", "-a", "Server Status",
                        f"{name} | {ip} | Status: DOWN"])
