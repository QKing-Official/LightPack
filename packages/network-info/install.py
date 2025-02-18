import os
import sys
import subprocess

def install():
    print("Installing Network Info package...")

    # Ensure the package directory exists
    package_dir = os.getcwd()  # Current directory
    script_path = os.path.join(package_dir, "network-info.py")

    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return

    try:
        # Install dependencies
        subprocess.run([sys.executable, "-m", "pip", "install", "psutil"], check=True)

        print("Network Info package installed successfully!")
    except Exception as e:
        print(f"Error during installation: {e}")

if __name__ == "__main__":
    install()
