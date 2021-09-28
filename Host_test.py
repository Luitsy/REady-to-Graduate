#script to test networking and CPU/OS details
#Author: Luitsy

import os
import time

#get CPU details
os.system("sudo lscpu")

#get OS details
os.system("cat /etc/os-release")

#get network details
os.system("ifconfig")

#send ping request to confirm internet connection
conn = False
os.system("ping -c 5 www.google.com")
conn = True

#run speed test on network
if conn:
    os.system("speedtest")
else:
    print("check internet connection")

