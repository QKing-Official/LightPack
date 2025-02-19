import psutil
import shutil
import os
import time
from datetime import timedelta
import keyboard  # to detect keyboard events

def get_cpu_usage():
    """Returns a list of CPU usage percentages for each core."""
    return psutil.cpu_percent(percpu=True)

def get_memory_usage():
    """Returns total, used, and free memory in GB."""
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024 ** 3), 2)
    used = round(memory.used / (1024 ** 3), 2)
    free = round(memory.free / (1024 ** 3), 2)
    return total, used, free

def get_disk_usage():
    """Returns total, used, and free disk space in GB."""
    total, used, free = shutil.disk_usage("/")
    return round(used / (1024 ** 3), 2), round(free / (1024 ** 3), 2)

def get_uptime():
    """Returns system uptime."""
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = int(now - boot_time)
    return str(timedelta(seconds=uptime_seconds))

def get_top_processes():
    """Returns top 5 processes sorted by CPU usage."""
    processes = [(p.info['pid'], p.info['name'], p.info['cpu_percent'], p.info['memory_percent']) for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    sorted_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    return sorted_processes

def display_system_stats():
    """Display the system stats like a simple htop."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    print("LightMonitor - System Stats")
    print("-" * 40)

    # CPU Usage
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage:")
    for i, usage in enumerate(cpu_usage):
        print(f"  Core {i+1}: {usage}%")
    
    # Memory Usage
    total_mem, used_mem, free_mem = get_memory_usage()
    print(f"\nMemory Usage:")
    print(f"  Total: {total_mem} GB")
    print(f"  Used: {used_mem} GB")
    print(f"  Free: {free_mem} GB")
    
    # Disk Usage
    used_disk, free_disk = get_disk_usage()
    print(f"\nDisk Usage:")
    print(f"  Used: {used_disk} GB")
    print(f"  Free: {free_disk} GB")
    
    # Uptime
    uptime = get_uptime()
    print(f"\nUptime: {uptime}")
    
    # Top Processes
    print("\nTop 5 Processes (by CPU Usage):")
    top_processes = get_top_processes()
    for i, process in enumerate(top_processes):
        print(f"{i + 1}. PID: {process[0]} | Name: {process[1]} | CPU: {process[2]}% | Mem: {process[3]}%")
    
    print("\nPress 'Ctrl+Q' to exit.")

def run_lightmonitor():
    """Run the LightMonitor in an infinite loop."""
    try:
        while True:
            display_system_stats()
            time.sleep(2)  # Update every 2 seconds

            # Check for Ctrl+Q (to quit the interactive shell)
            if keyboard.is_pressed('ctrl+q'):
                print("\nExiting LightMonitor...")
                break  # Exit the loop and stop the program

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, do nothing and continue
        print("\nCaught Ctrl+C. Press 'Ctrl+Q' to quit LightMonitor.")

if __name__ == "__main__":
    print("Welcome to LightMonitor! Press 'Ctrl+Q' to quit.")
    run_lightmonitor()
