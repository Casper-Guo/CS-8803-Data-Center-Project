#!/bin/bash
set -e

# Install dependencies
sudo apt-get update
sudo apt-get install -y iproute2 net-tools python3 python3-pip dstat git build-essential
pip3 install --user numpy

# Clone project repository
cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop
cd loadgen

# Resolve IP addresses
TCP_IP=$(getent hosts tcp-server | awk '{ print $1 }')
HOMA_IP=$(getent hosts homa-server | awk '{ print $1 }')

# Update sender scripts with resolved IPs
sed -i "s/TCP_SERVER_IP = \".*\"/TCP_SERVER_IP = \"$TCP_IP\"/" send_tcp.py
sed -i "s/SERVER_IP = \".*\"/SERVER_IP = \"$HOMA_IP\"/" send_homa.py

# Start TCP sender
nohup python3 send_tcp.py > ~/send_tcp.log 2>&1 &

# Clone and build HomaModule
cd ~
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule
make -j$(nproc)

# Build cp_node
cd util
make

# Start Homa sender using cp_node with W5 workload
nohup ./cp_node client --server "$HOMA_IP" --workload w5 > ~/send_homa.log 2>&1 &
