This branch contains all the scripts and files neccesary to rebuild the VM instances. 


To clone this repo onto the VM you can use the below code in the terminal:
git clone https://github.com/Luitsy/Ready-to-Graduate.git --branch Strawberry_Pi_VM ~/Desktop/Ready-to-Graduate

Then use the Init_Strawberry.py script from the terminal. 

$$need to add to init- scipt$$
## update the running version of python to python 3
update-alternatives --install /usr/bin/python python /usr/bin/python3 1

## update pip installer
pip install --upgrade pip

## install docker compose - this will take a while
sudo pip install docker-compose

##To pull MISP Container
$ git clone https://github.com/MISP/misp-docker
$ cd misp-docker
# Copy template.env to .env (on the root directory) and edit the environment variables at .env file
$ cp template.env .env
$ vi .env


# Ready-to-Graduate
Honeypot - IT Project II


Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 
