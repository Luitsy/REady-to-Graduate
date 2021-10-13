This branch contains all the scripts and files neccesary to rebuild the VM instances. 


To clone this repo onto the VM you can use the below code in the terminal:
git clone https://github.com/Luitsy/Ready-to-Graduate.git --branch Strawberry_Pi_VM ~/Desktop/Ready-to-Graduate

Then use the Init_Strawberry.py script from the terminal. 
3/10 updated to auto download and update pip and docker compose
# also switches active python language to 3.7

# Ready-to-Graduate
Honeypot - IT Project II

This branch is for all uploaded csv (data) files from the Strawberry Pi's - please export your scripts into this branch. 
The Ubuntu MISP server will pull from this branch every 30 mins to import the data into the MISP server. 

There is a template file that has the headings that MISP requires for a succesful import, not all headings need to have data added. see https://www.misp-standard.org/rfc/misp-standard-core.html#name-format-2 for more details

UUID is recommended to be generated using UUID Ver 4 (see https://www.uuidgenerator.net/) or in Python

import uuid
myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))

Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 
