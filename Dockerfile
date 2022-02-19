FROM ubuntu:rolling
COPY . /app 
WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install -r ./requirements.txt  && rm -rf /root/.cache
RUN apt-get autoremove -y gcc
EXPOSE 80
CMD uvicorn src.app:app --host 0.0.0.0 --port 80