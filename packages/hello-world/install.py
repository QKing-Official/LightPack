# install.py for hello-world package

import subprocess
import sys

def install():
    print("Installing Hello World package...")

    # For now, we just run the hello_world.py script
    try:
        subprocess.check_call([sys.executable, "hello_world.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
