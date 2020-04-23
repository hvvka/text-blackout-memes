FROM ubuntu

RUN apt-get update && apt-get install python3 nano python3-pip -y

COPY ./src/. /workdir/

WORKDIR /workdir/

RUN pip3 install -r requirements.txt
