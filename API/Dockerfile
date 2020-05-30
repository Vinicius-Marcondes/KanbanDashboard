FROM python:3.9.0b1-alpine3.11

ENV HOME=/home/api FLASK_APP=app.py FLASK_ENV=development FLASK_DEBUG=True

RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add build-base && \
    apk add gcc && \
    apk add python3-dev && \
    apk add libffi-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk del build-base && \
    rm -rf /var/cache/apk/*

RUN adduser -D api
USER api
COPY --chown=api:api . $HOME/API
WORKDIR $HOME/API

RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements/dev.txt

EXPOSE 80
CMD ["venv/bin/flask","run","--host=0.0.0.0"]