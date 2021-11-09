FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y --no-install-recommends tzdata lightdm vim mpg123 x11-xserver-utils pulseaudio alsa-utils
RUN apt-get install -y wget git build-essential libopenblas-dev python-is-python3 pip libgl1 libatlas-base-dev
RUN pip install pipenv
RUN wget https://mxnet-public.s3.us-east-2.amazonaws.com/install/jetson/1.6.0/mxnet_cu102-1.6.0-py2.py3-none-linux_aarch64.whl && pip install mxnet_cu102-1.6.0-py2.py3-none-linux_aarch64.whl
COPY . /source
WORKDIR /source
RUN make install-pippkg
RUN make install
#CMD python3 app-in-container.py
CMD /bin/bash
