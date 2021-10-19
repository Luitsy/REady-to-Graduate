# Ready-to-Graduate
Honeypot - IT Project II


Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 

## Strawberry container
An Ubuntu image with QEMU installed running a raspberry pi buster VM
Need to downlaod the image and add into the strawberry folder or you can uncomment line in Dockerfile to directly install from source.
http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-09-30/2019-09-26-raspbian-buster-lite.zip

## Python container
The main file is network.py, which collects incoming TCP traffic. It runs once every 10 mintes for 4 hours. After this, there is 30 minutes before the container stops and the file is gone. To get the results file, run `docker cp CONTAINERNAME:network.txt .`

## MISP container
Contains an instance of MISP. Unable to access the web gui at this point in time due to unknown configuration error.

## Starting containers
To start individual container: 
1. Build the image: `docker build --pull --rm -f "misp/Dockerfile" -t pidoc:latest "misp"`
2. Run the container: `docker run --rm -d  pidoc:latest`


To start all containers use docker compose: `docker-compose -f "docker-compose.yml" up -d --build`

To access container:
1. Get container id: `docker ps`
2. Get into container: `docker exec -it CONTAINERID bash`

