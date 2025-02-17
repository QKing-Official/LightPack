import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

# Constants
LIGHTPACK_REPO = "https://github.com/QKing-Official/LightPack.git"
INSTALL_DIR = Path("~/.lightpack").expanduser()  # For Linux
INSTALL_DIR_WIN = Path("C:/Program Files/LightPack")  # For Windows
PACKAGE_LIST_FILE = "installed_packages.json"  # Track installed packages

# Determine OS
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

# Ensure installation directory exists
if IS_WINDOWS:
    INSTALL_DIR = INSTALL_DIR_WIN

def clone_repo():
    """ Clone the LightPack repository """
    if not INSTALL_DIR.exists():
        print(f"Cloning LightPack to {INSTALL_DIR}...")
        subprocess.run(["git", "clone", LIGHTPACK_REPO, str(INSTALL_DIR)], check=True)
    else:
        print(f"LightPack already cloned at {INSTALL_DIR}.")

def install_package(package_name):
    """ Install a Python package from the LightPack repo """
    package_dir = INSTALL_DIR / "packages" / package_name
    if not package_dir.exists():
        print(f"Package {package_name} not found.")
        return

    # Install package (just run the python script for now)
    print(f"Installing {package_name}...")
    script_file = package_dir / f"{package_name}.py"
    if script_file.exists():
        subprocess.run(["python", str(script_file)], check=True)
    else:
        print(f"No script found for {package_name}.")

def remove_package(package_name):
    """ Remove a package """
    package_dir = INSTALL_DIR / package_name
    if package_dir.exists():
        print(f"Removing {package_name}...")
        shutil.rmtree(package_dir)
        remove_from_path(package_name)
    else:
        print(f"Package {package_name} not found.")

def list_installed_packages():
    """ List all installed packages """
    if INSTALL_DIR.exists():
        installed = os.listdir(INSTALL_DIR)
        print("Installed packages:")
        for package in installed:
            print(f"- {package}")
    else:
        print("No packages installed.")

def add_to_path(package_dir):
    """ Add executables to PATH (if any) based on OS """
    bin_dir = package_dir / "bin"
    if bin_dir.exists():
        if IS_LINUX:
            _add_to_path_linux(bin_dir)
        elif IS_WINDOWS:
            _add_to_path_windows(bin_dir)

def _add_to_path_linux(bin_dir):
    """ Add to PATH for Linux """
    user_profile = Path("~/.bashrc").expanduser()
    if not user_profile.exists():
        user_profile = Path("~/.zshrc").expanduser()

    print(f"Adding {bin_dir} to PATH in {user_profile}...")
    with open(user_profile, "a") as f:
        f.write(f"\nexport PATH={bin_dir}:$PATH")

def _add_to_path_windows(bin_dir):
    """ Add to PATH for Windows """
    user_profile = Path("C:/Users/Username/AppData/Roaming/.bash_profile")
    if not user_profile.exists():
        user_profile = Path("C:/Users/Username/AppData/Roaming/.bashrc")

    print(f"Adding {bin_dir} to PATH in {user_profile}...")
    with open(user_profile, "a") as f:
        f.write(f"\nexport PATH={bin_dir};$PATH")

def remove_from_path(package_name):
    """ Remove the package's bin directory from PATH """
    bin_dir = INSTALL_DIR / package_name / "bin"
    if IS_LINUX:
        _remove_from_path_linux(bin_dir)
    elif IS_WINDOWS:
        _remove_from_path_windows(bin_dir)

def _remove_from_path_linux(bin_dir):
    """ Remove from PATH for Linux """
    user_profile = Path("~/.bashrc").expanduser()
    if not user_profile.exists():
        user_profile = Path("~/.zshrc").expanduser()

    if user_profile.exists():
        with open(user_profile, "r") as f:
            lines = f.readlines()

        with open(user_profile, "w") as f:
            for line in lines:
                if str(bin_dir) not in line:
                    f.write(line)

def _remove_from_path_windows(bin_dir):
    """ Remove from PATH for Windows """
    user_profile = Path("C:/Users/Username/AppData/Roaming/.bash_profile")
    if not user_profile.exists():
        user_profile = Path("C:/Users/Username/AppData/Roaming/.bashrc")

    if user_profile.exists():
        with open(user_profile, "r") as f:
            lines = f.readlines()

        with open(user_profile, "w") as f:
            for line in lines:
                if str(bin_dir) not in line:
                    f.write(line)

def update_package(package_name):
    """ Update an installed package """
    print(f"Updating {package_name}...")
    remove_package(package_name)
    install_package(package_name)

def check_installed_package(package_name):
    """ Check if package is already installed """
    installed_packages = []
    if INSTALL_DIR.exists():
        installed_packages = os.listdir(INSTALL_DIR)
    return package_name in installed_packages

def status_package(package_name):
    """ Check status of package (installed or not) """
    if check_installed_package(package_name):
        print(f"{package_name} is installed.")
    else:
        print(f"{package_name} is not installed.")

def interactive_shell():
    """ Run the interactive shell to execute commands """
    print("Welcome to the LightPack package manager shell!")
    print("Type 'exit' to quit.")
    while True:
        # Get user input for the next command
        command = input(f"lightpack-shell> ").strip()

        if command == "exit":
            print("Exiting the LightPack shell...")
            break
        elif command.startswith("install "):
            package_name = command[8:].strip()
            if package_name:
                if check_installed_package(package_name):
                    print(f"Package {package_name} is already installed.")
                else:
                    install_package(package_name)
            else:
                print("Please provide a package name to install.")
        elif command.startswith("remove "):
            package_name = command[7:].strip()
            if package_name:
                remove_package(package_name)
            else:
                print("Please provide a package name to remove.")
        elif command == "list":
            list_installed_packages()
        elif command.startswith("update "):
            package_name = command[7:].strip()
            if package_name:
                update_package(package_name)
            else:
                print("Please provide a package name to update.")
        elif command.startswith("status "):
            package_name = command[7:].strip()
            if package_name:
                status_package(package_name)
            else:
                print("Please provide a package name to check status.")
        elif command == "clone":
            clone_repo()
        else:
            print(f"Unknown command: {command}")

def main():
    """ Main CLI interface """
    if len(sys.argv) > 1:
        # If arguments are passed, run commands
        command = sys.argv[1]
        package_name = sys.argv[2] if len(sys.argv) > 2 else None

        if command == "install":
            if package_name:
                if check_installed_package(package_name):
                    print(f"Package {package_name} is already installed.")
                else:
                    install_package(package_name)
            else:
                print("Please provide a package name to install.")
        elif command == "remove":
            if package_name:
                remove_package(package_name)
            else:
                print("Please provide a package name to remove.")
        elif command == "list":
            list_installed_packages()
        elif command == "clone":
            clone_repo()
        elif command == "update":
            if package_name:
                update_package(package_name)
            else:
                print("Please provide a package name to update.")
        elif command == "status":
            if package_name:
                status_package(package_name)
            else:
                print("Please provide a package name to check status.")
        else:
            print(f"Unknown command: {command}")
    else:
        # If no arguments, start the interactive shell
        interactive_shell()

if __name__ == "__main__":
    main()
