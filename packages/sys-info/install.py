import os
import sys
import subprocess

def install():
    print("Installing System Info package...")

    # Get current directory where the package is downloaded
    package_dir = os.getcwd()

    # Path to the system info script
    script_path = os.path.join(package_dir, "sys_info.py")

    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return
    
    try:
        print("Installing required dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "psutil"], check=True)

        print("Running System Info package...")
        result = os.system(f"{sys.executable} {script_path}")

        if result == 0:
            print("System Info package installed and executed successfully!")
        else:
            print(f"Error running the script. Exit code: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install()
