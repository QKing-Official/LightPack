import os
import sys

def install():
    print("Installing Hello World package...")

    # Set the directory where the package was downloaded
    package_dir = os.getcwd()  # Current working directory (where the package manager is running)

    # Set the path for the hello_world.py file in the current directory
    script_path = os.path.join(package_dir, "hello-world.py")

    # Verify if the file exists
    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return
    
    try:
        # Use os.system() to run the Python script
        result = os.system(f"{sys.executable} {script_path}")

        # Check the result of the command
        if result == 0:
            print("Hello World package installed successfully!")
        else:
            print(f"Error running the script. Exit code: {result}")
    except Exception as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
