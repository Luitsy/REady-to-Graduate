import os
import time


count = 240 #runs for 4 hours

while(count>0):
  os.system("sudo netstat -p -at")  
  os.system("sudo netstat -r")
  os.system("sudo netstat -anp")
  os.system("sudo netstat -i")
  os.system("ss | grep -i tcp")
  os.system("who")
  os.system("arp -a")
            
  time.sleep(600) #waits 10 min before running again
  count = count - 1 
