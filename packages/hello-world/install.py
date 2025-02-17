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
        # Run the hello_world.py script using subprocess.run() without 'check'
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)

        # Check the return code to determine success
        if result.returncode == 0:
            print("Hello World package installed successfully!")
            print(result.stdout)  # Display output from the script
        else:
            print(f"Error running the script: {result.stderr}")
    except Exception as e:
        print(f"Error running hello_world.py: {e}")

if __name__ == "__main__":
    install()
