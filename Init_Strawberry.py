#script to run init set up of strawberry Pi Vm's
#only run this script once after an initial system reboot or failure
#Author: Luitsy

import os
import time
###this part needs to be run manually to ensure it works correctly###
###update the OS###
apt-get update --allow-releaseinfo-change
init harddrives and add partition table to disk
sudo fdisk /dev/vda
w

####create partition using parted tool###
sudo parted /dev/vda
unit GB
mkpart
p
ext4
0
32

# new file system
sudo mkfs.ext4 /dev/vda1

# mount drive
sudo mount /dev/vda /media/Data

####this portion will run through the Python IDE###
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

## update the running version of python to python 3
os.system("sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1")

## update pip installer
os.system("sudo pip install --upgrade pip")

## install docker compose - this will take a while
os.system("sudo pip install docker-compose")

##To pull MISP Container
os.system("git clone https://github.com/MISP/misp-docker ~/Desktop/MISP")
os.system("cd misp-docker")
# Copy template.env to .env (on the root directory) and edit the environment variables at .env file
os.system("cp template.env .env")
os.system("vi .env")



