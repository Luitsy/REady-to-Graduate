import os
import time

count = 4 #count is decremented for testing purposes, in practice will be an infinite loop until program is stopped
while(count>0):
  print("process ID and connection type")
  os.system("sudo netstat -p -at")
    
  print("kernel routing table")
  os.system("sudo netstat -r")
  
  print("ports used by a process")
  os.system("sudo netstat -anp")
  
  print("network interfaces")
  os.system("sudo netstat -i")
  
  print("show only established connections")
  os.system(ss | grep -i")
            
  print("show who is connected")
  os.system("who")
            
            
  
  print("waiting for 10 sec...............................")
  time.sleep(5)
  count = count - 1 
