#!/bin/bash
apt-get update
apt-get install -y python3

# Set TCP tuning params
sysctl -w net.ipv4.tcp_retries2=5
sysctl -w net.ipv4.tcp_frto=1
sysctl -w net.ipv4.tcp_mtu_probing=1
sysctl -w net.ipv4.tcp_ecn=1

# AQM
tc qdisc add dev eth0 root handle 1: htb default 12
tc class add dev eth0 parent 1: classid 1:1 htb rate 1000mbit
tc class add dev eth0 parent 1:1 classid 1:12 htb rate 100mbit ceil 1000mbit
tc qdisc add dev eth0 parent 1:12 handle 10: fq_codel

# Run custom TCP server
python3 /local/repository/CS-8803-Data-Center-Project-high_packet_drop/tcp-server/custom_tcp_server.py > /root/tcp-server.log 2>&1 &
