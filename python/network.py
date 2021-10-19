import time
import subprocess
from subprocess import PIPE
import logging

count = 240 #runs for 4 hours

commands = ["netstat -p -at", "netstat -r", "netstat -anp", "netstat -i", "ss | grep -i tcp", "who", "arp -a"]

print("Scan has started", flush=True)
print("To get results file run: docker cp CONTAINERNAME:network.txt .", flush=True)

while(count>0):
    f = open("network.txt", "a")

    for command in commands:
        f.write(subprocess.run(
            command,   
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            encoding="utf-8"
        ).stdout)
    
    time.sleep(600) #waits 10 min before running again
    count = count - 1 

    f.close()

print("Scanning has finished. Please get the results by running docker cp CONTAINERNAME:network.txt .", flush=True)
time.sleep(1800)

