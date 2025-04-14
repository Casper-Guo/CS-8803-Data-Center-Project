# CS-8803-Data-Center-Project

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
