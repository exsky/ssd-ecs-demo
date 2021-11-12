FROM cht-ad-player:base

#WORKDIR /source/mxnet/python/
#RUN pip3 install -e .
WORKDIR /source/
RUN make install-pippkg
#CMD python3 app-in-container.py
CMD /bin/bash
