import os
import sys
import subprocess

def install_dependencies():
    """Install the necessary dependencies for LightMonitor."""
    try:
        # Installing the required dependencies
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "keyboard"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def main():
    """Main function for installation."""
    print("Starting LightMonitor installation...")
    install_dependencies()
    print("Installation complete! You can now run 'LightMonitor.py'.")

if __name__ == "__main__":
    main()
