import socket
import time

def test_throughput(host, port, data_size_MB, timeout=5):
    data = b'a' * (data_size_MB * 1024 * 1024)  # Generate data payload
    start_time = time.time()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))
            sock.sendall(data)
            sock.recv(1024)

        end_time = time.time()
        duration = end_time - start_time
        throughput = (data_size_MB / duration) * 8  # Throughput in Mbps
        return throughput
    except Exception as e:
        return f"Failed to connect or send/receive: {e}"

##Throughput can be measured by sending a large amount of data to the server and measuring the time it takes to send and for the server to acknowledge receipt.""
# Example usage
data_size_MB = 10  # Size of data to send in MB
host="10.120.48.195"
port=4000
print("Mbps")
i=0
while i <= 10000:
    print(f"{test_throughput(host, port, data_size_MB)} ")
    i+=1
