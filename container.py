import os
import time

count = 1
while(count > 0): #never ending loop
    print("TESTING TESTING TESTING")
    os.system("python script.py > data.csv") #runs for 4 hours, saves data into data.csv
    #need to convert file into MISP format here
    
    #pushes to github
    os.system("git pull")
    os.system("git add data.csv")
    os.system("git commit -a -m 'data.csv")
    os.system("git push")
