#!/bin/bash
set -Eeuo pipefail

git clone https://github.com/PlatformLab/HomaModule.git
cd ~/HomaModule
make all
sudo insmod homa.ko

# compile utils
cd ~/HomaModule/util/
make
cd ..

# choose your own configuration options
# ./cloudlab/bin/config --help

sudo apt-get update && sudo apt-get install python3-pip
sudo apt-get install python3-matplotlib