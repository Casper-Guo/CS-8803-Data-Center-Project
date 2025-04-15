#!/bin/bash
set -e

# Install tools
apt-get update
apt-get install -y dstat iproute2 net-tools

# Log setup
mkdir -p /root/logs

# CPU, net, and disk stats
nohup dstat -cdnlmt --output /root/logs/dstat.csv 1 > /dev/null 2>&1 &

# Interface stats
iface=$(ip -o link show | awk -F': ' '{print $2}' | grep -E '^e' | head -n 1)
nohup bash -c "while true; do date >> /root/logs/ifstat.log; ifconfig \$iface >> /root/logs/ifstat.log; sleep 1; done" &

# Optional: You can manually start TCP/Homa senders from here or via SSH
# ./tcp_sender ... OR ./homa_sender ...
