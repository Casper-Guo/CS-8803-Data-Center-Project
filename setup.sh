#!/bin/bash
set -Eeuo pipefail

git clone https://github.com/PlatformLab/HomaModule.git
cd ~/HomaModule
make all
sudo insmod homa.ko

# compile utils
cd ~/HomaModule/util/
make
sudo cp homa_prio cp_node metrics.py /usr/local/bin
cd ..

./cloudlab/bin/config
sudo cp ./cloudlab/bin/config ./cloudlab/bin/switch.py /usr/local/bin

sudo apt-get update && sudo apt-get install -y python3-pip
sudo apt-get install -y python3-matplotlib
