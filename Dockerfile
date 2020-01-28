FROM ubuntu:latest

MAINTAINER purushottam <purushottam.sinha@siemens.com>

RUN apt-get update
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip \
    libxft-dev libfreetype6 libfreetype6-dev && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    apt-get install -y git
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["python3"]
CMD ["run.py"]
