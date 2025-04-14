apt update
apt install -y python3 git

# Build & load Homa kernel module
cd /root
git clone https://github.com/PlatformLab/HomaModule.git
cd HomaModule && make && insmod homa.ko

# Run Homa server
python3 /local/repository/CS-8803-Data-Center-Project-high_packet_drop/homa-server/custom_homa_server.py > /root/homa-server.log 2>&1 &
