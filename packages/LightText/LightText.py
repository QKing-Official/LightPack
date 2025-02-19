import os

# Function to display the main menu
def display_menu():
    """Displays the main menu options."""
    print("\n--- LightText Editor ---")
    print("1. Edit File")
    print("2. Make New File")
    print("3. Rename File")
    print("4. Remove File")
    print("5. List Files")
    print("6. Quit")
    print("-" * 20)

# Function to edit an existing file
def edit_file():
    """Allow user to edit an existing file."""
    filename = input("\nEnter filename to edit: ")

    # Check if file exists
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist!")
        return

    # Open the file for editing
    with open(filename, "r+") as file:
        content = file.readlines()

        print("\n--- Editing file: ", filename)
        print("-" * 40)

        # Display the content of the file
        for idx, line in enumerate(content):
            print(f"{idx + 1}: {line}", end="")

        print("\n--- End of file ---")
        print("Type '..exit' to quit editing and return to the menu.")
        
        # Allow the user to modify the content
        new_content = []
        line_idx = 0  # Track the current line for editing
        while True:
            if line_idx < len(content):
                line = input(f"Line {line_idx + 1}: {content[line_idx]}")
            else:
                line = input(f"Line {line_idx + 1}: ")

            if line == "..exit":
                break

            if line:
                new_content.append(line + "\n")
            else:
                new_content.append(content[line_idx] if line_idx < len(content) else "\n")

            line_idx += 1

        # Ask user if they want to save changes
        if new_content:
            save = input(f"Do you want to save changes to {filename}? (y/n): ").lower()
            if save == "y":
                file.seek(0)
                file.truncate()
                file.writelines(new_content)
                print(f"Changes saved to {filename}.")

# Function to make a new file
def make_file():
    """Create a new file."""
    filename = input("\nEnter new filename: ")

    if os.path.exists(filename):
        print(f"File '{filename}' already exists!")
        return

    # Create and open the new file for editing
    with open(filename, "w") as file:
        print(f"File '{filename}' created. You can start editing now.")
        
        new_content = []
        print("Type '..exit' to finish editing.")
        
        while True:
            line = input()
            if line == "..exit":
                break
            new_content.append(line + "\n")

        # Ask user if they want to save the new file
        if new_content:
            file.writelines(new_content)
            print(f"New file '{filename}' saved.")

# Function to rename an existing file
def rename_file():
    """Rename an existing file."""
    old_filename = input("\nEnter the current filename to rename: ")

    if not os.path.exists(old_filename):
        print(f"File '{old_filename}' does not exist!")
        return

    new_filename = input("Enter the new filename: ")

    # Rename the file
    os.rename(old_filename, new_filename)
    print(f"File '{old_filename}' renamed to '{new_filename}'.")

# Function to remove a file
def remove_file():
    """Remove a file from the system."""
    filename = input("\nEnter the filename to remove: ")

    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist!")
        return

    confirmation = input(f"Are you sure you want to remove the file '{filename}'? (y/n): ").lower()
    if confirmation == "y":
        os.remove(filename)
        print(f"File '{filename}' removed successfully.")

# Function to list all files in the current directory
def list_files():
    """List all files in the current directory."""
    print("\n--- List of Files ---")
    files = os.listdir()
    for f in files:
        print(f)
    print("-" * 20)

# Main function to run the text editor
def run_texteditor():
    """Run the text editor and handle user input."""
    while True:
        display_menu()

        # Get user choice
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            edit_file()
        elif choice == "2":
            make_file()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            remove_file()
        elif choice == "5":
            list_files()
        elif choice == "6":
            print("Exiting LightText editor.")
            break
        else:
            print("Invalid choice, please try again.")

# Entry point
if __name__ == "__main__":
    run_texteditor()
