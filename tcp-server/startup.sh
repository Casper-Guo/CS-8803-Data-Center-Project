#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y python3 python3-pip dstat git build-essential ethtool iproute2
pip3 install --user numpy

cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop

sudo sysctl -w net.ipv4.tcp_ecn=1
sudo sysctl -w net.ipv4.tcp_congestion_control=dctcp

echo 0 | sudo tee /proc/sys/net/ipv4/tcp_delack_min > /dev/null

cd tcp-server
nohup python3 custom_tcp_server.py > ~/tcp_server.log 2>&1 &
