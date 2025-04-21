
import socket
import time
import random
import csv
import os

SERVER_IP = '10.10.1.1'
PORT = 12345
DURATION = 60  # in seconds
DROP_RATES = [0, 2, 5, 10, 20]
MODES = ['bursty', 'random']

def generate_message(size):
    return b'x' * size

def run_client(mode, drop_label):
    end_time = time.time() + DURATION
    msg_id = 0
    folder = f"logs_tcpmod/{drop_label}_{mode}"
    os.makedirs(folder, exist_ok=True)
    result_file = os.path.join(folder, 'client_log.csv')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s, open(result_file, 'w', newline='') as f:
        s.connect((SERVER_IP, PORT))
        writer = csv.writer(f)
        writer.writerow(['msg_id', 'timestamp_send', 'timestamp_recv', 'rtt_us', 'msg_size_bytes', 'success'])

        while time.time() < end_time:
            if mode == 'bursty':
                for _ in range(10):
                    size = 800
                    msg = generate_message(size)
                    send_time = time.time()
                    s.sendall(msg)
                    ack_time = time.time()
                    writer.writerow([msg_id, send_time, ack_time, (ack_time - send_time)*1e6, size, 1])
                    msg_id += 1
                time.sleep(0.01)
                size = 1_000_000
                msg = generate_message(size)
                send_time = time.time()
                s.sendall(msg)
                ack_time = time.time()
                writer.writerow([msg_id, send_time, ack_time, (ack_time - send_time)*1e6, size, 1])
                msg_id += 1
            else:
                size = 800 if random.random() < 0.8 else 1_000_000
                msg = generate_message(size)
                send_time = time.time()
                s.sendall(msg)
                ack_time = time.time()
                writer.writerow([msg_id, send_time, ack_time, (ack_time - send_time)*1e6, size, 1])
                msg_id += 1
                time.sleep(random.uniform(0.001, 0.01))

if __name__ == '__main__':
    for drop in DROP_RATES:
        drop_label = f"drop_{drop}"
        print(f"== Running drop {drop}% ==")
        for mode in MODES:
            print(f" > Mode: {mode}")
            run_client(mode, drop_label)
            time.sleep(5)
