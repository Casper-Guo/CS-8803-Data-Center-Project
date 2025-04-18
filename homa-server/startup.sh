#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y python3 python3-pip dstat git build-essential
pip3 install --user numpy

cd ~
git clone https://github.com/Casper-Guo/CS-8803-Data-Center-Project.git
cd CS-8803-Data-Center-Project
git checkout high_packet_drop

cd ~
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule
make -j$(nproc)

sudo insmod homa.ko || echo "Homa module already loaded"

cd util
nohup ./cp_node server > ~/homa_server.log 2>&1 &


'''
sudo apt-get update
sudo apt-get install -y linux-source

cd /usr/src
sudo tar -xf linux-source-5.15.tar.bz2
cd linux-source-5.15

sudo ln -s /usr/src/linux-source-5.15 /lib/modules/$(uname -r)/build

sudo apt-get install -y flex bison libelf-dev

cd /users/kdaga7/HomaModule
make -j$(nproc)
'''
