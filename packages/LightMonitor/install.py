import subprocess
import sys
import os

def install_requirements():
    """Install required packages via pip."""
    required_packages = [
        'psutil',  # Required for CPU, memory, and process information
    ]

    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_lightmonitor():
    """Install the LightMonitor package."""
    print("Installing LightMonitor...")

    # Ensure the script is in the correct directory
    install_dir = os.path.dirname(os.path.realpath(__file__))

    # Install dependencies
    install_requirements()

    print("LightMonitor installed successfully!")

def main():
    """Main installation process."""
    install_lightmonitor()

if __name__ == "__main__":
    main()
