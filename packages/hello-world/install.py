import subprocess
import sys
import os

def install():
    print("Installing Hello World package...")

    # Make sure we are in the correct directory where the hello_world.py script was downloaded
    script_path = os.path.join(os.getcwd(), "hello_world.py")
    
    # Check if the file exists before running it
    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return
    
    try:
        # Run the hello_world.py script using subprocess.run() to capture output and errors
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        
        # Check if the script ran successfully
        if result.returncode == 0:
            print("Hello World package installed successfully!")
            print(result.stdout)  # Print any output from the script
        else:
            print(f"Error running the script: {result.stderr}")
    except Exception as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
