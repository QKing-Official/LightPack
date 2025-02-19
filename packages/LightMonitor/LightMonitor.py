import psutil
import shutil
import os
import time
from datetime import timedelta


#some random stuff what fetches usage etc

def get_cpu_usage():
    return psutil.cpu_percent(percpu=True)

def get_memory_usage():
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024 ** 3), 2)
    used = round(memory.used / (1024 ** 3), 2)
    free = round(memory.free / (1024 ** 3), 2)
    return total, used, free

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return round(used / (1024 ** 3), 2), round(free / (1024 ** 3), 2)

def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = int(now - boot_time)
    return str(timedelta(seconds=uptime_seconds))

def get_top_processes():
    processes = [(p.info['pid'], p.info['name'], p.info['cpu_percent'], p.info['memory_percent']) for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    sorted_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    return sorted_processes

def display_system_stats():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    print("LightMonitor - System Stats")
    print("-" * 40)

    cpu_usage = get_cpu_usage()
    print(f"CPU Usage:")
    for i, usage in enumerate(cpu_usage):
        print(f"  Core {i+1}: {usage}%")
    
    total_mem, used_mem, free_mem = get_memory_usage()
    print(f"\nMemory Usage:")
    print(f"  Total: {total_mem} GB")
    print(f"  Used: {used_mem} GB")
    print(f"  Free: {free_mem} GB")
    
    used_disk, free_disk = get_disk_usage()
    print(f"\nDisk Usage:")
    print(f"  Used: {used_disk} GB")
    print(f"  Free: {free_disk} GB")
    
    uptime = get_uptime()
    print(f"\nUptime: {uptime}")
    
    print("\nTop 5 Processes (by CPU Usage):")
    top_processes = get_top_processes()
    for i, process in enumerate(top_processes):
        print(f"{i + 1}. PID: {process[0]} | Name: {process[1]} | CPU: {process[2]}% | Mem: {process[3]}%")
    
    print("\nPress Ctrl+C to exit.")

def run_lightmonitor():
    try:
        while True:
            display_system_stats()
            time.sleep(2)  # Update every 2 seconds
    except KeyboardInterrupt:
        print("\nCaught Ctrl+C. Exiting LightMonitor...")
        # You can place any additional cleanup logic here
        pass  # Continue without crashing the whole script

if __name__ == "__main__":
    run_lightmonitor()
