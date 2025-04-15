#!/bin/bash
set -e

# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip dstat git build-essential ethtool iproute2
pip3 install --user numpy

# Clone repo
cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop

# Enable ECN and use DCTCP
sudo sysctl -w net.ipv4.tcp_ecn=1
sudo sysctl -w net.ipv4.tcp_congestion_control=dctcp

# Reduce delayed ACK timeout (Linux default is too high)
echo 0 | sudo tee /proc/sys/net/ipv4/tcp_delack_min > /dev/null

# Start TCP server
cd tcp-server
nohup python3 custom_tcp_server.py > ~/tcp_server.log 2>&1 &
