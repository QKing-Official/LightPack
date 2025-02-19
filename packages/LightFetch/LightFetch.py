import os
import platform
import psutil
import socket
import cpuinfo
import shutil
from datetime import datetime

def get_system_info():
    """Get system information for LightFetch"""
    system_info = {}

    # Hostname
    system_info['hostname'] = socket.gethostname()

    # OS
    system_info['os'] = platform.system()
    system_info['os_version'] = platform.version()

    # CPU
    cpu = cpuinfo.get_cpu_info()
    system_info['cpu'] = cpu.get('processor', 'Unknown CPU')  # Safely access CPU info
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)

    # RAM
    system_info['ram'] = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # GB

    # Disk Usage
    total, used, free = shutil.disk_usage("/")
    system_info['disk'] = round(used / (1024 ** 3), 2)  # GB

    # Python version
    system_info['python_version'] = platform.python_version()

    # Uptime
    uptime_seconds = int(psutil.boot_time())
    uptime = datetime.fromtimestamp(uptime_seconds)
    system_info['uptime'] = datetime.now() - uptime

    return system_info

def print_system_info(info):
    """Print system information like neofetch"""
    
    # Improved ASCII art icon
    ascii_icon = r"""
      _______________________
     |  _________________    |
     | |                 |   |
     | |    LIGHTFETCH   |   |
     | |                 |   |
     | |    _________    |   |
     | |   |         |   |   |
     | |   |  [==]   |   |   |
     | |   |_________|   |   |
     | |_________________|   |
     |_______________________|
    """
    
    print(ascii_icon)
    print(f"            {info['hostname']}")
    print(f"        OS: {info['os']} {info['os_version']}")
    print(f"     Kernel: {info['cpu']}")
    print(f"      RAM: {info['ram']} GB")
    print(f"    Disk: {info['disk']} GB used")
    print(f"   Python: {info['python_version']}")
    print(f"   Uptime: {info['uptime']}")
    print(f" CPU Cores: {info['cpu_cores']}")
    print("\n")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
