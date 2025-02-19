import psutil
import shutil
import os
import time
import keyboard  # To detect keypress events
from datetime import timedelta  # For uptime formatting

# Function to get the CPU usage percentage for each core
def get_cpu_usage():
    """Fetch the CPU usage for each core."""
    return psutil.cpu_percent(percpu=True)

# Function to get memory usage (total, used, and free)
def get_memory_usage():
    """Fetch memory usage details (total, used, free)."""
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024 ** 3), 2)  # Convert bytes to GB
    used = round(memory.used / (1024 ** 3), 2)
    free = round(memory.free / (1024 ** 3), 2)
    return total, used, free

# Function to get disk usage (used and free space)
def get_disk_usage():
    """Fetch disk usage details (used, free)."""
    total, used, free = shutil.disk_usage("/")
    return round(used / (1024 ** 3), 2), round(free / (1024 ** 3), 2)  # Convert to GB

# Function to get the system uptime
def get_uptime():
    """Fetch the system's uptime (how long the system has been running)."""
    boot_time = psutil.boot_time()  # Get the system boot time
    now = time.time()  # Get the current time
    uptime_seconds = int(now - boot_time)  # Calculate uptime in seconds
    return str(timedelta(seconds=uptime_seconds))  # Convert seconds to a readable format (e.g., days, hours)

# Function to get the top 5 processes based on CPU usage
def get_top_processes():
    """Fetch top 5 processes consuming the most CPU."""
    processes = [
        (p.info['pid'], p.info['name'], p.info['cpu_percent'], p.info['memory_percent'])
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    ]
    sorted_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]  # Sort by CPU usage
    return sorted_processes

# Function to display system statistics in a user-friendly format
def display_system_stats():
    """Clear the screen and display system stats like CPU, Memory, Disk, Uptime, and Top Processes."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    print("LightMonitor - System Stats")
    print("-" * 40)

    # Display CPU Usage for each core
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage:")
    for i, usage in enumerate(cpu_usage):
        print(f"  Core {i + 1}: {usage}%")
    
    # Display Memory Usage (Total, Used, Free)
    total_mem, used_mem, free_mem = get_memory_usage()
    print(f"\nMemory Usage:")
    print(f"  Total: {total_mem} GB")
    print(f"  Used: {used_mem} GB")
    print(f"  Free: {free_mem} GB")
    
    # Display Disk Usage (Used, Free)
    used_disk, free_disk = get_disk_usage()
    print(f"\nDisk Usage:")
    print(f"  Used: {used_disk} GB")
    print(f"  Free: {free_disk} GB")
    
    # Display System Uptime
    uptime = get_uptime()
    print(f"\nUptime: {uptime}")
    
    # Display Top 5 Processes by CPU Usage
    print("\nTop 5 Processes (by CPU Usage):")
    top_processes = get_top_processes()
    for i, process in enumerate(top_processes):
        print(f"{i + 1}. PID: {process[0]} | Name: {process[1]} | CPU: {process[2]}% | Mem: {process[3]}%")
    
    print("\nPress 'Q' to exit...")  # Prompt to exit

# Main function to run the LightMonitor
def run_lightmonitor():
    """Run the LightMonitor in a continuous loop, displaying system stats every few seconds."""
    try:
        while True:
            display_system_stats()  # Display system stats
            time.sleep(2)  # Wait for 2 seconds before refreshing the stats

            # Wait for 'Q' key to exit the loop
            if keyboard.is_pressed('q'):  # Check if 'Q' key is pressed
                print("\nExiting LightMonitor...")
                break  # Exit the loop when 'Q' key is pressed

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully, so it doesn't crash the program
        print("\nCaught Ctrl+C. Exiting LightMonitor.")

# Entry point of the script
if __name__ == "__main__":
    print("Welcome to LightMonitor! Press 'Q' to quit.")
    run_lightmonitor()  # Start monitoring the system
