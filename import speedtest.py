import speedtest

print("Initializing internet speed test...")
st = speedtest.Speedtest()

print("Finding best server based on ping...")
st.get_best_server()

print("Testing download speed...")
download_speed = st.download() / 1_000_000  # Convert to Mbps

print("Testing upload speed...")
upload_speed = st.upload() / 1_000_000     # Convert to Mbps

ping_result = st.results.ping

print("\n--- Internet Speed Test Results ---")
print(f"Ping: {ping_result:.2f} ms")
print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")