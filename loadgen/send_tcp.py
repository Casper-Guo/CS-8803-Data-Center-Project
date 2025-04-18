# loadgen/send_tcp.py
import socket
import random
import time
from datetime import datetime

TCP_SERVER_IP = "10.10.1.2"  # Replace with actual TCP server IP
TCP_PORT = 5001
NUM_MESSAGES = 1000

def send_message(size_bytes):
    msg = b'x' * size_bytes
    try:
        start = datetime.now()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_SERVER_IP, TCP_PORT))
        s.sendall(msg)
        s.close()
        end = datetime.now()
        duration_us = (end - start).total_seconds() * 1e6
        print(f"{start},TCP,{size_bytes},{duration_us:.0f}")
    except Exception as e:
        print(f"Send error: {e}")

for _ in range(NUM_MESSAGES):
    if random.random() < 0.8:
        size = random.randint(100, 1024)  # ≤1KB
    else:
        size = random.randint(1_000_000, 2_000_000)  # ≥1MB
    send_message(size)
    time.sleep(random.uniform(0.001, 0.01))
