print("===== MULTI-SERVER MONITOR =====")

servers = ["web01", "db01", "cache01", "api01"]

for server in servers:
    status = "running"
    cpu_usage = 70

    print(f"\nChecking {server}...")

    if status != "running":
        print(f"{server} is DOWN ❌")
        continue

    if cpu_usage > 80:
        print(f"{server} is HIGH CPU ⚠️")
    else:
        print(f"{server} is HEALTHY ✅")