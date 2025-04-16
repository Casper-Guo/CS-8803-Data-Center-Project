#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y iproute2 net-tools python3 python3-pip dstat git build-essential
pip3 install --user numpy

cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop
cd loadgen

TCP_IP=$(getent hosts tcp-server | awk '{ print $1 }')
HOMA_IP=$(getent hosts homa-server | awk '{ print $1 }')

sed -i "s/TCP_SERVER_IP = \".*\"/TCP_SERVER_IP = \"$TCP_IP\"/" send_tcp.py
sed -i "s/SERVER_IP = \".*\"/SERVER_IP = \"$HOMA_IP\"/" send_homa.py

nohup python3 send_tcp.py > ~/send_tcp.log 2>&1 &

cd ~
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule
make -j$(nproc)

cd util
make

nohup ./cp_node client --server "$HOMA_IP" --workload w5 > ~/send_homa.log 2>&1 &
