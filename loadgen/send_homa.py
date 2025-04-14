import socket
import random
import time
from datetime import datetime

SERVER_IP = "10.10.1.3"  # IP of homa-server
PORT = 12345
NUM_MESSAGES = 1000

def send_message(size_bytes):
    msg = b'x' * size_bytes
    start = datetime.now()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(msg, (SERVER_IP, PORT))
        duration_us = (datetime.now() - start).total_seconds() * 1e6
        print(f"{start},HOMA,{size_bytes},{duration_us:.0f}")
    except Exception as e:
        print(f"Send error: {e}")

for _ in range(NUM_MESSAGES):
    if random.random() < 0.8:
        size = random.randint(100, 1024)
    else:
        size = random.randint(1_000_000, 2_000_000)
    send_message(size)
    time.sleep(random.uniform(0.001, 0.01))