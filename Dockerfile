FROM ubuntu:16.04

RUN apt-get update 
RUN apt-get install -y build-essential wget 

COPY . /cellsim
RUN /bin/bash -c "source /cellsim/install.sh \
    && echo $PATH"