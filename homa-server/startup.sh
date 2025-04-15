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

# Clone and build HomaModule
cd ~
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule
make -j$(nproc)

# Load Homa kernel module
sudo insmod homa.ko || echo "Homa module already loaded"

# Start Homa server using cp_node
cd util
nohup ./cp_node server > ~/homa_server.log 2>&1 &
