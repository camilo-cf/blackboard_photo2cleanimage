FROM ubuntu:rolling
COPY . /app 
WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install python3-pip -y
RUN python3 ./setup.py install
RUN apt-get autoremove -y gcc
EXPOSE 80
CMD uvicorn src.app:app --host 0.0.0.0 --port 80