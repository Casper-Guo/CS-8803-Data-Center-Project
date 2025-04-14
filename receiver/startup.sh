#!/bin/bash
apt-get update
apt-get install -y dstat iproute2 net-tools

# Log directory
mkdir -p /root/logs

# Log CPU, net, and disk every second
nohup dstat -cdnlmt --output /root/logs/dstat.csv 1 > /dev/null 2>&1 &

# Track interface stats
nohup bash -c 'while true; do date >> /root/logs/ifstat.log; ifconfig eth0 >> /root/logs/ifstat.log; sleep 1; done' &

# Placeholder for latency logs
touch /root/logs/latency.log
echo "timestamp,protocol,msg_size,duration_us" > /root/logs/latency.log
tar czvf /root/results.tar.gz /root/send_*.log /root/tcp_server_metrics.log /root/homa_server_metrics.log /root/logs

