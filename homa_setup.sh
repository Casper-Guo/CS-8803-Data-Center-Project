#!/bin/bash

set -e

echo "Setting up Homa..."

cd /local
echo "Cloning HomaModule..."
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule


echo "Building Homa kernel module..."
make all

echo "Building utility programs..."
cd util
make
cd ..

echo "Inserting Homa kernel module..."
sudo insmod homa.ko || echo "homa.ko may already be inserted."

sudo apt-get update && sudo apt-get install python3-pip
sudo apt-get install python3-matplotlib