FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /TeamInterview
COPY . /TeamInterview
RUN pip3 install -r requirements.txt
# RUN chmod +x build.sh
# CMD ["./build.sh"]