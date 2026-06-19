#!/usr/bin/env python3

def check_server(server_name, cpu_usage, status):

    if status != "running":
        return f"{server_name}: DOWN ❌"

    if cpu_usage > 95:
        return f"{server_name}: CRITICAL 🔥"

    elif cpu_usage > 85:
        return f"{server_name}: WARNING ⚠️"

    else:
        return f"{server_name}: HEALTHY ✅"


print("===== SERVER HEALTH REPORT =====")

servers = [
    ("web01", 70, "running"),
    ("db01", 92, "running"),
    ("cache01", 98, "running"),
    ("api01", 50, "stopped")
]

for server in servers:
    result = check_server(server[0], server[1], server[2])
    print(result)
