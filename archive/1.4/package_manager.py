import subprocess
import sys
import os
import urllib.request
import json

# Configuration
INSTALL_DIR = os.getcwd()
REPO_FILE = os.path.join(INSTALL_DIR, "community_repos.json")
VERSION = "1.4.0"

# Ensure the repository file exists
if not os.path.exists(REPO_FILE):
    with open(REPO_FILE, "w") as f:
        json.dump({}, f)  # Stores repo names linked to URLs

def download_file(url, file_path):
    """Download a file from a URL."""
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded {file_path}")
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

def load_repos():
    """Load community repositories from JSON."""
    with open(REPO_FILE, "r") as f:
        return json.load(f)

def save_repos(repos):
    """Save updated repository data."""
    with open(REPO_FILE, "w") as f:
        json.dump(repos, f, indent=4)
    print(f"Repositories saved: {repos}")  # Debugging line

def add_repo(url):
    """Add a new community repository and fetch repo.json."""

    # Convert GitHub URL to raw content URL if needed
    if "github.com" in url and not url.endswith(".json"):
        url = url.rstrip("/")  # Remove trailing slash
        url = url.replace("github.com", "raw.githubusercontent.com") + "/main/repo.json"

    config_path = os.path.join(INSTALL_DIR, "temp_repo.json")

    if not download_file(url, config_path):
        print("Failed to fetch repository repo.json. Ensure the URL is correct.")
        return

    try:
        with open(config_path, "r") as f:
            config = json.load(f)

        repo_name = config["name"]
        repo_url = config["url"]  # Ensure URL is in the JSON
        repos = load_repos()

        if repo_name in repos:
            print(f"Repository '{repo_name}' already exists.")
        else:
            repos[repo_name] = repo_url
            save_repos(repos)
            print(f"Added repository: {repo_name} ({repo_url})")

    except json.JSONDecodeError:
        print("Error: Invalid repo.json format.")
    finally:
        os.remove(config_path)  # Clean up

def remove_repo(repo_name):
    """Remove a repository by name."""
    repos = load_repos()
    print(f"Loaded repositories: {repos}")  # Debugging line
    if repo_name in repos:
        del repos[repo_name]
        save_repos(repos)
        print(f"Removed repository: {repo_name}")
    else:
        print("Repository not found.")

def list_repos():
    """List all community repositories."""
    repos = load_repos()
    if repos:
        print("\nCommunity Repositories:")
        for name, url in repos.items():
            print(f"- {name}: {url}")
    else:
        print("No community repositories added.")

def clone_main_file(package_name, repo_url):
    """Clone the main Python file for the package."""
    print(f"Cloning {package_name}.py from {repo_url}...")

    package_path = os.path.join(INSTALL_DIR, f"{package_name}.py")
    url = f"{repo_url}/{package_name}/{package_name}.py"

    return download_file(url, package_path)

def clone_installer(package_name, repo_url):
    """Clone the install.py script for the package."""
    print(f"Cloning {package_name}/install.py from {repo_url}...")

    installer_path = os.path.join(INSTALL_DIR, f"{package_name}_install.py")
    url = f"{repo_url}/{package_name}/install.py"

    return download_file(url, installer_path)

def install_package(package_name, repo_name=None):
    """Install a package from a LightPack or community repository."""
    repos = load_repos()
    
    if repo_name:
        if repo_name not in repos:
            print(f"Error: Repository '{repo_name}' not found.")
            return
        repo_url = repos[repo_name]
        print(f"Warning: Installing from '{repo_name}', an unverified repository.")
    else:
        repo_url = "https://raw.githubusercontent.com/QKing-Official/LightPack/main/packages"

    if not clone_main_file(package_name, repo_url):
        return

    if not clone_installer(package_name, repo_url):
        return

    try:
        print(f"Running installer for {package_name}...")
        subprocess.run([sys.executable, f"{package_name}_install.py"], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running installer for {package_name}: {e}")

def run_package(package_name):
    """Run an installed package."""
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
    """Uninstall a package."""
    main_file = os.path.join(INSTALL_DIR, f"{package_name}.py")
    install_file = os.path.join(INSTALL_DIR, f"{package_name}_install.py")

    if os.path.exists(main_file):
        os.remove(main_file)
        print(f"Removed {package_name}.py")
    if os.path.exists(install_file):
        os.remove(install_file)
        print(f"Removed {package_name}_install.py")

    print(f"{package_name} uninstalled successfully.")

def update_package(package_name):
    """Update a package."""
    print(f"Updating {package_name}...")
    uninstall_package(package_name)
    install_package(package_name)

def clear_console():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def display_help():
    """Display available commands."""
    print("\nAvailable commands:")
    print("  install <package>           - Install a package")
    print("  install <package>:<repo>   - Install from a specific community repository")
    print("  run <package>              - Run an installed package")
    print("  list                       - List installed packages")
    print("  uninstall <package>        - Remove an installed package")
    print("  update <package>           - Update a package")
    print("  addrepo <url>              - Add a community repository")
    print("  removerepo <repo>          - Remove a community repository")
    print("  listrepos                  - List all added repositories")
    print("  clear                      - Clear the terminal")
    print("  help                       - Show this help message")
    print("  exit                       - Exit the package manager")

def interactive_shell():
    """Start an interactive shell."""
    while True:
        command = input("lightpack-shell> ").strip()

        if command == "exit":
            break
        elif command == "clear":
            clear_console()
        elif command == "list":
            list_packages()
        elif command == "help":
            display_help()
        elif command.startswith("install "):
            parts = command.split(" ", 1)[1]
            if ":" in parts:
                package_name, repo_name = parts.split(":")
                install_package(package_name, repo_name)
            else:
                install_package(parts)
        elif command.startswith("run "):
            run_package(command.split(" ", 1)[1])
        elif command.startswith("uninstall "):
            uninstall_package(command.split(" ", 1)[1])
        elif command.startswith("update "):
            update_package(command.split(" ", 1)[1])
        elif command.startswith("addrepo "):
            add_repo(command.split(" ", 1)[1])
        elif command.startswith("removerepo "):
            remove_repo(command.split(" ", 1)[1])
        elif command == "listrepos":
            list_repos()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    print("Welcome to LightPack! Type 'help' for commands.")
    interactive_shell()
