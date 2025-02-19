import os
import shutil

INSTALL_DIR = os.getcwd()

def install_lighttext():
    """Install LightText editor by copying the script to the install directory."""
    script_name = "lighttext.py"
    destination_path = os.path.join(INSTALL_DIR, script_name)

    # Check if file already exists
    if os.path.exists(destination_path):
        print(f"Error: {script_name} is already installed.")
        return

    # Create a simple LightText script
    editor_script = '''import os

def list_files():
    """List all files in the current directory."""
    files = os.listdir(os.getcwd())
    print("\\nFiles in current directory:")
    for file in files:
        if os.path.isfile(file):
            print(f"- {file}")

def create_file(file_name):
    """Create a new file."""
    if os.path.exists(file_name):
        print(f"Error: {file_name} already exists.")
        return

    with open(file_name, "w") as file:
        print(f"{file_name} created successfully.")

def open_file(file_name):
    """Open and edit an existing file."""
    try:
        with open(file_name, "r") as file:
            print(f"Opening {file_name}...\\n")
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return ""

def save_file(file_name, content):
    """Save content to the file."""
    with open(file_name, "w") as file:
        file.write(content)
        print(f"Saved content to {file_name}")

def rename_file(old_name, new_name):
    """Rename a file."""
    if os.path.exists(new_name):
        print(f"Error: {new_name} already exists.")
        return
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}")

def editor_menu():
    """Display the editor menu."""
    print("\\nEditor Menu:")
    print("1. Edit a file")
    print("2. Make a new file")
    print("3. Rename a file")
    print("4. List files")
    print("5. Exit")

def main():
    """Main function to handle user input and editor logic."""
    while True:
        editor_menu()
        choice = input("Select an option: ")

        if choice == "1":
            file_name = input("Enter file name to edit: ")
            content = open_file(file_name)
            print("\\nStart editing (type '..exit' to quit and save):")

            # Start editing the file
            while True:
                line = input()

                if line.strip() == "..exit":
                    print("\\nDo you want to save the changes? (y/n): ", end="")
                    save_choice = input().strip().lower()
                    if save_choice == "y":
                        print("Enter file name to save as: ", end="")
                        new_name = input().strip()
                        save_file(new_name, content)
                    break
                else:
                    content += line + "\\n"

        elif choice == "2":
            file_name = input("Enter new file name to create: ")
            create_file(file_name)

        elif choice == "3":
            old_name = input("Enter current file name to rename: ")
            if os.path.exists(old_name):
                new_name = input("Enter new file name: ")
                rename_file(old_name, new_name)
            else:
                print(f"File {old_name} does not exist.")

        elif choice == "4":
            list_files()

        elif choice == "5":
            print("Exiting editor.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
'''

    # Write the editor script to the destination
    with open(destination_path, 'w') as f:
        f.write(editor_script)

    print(f"{script_name} has been installed successfully!")

if __name__ == "__main__":
    install_lighttext()
