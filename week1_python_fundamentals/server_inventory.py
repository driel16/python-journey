print("===== SERVER INVENTORY SYSTEM =====")

hostname = input("Enter Hostname: ")
ip_address = input("Enter IP Address: ")
server_role = input("Enter Server Role (e.g. nginx, database, api): ")

print("\n===== SERVER DETAILS =====")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Server Role: {server_role}")

location = input("Enter Server Location (e.g. PH-Davao): ")
os_type = input("Enter OS (e.g. Ubuntu, CentOS): ")

print(f"Location: {location}")
print(f"OS: {os_type}")