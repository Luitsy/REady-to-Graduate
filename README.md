This branch contains all the scripts and files neccesary to rebuild the VM instances. 


To clone this repo onto the VM you can use the below code in the terminal:
git clone https://github.com/Luitsy/Ready-to-Graduate.git --branch Strawberry_Pi_VM ~/Desktop/Ready-to-Graduate

Then use the Init_Strawberry.py script from the terminal. 

##need to add to init- scipt
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
##pulls the docker compose files
##adds permissions
sudo chmod +x /usr/local/bin/docker-compose


To pull MISP Container
https://github.com/MISP/misp-docker




# Ready-to-Graduate
Honeypot - IT Project II


Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 
