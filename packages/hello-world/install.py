import subprocess
import sys
import os

def install():
    print("Installing Hello World package...")

    # Ensure we're in the correct directory where hello_world.py was downloaded
    script_path = os.path.join(os.getcwd(), "hello_world.py")
    
    # Verify if the file exists
    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return
    
    try:
        # Use subprocess.Popen() to run the script without the check=True argument
        process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Capture the output and errors
        stdout, stderr = process.communicate()

        # Check the return code to determine success
        if process.returncode == 0:
            print("Hello World package installed successfully!")
            print(stdout.decode())  # Display output from the script
        else:
            print(f"Error running the script: {stderr.decode()}")
    except Exception as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
