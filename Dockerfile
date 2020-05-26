FROM python:3.9.0b1-alpine3.11
RUN apk add sudo vim \
    pip install flask
