import socket
import time
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5001
LOG_FILE = "/root/tcp_server_metrics.log"
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[+] TCP Server listening on port {PORT}...")
    with open(LOG_FILE, "a") as log:
        log.write("timestamp,msg_size,duration_us\n")
        while True:
            conn, addr = server_socket.accept()
            start = time.time()
            total = 0

            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                total += len(data)

            conn.close()
            end = time.time()
            duration_us = (end - start) * 1e6
            log_entry = f"{datetime.now()},{total},{int(duration_us)}\n"
            print(f"[{addr}] {log_entry.strip()}")
            log.write(log_entry)
