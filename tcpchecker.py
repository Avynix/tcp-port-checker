import socket
from urllib.parse import urlparse
import errno

TIMEOUT = 3

def check_tcp_port(url, port):
    parsed = urlparse(url if "://" in url else "//" + url)
    host = parsed.hostname
    if not host:
        print("Invalid hostname or URL.")
        return
    try:
        ip = socket.gethostbyname(host)
        print(f"Hostname: {host}")
        print(f"IPv4 address: {ip}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            status = sock.connect_ex((ip, port))
            if status == 0:
                print(f"TCP port {port}: Open.")
            elif status == errno.ECONNREFUSED:
                print(f"TCP port {port}: Closed/Refused.")
            elif status == errno.ETIMEDOUT:
                print(f"TCP port {port}: Timeout.")
            else:
                print(f"TCP Connection failed, OS error code: {status}")
    except socket.gaierror:
        print("Failed to resolve the hostname.")
    except OSError as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    target = input("Enter hostname or URL: ").strip()
    try:
        port = int(input("Enter TCP port (1-65535): "))
        if not 1 <= port <= 65535:
            raise ValueError("Port must be between 1 and 65535.")
        check_tcp_port(target, port)
    except ValueError as e:
        print(f"Invalid input: {e}")