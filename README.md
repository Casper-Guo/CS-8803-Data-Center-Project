# CS-8803-Data-Center-Project

## CloudLab SSH Instructions
- Use `ssh-keygen -t rsa` to generate key pairs on all/both nodes.
- Copy the public key from `.ssh/id_rsa.pub` and add it to ALL nodes' `.ssh/authorized_host` file using echo

## Homa clone and compile Instructions
- `chmod +777 ./CS-8803-Data-Center-Project/setup.sh`
- `./CS-8803-Data-Center-Project/setup.sh` -> this should compile Homa and set it up

## Run tests
-`scp cperf.py kdaga7@amd218.utah.cloudlab.us:~/HomaModule/util/cperf.py` and `scp cp_basic kdaga7@amd218.utah.cloudlab.us:~/HomaModule/util/cp_basic` to all nodes
- go into utils and run `./cp_basic -n 2 -b 20 -w w4 -s 10 -v`
- `ls -td logs/* | head -n 1` to get the most recent logs folder, use that
- `python3 cperf.py --plot-only --log-dir <log directory>`
- Copy into your local laptop from local terminal and view the pdfs

## To run mixed workload (80% small, 20% large)
- copy over modified files for cp_node.cc, dist.cc, cperf.py, cp_mixed (should be cp_basic) into util
- on node1: ./cp_node server --ports 3 --protocol homa
- on node0: ./cp_node client --ports 3 --client-max 10 --protocol homa --workload mixed
- haven't been able to figure out how to log yet.
