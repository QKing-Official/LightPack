import os
import sys
import psutil

def get_disk_usage(path='/'):
    """Get disk usage information for a given path."""
    usage = psutil.disk_usage(path)
    return {
        "Total": usage.total / (1024 ** 3),
        "Used": usage.used / (1024 ** 3),
        "Free": usage.free / (1024 ** 3),
        "Percentage": usage.percent
    }

def get_largest_files(path='/', n=10):
    """Get the largest files in a given directory."""
    largest_files = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path) / (1024 ** 2)  # Size in MB
                largest_files.append((size, file_path))
            except OSError:
                continue
    largest_files.sort(reverse=True, key=lambda x: x[0])
    return largest_files[:n]

def display_disk_info():
    """Print disk usage information."""
    print("\n--- Disk Usage Information ---")
    usage = get_disk_usage()
    for key, value in usage.items():
        print(f"{key}: {value:.2f} GB" if key != "Percentage" else f"{key}: {value}%")

    print("\n--- Largest Files ---")
    largest_files = get_largest_files()
    for size, file in largest_files:
        print(f"Size: {size:.2f} MB, Path: {file}")

if __name__ == "__main__":
    display_disk_info()
