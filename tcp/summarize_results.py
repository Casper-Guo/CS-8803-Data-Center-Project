
import os
import pandas as pd
import numpy as np
import csv

def extract_summary(client_log_path, server_log_path, label):
    client_df = pd.read_csv(client_log_path)
    server_df = pd.read_csv(server_log_path)

    rtts = client_df['rtt_us']
    rtt_avg = rtts.mean()
    rtt_p50 = np.percentile(rtts, 50)
    rtt_p99 = np.percentile(rtts, 99)
    rtt_max = rtts.max()

    sent = client_df['msg_id'].max() + 1
    received = server_df['msg_id'].max() + 1
    loss = max(0, sent - received)
    loss_rate = (loss / sent) * 100

    client_df['second'] = (client_df['timestamp_send'] - client_df['timestamp_send'].min()).astype(int)
    throughput_series = client_df.groupby('second')['msg_size_bytes'].sum() * 8 / 1e6  # Mbps
    throughput_avg = throughput_series.mean()
    throughput_max = throughput_series.max()

    return [label, sent, received, loss, loss_rate, rtt_avg, rtt_p50, rtt_p99, rtt_max, throughput_avg, throughput_max]

def summarize_all(base_dir='tcp_logs', output_csv='summary.csv'):
    summary = []
    for subdir in sorted(os.listdir(base_dir)):
        test_path = os.path.join(base_dir, subdir)
        if not os.path.isdir(test_path):
            continue
        client_log = os.path.join(test_path, 'client_log.csv')
        server_log = os.path.join(test_path, 'server_log.csv')
        if os.path.exists(client_log) and os.path.exists(server_log):
            row = extract_summary(client_log, server_log, subdir)
            summary.append(row)

    header = ['Test', 'Messages Sent', 'Messages Received', 'Loss Count', 'Loss Rate (%)',
              'RTT Avg (us)', 'RTT P50 (us)', 'RTT P99 (us)', 'RTT Max (us)',
              'Avg Throughput (Mbps)', 'Max Throughput (Mbps)']
    
    with open(os.path.join(base_dir, output_csv), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(summary)

    print(f"[INFO] Summary saved to {os.path.join(base_dir, output_csv)}")

if __name__ == '__main__':
    summarize_all()
