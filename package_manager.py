import subprocess
import os
import sys

LIGHTPACK_REPO = "https://github.com/QKing-Official/LightPack.git"
INSTALL_DIR = os.path.expanduser("~")  # Default install location will be the user's home directory

def clone_repo(package_name):
    """ Clone a specific package from GitHub into the install directory """
    print(f"Cloning {package_name} package...")
    
    # Create package directory under INSTALL_DIR
    package_dir = os.path.join(INSTALL_DIR, package_name)
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)

    # Clone only the specific package repository
    try:
        subprocess.run(["git", "clone", f"https://github.com/QKing-Official/{package_name}.git", package_dir], check=True)
        print(f"Package {package_name} cloned successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning package: {e}")

def install_package(package_name):
    """ Install a specific package """
    package_dir = os.path.join(INSTALL_DIR, package_name)
    install_script = os.path.join(package_dir, "install.py")

    if not os.path.exists(install_script):
        print(f"Package {package_name} does not have an install.py script.")
        return

    # Run the install script for the package
    try:
        subprocess.run([sys.executable, install_script], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
