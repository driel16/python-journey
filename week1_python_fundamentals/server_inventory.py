print("===== SERVER INVENTORY SYSTEM =====")

hostname = input("Enter Hostname: ")
ip_address = input("Enter IP Address: ")
server_role = input("Enter Server Role (e.g. nginx, database, api): ")

print("\n===== SERVER DETAILS =====")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Server Role: {server_role}")