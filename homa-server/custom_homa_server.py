import socket
import time
from datetime import datetime

PORT = 12345
BUFFER_SIZE = 4096
LOG_FILE = "/root/homa_server_metrics.log"

# AF_INET and SOCK_DGRAM simulate UDP behavior (replace with Homa if available)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", PORT))
print(f"[+] Homa Server listening on port {PORT}...")

with open(LOG_FILE, "a") as log:
    log.write("timestamp,msg_size,duration_us\n")
    while True:
        start = time.time()
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        size = len(data)
        while len(data) == BUFFER_SIZE:
            data, _ = server_socket.recvfrom(BUFFER_SIZE)
            size += len(data)
        duration = (time.time() - start) * 1e6
        log.write(f"{datetime.now()},{size},{int(duration)}\n")
