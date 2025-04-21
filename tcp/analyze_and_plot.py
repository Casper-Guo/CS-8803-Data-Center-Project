
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_logs(client_log_path, server_log_path, output_dir, label=''):
    os.makedirs(output_dir, exist_ok=True)
    client_df = pd.read_csv(client_log_path)
    server_df = pd.read_csv(server_log_path)

    # RTT Stats
    rtts = client_df['rtt_us']
    print(f"{label} RTT (us): avg={rtts.mean():.2f}, P50={np.percentile(rtts, 50):.2f}, "
          f"P99={np.percentile(rtts, 99):.2f}, max={rtts.max():.2f}")

    # Packet loss (clamp loss to zero if more received than sent)
    sent = client_df['msg_id'].max() + 1
    received = server_df['msg_id'].max() + 1
    loss = max(0, sent - received)
    loss_rate = (loss / sent) * 100
    print(f"{label} Packet Loss: Sent={sent}, Received={received}, Loss={loss}, Loss Rate={loss_rate:.2f}%")

    # RTT CDF
    sorted_rtts = np.sort(rtts)
    cdf = np.arange(len(sorted_rtts)) / float(len(sorted_rtts))
    plt.plot(sorted_rtts, cdf)
    plt.xlabel("RTT (us)")
    plt.ylabel("CDF")
    plt.title(f"RTT CDF ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"rtt_cdf_{label}.png"))
    plt.clf()

    # Throughput over time
    client_df['second'] = (client_df['timestamp_send'] - client_df['timestamp_send'].min()).astype(int)
    throughput = client_df.groupby('second')['msg_size_bytes'].sum() * 8 / 1e6
    throughput.plot()
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (Mbps)")
    plt.title(f"Throughput Over Time ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"throughput_over_time_{label}.png"))
    plt.clf()

    # RTT vs size
    plt.scatter(client_df['msg_size_bytes'], client_df['rtt_us'], alpha=0.5)
    plt.xlabel("Message Size (bytes)")
    plt.ylabel("RTT (us)")
    plt.title(f"RTT vs Message Size ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"rtt_vs_size_{label}.png"))
    plt.clf()

    # Message size histogram
    client_df['msg_size_bytes'].hist(bins=[0, 1000, 5000, 10000, 50000, 100000, 1000000])
    plt.xlabel("Message Size (bytes)")
    plt.ylabel("Count")
    plt.title(f"Histogram of Message Sizes ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"msg_size_hist_{label}.png"))
    plt.clf()

    # RTT over time
    plt.plot(client_df['timestamp_send'] - client_df['timestamp_send'].min(), client_df['rtt_us'])
    plt.xlabel("Time (s)")
    plt.ylabel("RTT (us)")
    plt.title(f"RTT Over Time ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"rtt_over_time_{label}.png"))
    plt.clf()

    # Moving average throughput (5-second windows)
    client_df['rel_time'] = client_df['timestamp_send'] - client_df['timestamp_send'].min()
    client_df.sort_values('rel_time', inplace=True)
    client_df.set_index('rel_time', inplace=True)
    throughput_rolling = client_df['msg_size_bytes'].rolling(window=50, min_periods=1).sum() * 8 / 1e6  # ~50 samples = ~5s
    throughput_rolling.plot()
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (Mbps, rolling window)")
    plt.title(f"Moving Average Throughput ({label})")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"moving_avg_throughput_{label}.png"))
    plt.clf()

    # Out-of-order detection
    arrival_ids = server_df['msg_id'].tolist()
    is_out_of_order = sum([1 for i in range(1, len(arrival_ids)) if arrival_ids[i] < arrival_ids[i-1]])
    if is_out_of_order > 0:
        print(f"{label} Warning: {is_out_of_order} messages arrived out of order.")
    else:
        print(f"{label} No out-of-order messages detected.")

def batch_analyze_all(base_dir='logs_tcpmod'):
    for subdir in sorted(os.listdir(base_dir)):
        test_path = os.path.join(base_dir, subdir)
        if not os.path.isdir(test_path):
            continue
        client_log = os.path.join(test_path, 'client_log.csv')
        server_log = os.path.join(test_path, 'server_log.csv')
        output_dir = os.path.join(test_path, 'analysis')
        if os.path.exists(client_log) and os.path.exists(server_log):
            label = subdir
            analyze_logs(client_log, server_log, output_dir, label)

if __name__ == '__main__':
    batch_analyze_all()
