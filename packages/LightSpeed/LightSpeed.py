import speedtest

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
