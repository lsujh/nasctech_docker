FROM python:3.8-slim-buster
LABEL maintainer="Ihor Diakiv <lsujh72@gmail.com>"
RUN apt-get update
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .
CMD [ "python3", "./main.py"]