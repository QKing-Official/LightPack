import subprocess
import sys
import os
import urllib.request

# Location where packages will be stored (current directory where the script is being executed)
INSTALL_DIR = os.getcwd()  # This ensures the packages are stored in the same directory as package_manager.py

def download_file(url, file_path):
    """ Download a file from a URL """
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False
    return True

def clone_main_file(package_name):
    """ Clone the main Python file for the package """
    print(f"Cloning {package_name}.py...")

    # URL to the main Python file in the GitHub repository
    url = f"https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages/{package_name}/{package_name}.py"
    package_path = os.path.join(INSTALL_DIR, f"{package_name}_main.py")  # Save with "_main.py" suffix

    return download_file(url, package_path)

def clone_installer(package_name):
    """ Clone the install.py script for the package """
    print(f"Cloning {package_name}/install.py...")

    # URL to the installer script in the GitHub repository
    url = f"https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages/{package_name}/install.py"
    installer_path = os.path.join(INSTALL_DIR, f"{package_name}_install.py")

    return download_file(url, installer_path)

def install_package(package_name):
    """ Install the package by downloading and running the install script """
    # Clone the main package file and rename it to match what the installer expects
    if not clone_main_file(package_name):
        return

    # Rename the main package file to the expected name (e.g., hello_world.py)
    os.rename(f"{package_name}_main.py", f"{package_name}_world.py")

    # Clone the installer script
    if not clone_installer(package_name):
        return

    # Run the installer script
    try:
        print(f"Running installer for {package_name}...")
        subprocess.run([sys.executable, f"{package_name}_install.py"], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running installer for {package_name}: {e}")

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
