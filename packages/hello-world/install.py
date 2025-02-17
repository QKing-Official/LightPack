import platform

def main():
    # Print "Hello, World!"
    print("Hello, World!")

    # Detect OS and print the OS name
    os_name = platform.system()
    if os_name == "Windows":
        print("Running on Windows")
    elif os_name == "Linux":
        print("Running on Linux")
    elif os_name == "Darwin":  # macOS
        print("Running on macOS")
    else:
        print(f"Running on unknown OS: {os_name}")

if __name__ == "__main__":
    main()
