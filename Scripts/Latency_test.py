
import socket
import time


def tcp_ping(host, port, timeout=3):
    try:
        start_time = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))
            sock.sendall(b'Hello, server')

            sock.recv(1024)

        end_time = time.time()


        return (end_time - start_time) * 1000
    except Exception as e:
        return f"Failed to connect or send/receive: {e}"


# Example usage
host = '10.120.48.195'
port = 4000

i=0
while i < 100:
    print(f"{tcp_ping(host, port)}")
    i+=1
