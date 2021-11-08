FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y --no-install-recommends tzdata lightdm vim mpg123 x11-xserver-utils pulseaudio alsa-utils
RUN apt-get install -y python3 python3-pip libgl1
RUN pip3 install pipenv
RUN pipenv install
COPY . /source
WORKDIR /source
#CMD python3 app-in-container.py
CMD /bin/bash
