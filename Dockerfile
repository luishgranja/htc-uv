FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
RUN pip3 install numpy pillow
