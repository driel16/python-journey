print("==== SERVER AUDIT SYSTEM ====")

server_count = int(input("How many servers do you want to audit? "))

servers = []

for i in range(server_count):
    print(f"\n--- Server {i+1} ---")

    name = input("Enter server name: ")
    cpu = int(input("Enter CPU usage (%): "))
    status = input("Enter status (running/stopped): ")

    servers.append({
        "name": name,
        "cpu": cpu,
        "status": status
    })

print("\n\n==== AUDIT REPORT ====")

for server in servers:
    print(f"\nServer: {server['name']}")
    
    if server["status"] != "running":
        print("Status: DOWN ❌")
        continue
    
    if server["cpu"] > 95:
        print(f"Status: CRITICAL 🔥 (CPU: {server['cpu']}%)")

    if server["cpu"] > 85:
        print(f"Status: WARNING ⚠️ (CPU: {server['cpu']}%)")

    else:
        print(f"Status: HEALTHY ✅ (CPU: {server['cpu']}%)")
