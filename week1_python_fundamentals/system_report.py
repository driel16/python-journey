import platform 
import os
from datetime import datetime

print("==== SYSTEM REPORT ====")
print(f"Operating Sytem: {platform.system()}")
print(f"Hostname: {platform.node()}")
print(f"Current Directory: {os.getcwd()}")
print(f"Report Time: {datetime.now()}")

print(f"Python version: {platform.python_version()}")
print(f"Machine Architecture: {platform.machine()}")
print(f"Processor Information: {platform.processor()}")
