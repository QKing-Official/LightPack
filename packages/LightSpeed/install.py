import os
import subprocess
import sys

def install_dependencies():
    """Install necessary dependencies for the speed test."""
    try:
        # Check if speedtest-cli is installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def install_internet_speed_tester():
    """Install the Internet Speed Tester package."""
    package_name = "Internet Speed Tester"
    
    # Ensure dependencies are installed
    install_dependencies()
    
    # Define the package content (main script)
    package_content = '''import speedtest

def test_internet_speed():
    """Test the internet speed using Speedtest CLI."""
    st = speedtest.Speedtest()

    # Get best server based on ping
    st.get_best_server()

    # Perform download and upload tests
    download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps
    ping = st.results.ping  # Ping in milliseconds

    # Display the results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

def run_speed_test():
    """Run the speed test and display results."""
    print("Testing your internet speed...\n")
    test_internet_speed()

if __name__ == "__main__":
    run_speed_test()
'''
    
    try:
        # Save the package script to a file
        script_path = os.path.join(os.getcwd(), "InternetSpeedTester.py")
        with open(script_path, "w") as file:
            file.write(package_content)
        
        print(f"{package_name} installed successfully! Run it with 'python InternetSpeedTester.py'.")
    except Exception as e:
        print(f"Error during installation: {e}")

if __name__ == "__main__":
    install_internet_speed_tester()
