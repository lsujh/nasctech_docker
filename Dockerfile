FROM python:3.8-slim
#FROM python:buster
LABEL maintainer="Ihor Diakiv <lsujh72@gmail.com>"
RUN apt-get update
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
#RUN pip3 install uwsgi
COPY app/ .
CMD [ "python3", "./main.py"]
#CMD ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "./main.py", \
#    "--callable", "app", "--stats", "0.0.0.0:81"]