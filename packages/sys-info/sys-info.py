import os
import sys
import platform
import socket
import psutil
import subprocess

def get_system_info():
    """Gather system information."""
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "Total RAM": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "Used RAM": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
        "Available RAM": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
        "Disk Usage": f"{psutil.disk_usage('/').percent}%",
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }
    return info

def display_info():
    """Print system information in a readable format."""
    print("\n--- System Information ---")
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    display_info()
