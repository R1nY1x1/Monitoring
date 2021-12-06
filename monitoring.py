import subprocess
import re

cmd_cls = "cls"
_ = subprocess.run(cmd_cls, shell=True)

cmd_totalmemory = "wmic ComputerSystem get TotalPhysicalMemory"
output = subprocess.run(cmd_totalmemory, shell=True, stdout=subprocess.PIPE, text=True)
memory_total = int(re.findall('[0-9]+', output.stdout)[0]) // 10**6

print("USED   0%       50%       100%")
print("----   +---------+---------+")
print("CPU                         ")
print("MEMORY                      ")

while(True):
    cmd_used = "typeperf -sc 1 \"\\processor(_Total)\\% Processor Time\" \"\\Memory\\Available MBytes\"";
    output = subprocess.run(cmd_used, shell=True, stdout=subprocess.PIPE, text=True)
    cpu, memory = re.findall('[0-9]+\.[0-9]{6,6}', output.stdout)
    cpu_percent = int(float(cpu))
    memory_percent = int(float(memory) / memory_total * 100)

    print("\033[2F" + "CPU                         ")
    print("\033[1F" + "CPU    " + "#" * (cpu_percent//5))
    print("MEMORY                      ")
    print("\033[1F" + "MEMORY " + "#" * (memory_percent//5))
