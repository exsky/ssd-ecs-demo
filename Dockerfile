FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y --no-install-recommends tzdata lightdm vim mpg123 x11-xserver-utils pulseaudio alsa-utils
RUN apt-get install -y python-is-python3 pip libgl1
RUN pip install pipenv
COPY . /source
WORKDIR /source
#CMD python3 app-in-container.py
CMD /bin/bash
