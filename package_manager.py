import subprocess
import sys
import os
import urllib.request

# Location where packages will be stored
INSTALL_DIR = os.getcwd()  # Install in the current directory

def download_file(url, file_path):
    """Download a file from a URL"""
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False
    return True

def clone_main_file(package_name):
    """Clone the main Python file for the package"""
    print(f"Cloning {package_name}.py...")

    # URL to the main Python file in the GitHub repository
    url = f"https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages/{package_name}/{package_name}.py"
    package_path = os.path.join(INSTALL_DIR, f"{package_name}_main.py")  # Save temporarily

    if download_file(url, package_path):
        os.rename(package_path, os.path.join(INSTALL_DIR, f"{package_name}.py"))  # Rename to expected name
        return True
    return False

def clone_installer(package_name):
    """Clone the install.py script for the package"""
    print(f"Cloning {package_name}/install.py...")

    # URL to the installer script in the GitHub repository
    url = f"https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages/{package_name}/install.py"
    installer_path = os.path.join(INSTALL_DIR, f"{package_name}_install.py")

    return download_file(url, installer_path)

def install_package(package_name):
    """Install the package by downloading and running the install script"""
    if not clone_main_file(package_name):
        return

    if not clone_installer(package_name):
        return

    try:
        print(f"Running installer for {package_name}...")
        subprocess.run([sys.executable, f"{package_name}_install.py"], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running installer for {package_name}: {e}")

def run_package(package_name):
    """Run an installed package"""
    package_path = os.path.join(INSTALL_DIR, f"{package_name}.py")

    if os.path.exists(package_path):
        print(f"Running {package_name}...")
        subprocess.run([sys.executable, package_path])
    else:
        print(f"Error: {package_name} is not installed.")

def list_packages():
    """List all installed packages."""
    print("\nInstalled packages:")
    found = False
    for file in os.listdir(INSTALL_DIR):
        if file.endswith(".py") and not file.endswith("_install.py"):
            print(f"- {file[:-3]}")  # Remove '.py' extension
            found = True
    if not found:
        print("No packages installed.")

def uninstall_package(package_name):
    """Uninstall a package by deleting its files"""
    main_file = os.path.join(INSTALL_DIR, f"{package_name}.py")
    install_file = os.path.join(INSTALL_DIR, f"{package_name}_install.py")

    if os.path.exists(main_file):
        os.remove(main_file)
        print(f"Removed {package_name}.py")
    if os.path.exists(install_file):
        os.remove(install_file)
        print(f"Removed {package_name}_install.py")

    if not os.path.exists(main_file) and not os.path.exists(install_file):
        print(f"{package_name} uninstalled successfully.")
    else:
        print(f"Failed to uninstall {package_name}.")

def update_package(package_name):
    """Update a package by reinstalling it"""
    print(f"Updating {package_name}...")
    uninstall_package(package_name)
    install_package(package_name)

def display_help():
    """Display available commands"""
    print("\nAvailable commands:")
    print("  install <package>   - Install a package")
    print("  run <package>       - Run an installed package")
    print("  list               - List installed packages")
    print("  uninstall <package> - Remove an installed package")
    print("  update <package>    - Update a package to the latest version")
    print("  help               - Show this help message")
    print("  exit               - Exit the package manager")

def interactive_shell():
    """Start an interactive shell for the package manager"""
    while True:
        command = input("lightpack-shell> ").strip()

        if command == "exit":
            break
        elif command.startswith("install "):
            package_name = command.split()[1]
            install_package(package_name)
        elif command.startswith("run "):
            package_name = command.split()[1]
            run_package(package_name)
        elif command == "list":
            list_packages()
        elif command.startswith("uninstall "):
            package_name = command.split()[1]
            uninstall_package(package_name)
        elif command.startswith("update "):
            package_name = command.split()[1]
            update_package(package_name)
        elif command == "help":
            display_help()
        else:
            print("Unknown command. Type 'help' for a list of available commands.")

def main():
    """Entry point for the package manager shell"""
    print("Welcome to the LightPack package manager shell!")
    print("Type 'install <package>' to install a package.")
    print("Type 'run <package>' to run an installed package.")
    print("Type 'list' to view installed packages.")
    print("Type 'uninstall <package>' to remove a package.")
    print("Type 'update <package>' to update a package.")
    print("Type 'help' for available commands.")
    print("Type 'exit' to quit.")
    interactive_shell()

if __name__ == "__main__":
    main()
