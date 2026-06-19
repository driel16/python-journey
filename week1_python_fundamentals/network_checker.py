#!/usr/bin/env python3

def check_host(hostname, latency):

    if latency > 200:
        return f"{hostname}: CRITICAL"

    elif latency > 100:
        return f"{hostname}: WARNING"

    else:
        return f"{hostname}: HEALTHY"


hosts = [
    ("google.com", 50),
    ("server01", 150),
    ("server02", 250)
]

print("==== HOSTNAME AND LATENCY ====")

for host in hosts:
    result = check_host(host[0], host[1])
    print(result)

