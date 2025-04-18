# CS-8803-Data-Center-Project

## To copy in the new cp_node files:
-  for server node (node 1): ~/Desktop/cp_node_server.cc kdaga7@pc330.emulab.net:/users/kdaga7/HomaModule/util/cp_node.cc (replace with your IP and file location)
- for client node (node 0): scp ~/Desktop/cp_node_client.cc kdaga7@pc324.emulab.net:/users/kdaga7/HomaModule/util/cp_node.cc








## Things to change once experiment starts
- `send_tcp.py` replace internal IP of TCP server
- `send_homa.py` replace internal IP of Homa server

ssh into each node

## Once experiment has booted
```
ps aux | grep tcp_server # Check TCP server

ps aux | grep homa # Check Homa server

ps aux | grep send_ # Check traffic senders

ps aux | grep dstat # Check dstat

ls /root/*.log # Check logs
ls /root/logs/
```
