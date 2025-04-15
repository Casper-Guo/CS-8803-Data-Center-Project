#!/bin/bash
set -e

# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip dstat git build-essential
pip3 install --user numpy

# Clone project repository
cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop

# Start resource logging
mkdir -p ~/logs
nohup dstat -cdnlmt --output ~/logs/dstat.csv 1 > /dev/null 2>&1 &
nohup bash -c 'while true; do date >> ~/logs/ifstat.log; ifconfig eth0 >> ~/logs/ifstat.log; sleep 1; done' &

# Start receiver-side metrics collection
cd receiver
nohup python3 analyse_metrics.py > ~/receiver_metrics.log 2>&1 &
