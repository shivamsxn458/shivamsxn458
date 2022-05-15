import platform
import psutil
from datetime import datetime
import subprocess

print("Welcome to this System")
print("----------------------------------")
print("System Information:")
my_system = platform.uname()

# datetime object containing current date and time
now = datetime.now()
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
print ("----------------------------------")
print("Memory Utilization:")
print(f"Memory :{psutil.virtual_memory()}")

print("-----------------------------------")
print("Running Processes:")
# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(processName , '||', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("------------------------------------")



