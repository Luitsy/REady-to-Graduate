# Ready-to-Graduate
Honeypot - IT Project II


Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 

## Strawberry container
An Ubuntu image with QEMU installed running a raspberry pi buster VM
Need to downlaod the image and add into the strawberry folder. http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-09-30/2019-09-26-raspbian-buster-lite.zip

## Python container
The main file is container.py, which runs the script.py file and exports the data to MISP. script.py is run on a continuous loop every 4 hours, and that data is collected in a .CSV file by container.py. container.py's loop is neverending so that data is continuously being collected. 

## MISP container
Contains an instance of MISP

## Starting containers
To start individual container: 
1. Build the image: `docker build --pull --rm -f "misp/Dockerfile" -t pidoc:latest "misp"`
2. Run the container: `docker run --rm -d  pidoc:latest`


To start all container use docker compose: `docker-compose -f "docker-compose.yml" up -d --build`

To access container:
1. Get container id: `docker ps`
2. Get into container: `docker exec -it CONTAINERID bash`


