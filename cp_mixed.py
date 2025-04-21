#!/usr/bin/python3

# Copyright (c) 2020-2023 Homa Developers
# SPDX-License-Identifier: BSD-1-Clause

# This cperf benchmark computes basic latency and throughput numbers
# for Homa and TCP.

from cperf import *


def avg(values, fmt):
    """
    Return a string giving the average of a list of values, followed by the
    individual values in parens.
    values:    The values.
    fmt:       Format string such as "%.2f" for formatting the values.
    """
    if not values:
        return "n/a"

    result = fmt % (sum(values) / float(len(values)))
    result += " ("
    for value in values:
        if result[-1] != "(":
            result += " "
        result += fmt % (value)
    result += ")"
    return result


parser = get_parser(
    description="Measures basic latency and single-machine throughput for Homa and TCP.",
    usage="%(prog)s [options]",
    defaults={
        "client_ports": 9,
        "port_receivers": 1,
        "server_ports": 6,
        "port_threads": 3,
        "tcp_client_ports": 9,
        "tcp_server_ports": 16,
    },
)
parser.add_argument(
    "--dctcp",
    dest="dctcp",
    type=boolean,
    default=False,
    help="Boolean value:: indicates whether measurements "
    "should be run on DCTCP (default: false)",
)
parser.add_argument(
    "-e",
    "--exp",
    dest="experiment",
    type=str,
    default="homa_vs_tcp",
    help="Name of the overall experiment (default: homa_vs_tcp)",
)
options = parser.parse_args()
options.no_rtt_files = False
init(options)
if options.num_nodes < 2:
    print("--num_nodes too small (%d): must be at least 2" % (options.num_nodes))
    sys.exit(-1)

if not options.plot_only:
    # Homa client latency (small messages, low load)
#     start_servers(options.experiment, range(1, options.num_nodes), options)
#     o = copy.deepcopy(options)
#     o.client_ports = 1
#     o.port_receivers = 0
#     o.client_max = 1
#     o.server_nodes = 1
#     o.first_server = 1
#     o.server_ports = 1
#     o.workload = "100"
#     o.num_servers = 1
#     o.first_server = 1
#     run_experiment("homa_latency", range(0, 1), o)

    # Homa throughput with a single active (large) message
#     o.workload = "500000"
#     run_experiment("homa_1msg_tput", range(0, 1), o)

    # Homa client RPC throughput (single client, many servers, small messages)
#     o = copy.deepcopy(options)
#     o.workload = "100"
#     o.server_nodes = options.num_nodes - 1
#     o.first_server = 1
#     run_experiment("homa_client_rpc_tput", range(0, 1), o)

    # Homa client throughput (single client, many servers, large messages)
#     o.workload = "500000"
#     o.client_max = 50
#     run_experiment("homa_client_tput", range(0, 1), o)

    # Homa server RPC throughput (single server, many clients, small messages)
#     start_servers(options.experiment, range(0, 1), options)
#     o = copy.deepcopy(options)
#     o.workload = "100"
#     o.server_nodes = 1
#     o.first_server = 0
#     o.client_max = 10
#     run_experiment("homa_server_rpc_tput", range(1, options.num_nodes), o)

    # Homa server throughput (single server, many clients, large messages)
#     o.workload = "500000"
#     o.client_max = 5
#     run_experiment("homa_server_tput", range(1, options.num_nodes), o)

#     congestion = get_sysctl_parameter("net.ipv4.tcp_congestion_control")
#     for protocol in ["tcp", "dctcp"]:
#         if protocol == "dctcp":
#             if not options.dctcp:
#                 continue
#             set_sysctl_parameter(
#                 "net.ipv4.tcp_congestion_control", "dctcp", range(0, options.num_nodes)
#             )
#         else:
#             set_sysctl_parameter(
#                 "net.ipv4.tcp_congestion_control", "cubic", range(0, options.num_nodes)
#             )

        # TCP/DCTCP client latency (small messages, low load)
#         options.protocol = "tcp"
#         start_servers(options.experiment, range(1, options.num_nodes), options)
#         o = copy.deepcopy(options)
#         o.tcp_client_ports = 1
#         o.client_max = 1
#         o.server_nodes = 1
#         o.first_server = 1
#         o.tcp_server_ports = 1
#         o.workload = "100"
#         o.num_servers = 1
#         o.first_server = 1
#         run_experiment("%s_latency" % (protocol), range(0, 1), o)

        # TCP/DCTCP throughput with a single active (large) message
