FROM cht-facead-runner:latest

WORKDIR /source/
#RUN make install-pippkg
CMD python3 app-in-container.py
