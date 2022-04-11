# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /server
COPY . /server/
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache \
    pip3 install -r requirements.txt
ENV FLASK_APP server
CMD [ "python3", "server.py"]