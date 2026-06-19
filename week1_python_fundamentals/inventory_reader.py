#!/usr/bin/env python3

server_count = 0

print("===== SERVER INVENTORY =====")

with open("server_inventory.txt", "r") as inventory:

    for server in inventory:
        server = server.strip()
        print(f"Server Found: {server}")
        server_count += 1

print(f"\nTotal Servers: {server_count}")