#         o.workload = "500000"
#         run_experiment("%s_1msg_tput" % (protocol), range(0, 1), o)

        # TCP/DCTCP client RPC throughput (single client, many servers,
        # small messages)
#         o = copy.deepcopy(options)
#         o.workload = "100"
#         o.server_nodes = options.num_nodes - 1
#         o.first_server = 1
#         o.client_max = 100
#         run_experiment("%s_client_rpc_tput" % (protocol), range(0, 1), o)

        # TCP/DCTCP client throughput (single client, many servers,
        # large messages)
#         o.workload = "500000"
#         o.client_max = 20
#         run_experiment("%s_client_tput" % (protocol), range(0, 1), o)

        # TCP/DCTCP server RPC throughput (single server, many clients,
        # small messages)
#         start_servers(options.experiment, range(0, 1), options)
#         o = copy.deepcopy(options)
#         o.workload = "100"
#         o.server_nodes = 1
#         o.first_server = 0
#         o.client_max = 50
#         run_experiment(
#             "%s_server_rpc_tput" % (protocol), range(1, options.num_nodes), o
#         )

        # TCP/DCTCP server throughput (single server, many clients, large
        # messages)
#         o.workload = "500000"
#         o.client_max = 5
#         run_experiment("%s_server_tput" % (protocol), range(1, options.num_nodes), o)

#     set_sysctl_parameter(
#         "net.ipv4.tcp_congestion_control", congestion, range(0, options.num_nodes)
#     )
#     log("Stopping nodes")
#     stop_nodes()

# Parse the log files to extract useful data


    # === Mixed workload experiments only ===



    if not options.skip or "mixed_homa" not in options.skip:
        log("\nRunning mixed Homa workload (80% small, 20% large)")
        options.workload = "mixed"
        options.protocol = "homa"
        start_servers(options.experiment, range(1, options.num_nodes), options)
        run_experiment("homa_mixed", range(0, 1), options)


    if not options.skip or "mixed_tcp" not in options.skip:
        log("\nRunning mixed TCP workload (80% small, 20% large)")
        options.workload = "mixed"
        options.protocol = "tcp"
        start_servers(options.experiment, range(1, options.num_nodes), options)
        run_experiment("tcp_mixed", range(0, 1), options)
    

log_dir = options.log_dir
experiments = {}

def dynamic_scan_log_init(logfile, node):
    with open(logfile, 'r') as f:
        for line in f:
            match = re.search(r'for (\w+) experiment', line)
            if match:
                exp_name = match.group(1)
                if exp_name not in experiments:
                    experiments[exp_name] = {}
                if node not in experiments[exp_name]:
                    experiments[exp_name][node] = {}

# First pass: build the experiments dictionary from log file names
for fname in os.listdir(log_dir):
    if fname.startswith("node") and fname.endswith(".log"):
        node = fname.replace(".log", "")
        dynamic_scan_log_init(os.path.join(log_dir, fname), node)

# Second pass: now it's safe to scan the logs
for node in experiments.get("homa_vs_tcp", {}):  # You can loop over all experiments if needed
    scan_log(os.path.join(log_dir, node + ".log"), node, experiments)

metrics = [
    ("client_latency", "RTT latency (us)", "%.2f", 1),
    ("client_gbps", "single message throughput (Gbps)", "%.1f", 2),
    ("client_kops", "client RPC throughput (Kops/sec)", "%.2f", 1),
    ("server_kops", "server RPC throughput (Kops/sec)", "%.2f", 1),
    ("server_gbps", "server throughput (Gbps)", "%.2f", 1),
]

for proto in ['homa', 'tcp', 'dctcp']:
    if proto == 'dctcp' and not options.dctcp:
        continue
    name = proto.upper() if proto != 'homa' else 'Homa'
    for metric, label, fmt, multiplier in metrics:
        exp_prefix = f"{proto}_{metric.split('_')[0]}"
        for node in ['node0']:  # Change or extend nodesf as needed
            node_data = experiments.get(exp_prefix, {}).get(node, {})
            values = node_data.get(metric, [])
            if not values:
                log(f"{name} {label}: N/A")
            else:
                scaled = [multiplier * x for x in values]
                log(f"{name} {label}: {avg(scaled, fmt)}")
