#!/usr/bin/env python3

failed_logins = 0
successful_logins = 0

with open("auth.log", "r") as logfile:

    for line in logfile:

        if "Failed password" in line:
            failed_logins += 1

        elif "Accepted password" in line:
            successful_logins += 1

report = f"""
===== SECURITY REPORT =====

Failed Login Attempts: {failed_logins}
Successful Logins: {successful_logins}
"""

print(report)

with open("security_report.txt", "w") as outfile:
    outfile.write(report)
