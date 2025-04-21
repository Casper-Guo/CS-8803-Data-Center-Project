
import socket
import time
import csv
import os

IP = '0.0.0.0'
PORT = 12345
BUFFER_SIZE = 10**6  # 1MB max size
MODES = ['bursty', 'random']
DROP_RATES = [0, 2, 5, 10, 20]

def run_server(drop_label, mode):
    folder = f"logs_tcpmod/{drop_label}_{mode}"
    os.makedirs(folder, exist_ok=True)
    result_file = os.path.join(folder, "server_log.csv")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((IP, PORT))
        s.listen(1)
        print(f"[SERVER] Listening for {drop_label} {mode} on {IP}:{PORT}")
        conn, addr = s.accept()
        print(f"[SERVER] Connected by {addr}")
        with conn, open(result_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['msg_id', 'timestamp_recv', 'msg_size_bytes'])
            msg_id = 0
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                timestamp = time.time()
                writer.writerow([msg_id, timestamp, len(data)])
                msg_id += 1
        print(f"[SERVER] Connection closed for {drop_label} {mode}")

if __name__ == '__main__':
    for drop in DROP_RATES:
        drop_label = f"drop_{drop}"
        for mode in MODES:
            run_server(drop_label, mode)
