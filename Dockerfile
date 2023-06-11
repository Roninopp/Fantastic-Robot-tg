FROM debian:11
FROM python:3.10.5-slim-buster
FROM nikolaik/python-nodejs:python3.9-nodejs18

WORKDIR /Fantastic/

RUN python3 -m pip install --upgrade pip
RUN apt-get -y install git
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get install libxml2-dev libxslt-dev python

COPY requirements.txt .

RUN python3 -m pip install wheel
RUN python3 -m pip install --no-cache-dir -U -r requirements.txt
RUN python3 -m pip install unidecode
COPY . .
CMD ["python3", "-m", "Fantastic"]
