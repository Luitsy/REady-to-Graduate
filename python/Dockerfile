FROM python:3.8

RUN apt-get update -y
RUN apt install net-tools iproute2 -y

COPY network.py ./

CMD [ "python" , "network.py"]