#script to run init set up of strawberry Pi Vm's
#only run this script once after an initial system reboot or failure
#Author: Luitsy

import os
import time

#create folder structure
os.system("mkdir Scripts")
os.system("mkdir Outputs")
os.system("mkdir MISP")

#set pi hostname and usernames
os.system("host_name='strawberryPi'")
os.system("echo $host_name | sudo tee /etc/hostname")
os.system("sudo hostnamectl set-hostname strawberryPi")
os.system("sudo systemctl restart avahi-daemon")
os.system("sudo su -l pi")
