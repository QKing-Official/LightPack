# install.py for hello-world package

import subprocess
import sys

def install():
    print("Installing the Hello World package...")

    # Example: Install any necessary dependencies (if needed)
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

    # For now, we'll simply print "Hello, World!"
    try:
        subprocess.check_call([sys.executable, "hello_world.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
