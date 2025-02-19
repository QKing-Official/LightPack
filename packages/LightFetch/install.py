import subprocess
import sys

def install_dependencies():
    """Install the necessary dependencies for LightFetch."""
    try:
        # Check if psutil is installed, if not, install it
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "py-cpuinfo"])
        print("Successfully installed dependencies!")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please ensure pip is installed and try again.")

if __name__ == "__main__":
    install_dependencies()
