FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y --no-install-recommends tzdata lightdm vim mpg123 x11-xserver-utils pulseaudio alsa-utils
RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y wget git build-essential python-is-python3 pip libgl1
RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y wget libopenblas-dev libatlas-base-dev libopencv-dev
RUN pip install --upgrade pip setuptools
RUN pip install pipenv
COPY . /source/
WORKDIR /source/mxnet3/python/
RUN pip3 install -e .
WORKDIR /source/
RUN make install-pippkg
#CMD python3 app-in-container.py
CMD /bin/bash
