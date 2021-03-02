# base image
FROM snakepacker/python:all as builder

# Create virtualenv
RUN python3.6 -m venv /usr/share/python3/app

ADD requirements.txt /tmp/
RUN apt-get update && apt-get install gcc python-dev libsasl2-dev -y && \
    /usr/share/python3/app/bin/pip install --no-cache-dir \
    --upgrade pip -Ur /tmp/requirements.txt
