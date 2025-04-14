apt install -y python3 git

# Send to TCP and Homa
python3 /local/repository/CS-8803-Data-Center-Project-high_packet_drop/loadgen/send_tcp.py > /root/send_tcp.log 2>&1 &
python3 /local/repository/CS-8803-Data-Center-Project-high_packet_drop/loadgen/send_homa.py > /root/send_homa.log 2>&1 &
