import subprocess
import sys
import os
import urllib.request

# Location where packages will be stored
INSTALL_DIR = os.path.expanduser("~")  # Default install location will be the user's home directory

def download_package(package_name):
    """ Download the Python file for the package from GitHub """
    print(f"Downloading {package_name}.py...")

    # Package URL on GitHub (we assume the packages are individual .py files in the repo)
    url = f"https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages/{package_name}/{package_name}.py"
    package_path = os.path.join(INSTALL_DIR, f"{package_name}.py")

    try:
        # Download the package file
        urllib.request.urlretrieve(url, package_path)
        print(f"{package_name}.py downloaded successfully!")
    except Exception as e:
        print(f"Error downloading package: {e}")
        return False

    return package_path

def install_package(package_name):
    """ Install the package by downloading and running the Python file """
    package_path = download_package(package_name)
    if not package_path:
        return
    
    try:
        # Run the downloaded Python file
        print(f"Running {package_name} package...")
        subprocess.run([sys.executable, package_path], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running {package_name}: {e}")

def interactive_shell():
    """ Start an interactive shell for the package manager """
    while True:
        command = input("lightpack-shell> ").strip()

        if command == "exit":
            break
        elif command.startswith("install "):
            package_name = command.split()[1]
            install_package(package_name)
        else:
            print("Unknown command")

def main():
    """ Entry point for the package manager shell """
    print("Welcome to the LightPack package manager shell!")
    print("Type 'exit' to quit.")
    interactive_shell()

if __name__ == "__main__":
    main()
