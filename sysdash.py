import os
import platform
from datetime import datetime

import psutil
from art import *
from termcolor import colored


def create_bar(percent: float, width: int = 70) -> str:
    filled = int(width * percent / 100)
    return f"[{'█' * filled}{'░' * (width - filled)}] {percent:.1f}%"


def get_system_information():
    hostname = os.uname().nodename
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(colored("System Information".center(80), "cyan"))
    print(colored("╔" + "═" * 78 + "╗", "cyan"))
    print(colored(f"║ {'Time:':<12} {current_time:<63} ║", "cyan"))
    print(colored(f"║ {'Hostname:':<12} {hostname:<63} ║", "cyan"))
    print(colored(f"║ {'OS:':<12} {platform.system():<63} ║", "cyan"))
    print(colored("╚" + "═" * 78 + "╝\n", "cyan"))


def get_system_status():
    print(colored("System Status".center(80), "cyan") + "\n")
    metrics = [
        ("CPU", psutil.cpu_percent(), None),
        ("RAM", psutil.virtual_memory().percent, None),
        (
            "Disk",
            psutil.disk_usage("/").percent,
            "green" if psutil.disk_usage("/").percent < 80 else "red",
        ),
    ]

    for label, value, color in metrics:
        line = f"{label:<4} {create_bar(value)}"
        print(colored(line, color) if color else line)


def main():
    os.system("clear")
    tprint(f"{'Welcome':>20}", font="standard")
    get_system_information()
    get_system_status()


if __name__ == "__main__":
    main()
