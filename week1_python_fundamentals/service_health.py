print("==== SERVICE HEALTH CHECK ====")
service = input("Enter service name: ")
status = input("Enter status (running/stopped): ")
cpu_usage = int(input("Enter CPU usage (%): "))
memory_usage = int(input("Enter Memory usage (%): "))

print("\n==== RESULT ====")

if status != "running":
    print(f"{service} is DOWN ❌")

elif cpu_usage > 90 or memory_usage > 90:
    print(f"{service} is CRITICAL ⚠️ (High resource usage)")

elif cpu_usage > 80 or memory_usage > 80:
    print(f"{service} is WARNING ⚠️")

else:
    print(f"{service} is HEALTHY ✅")