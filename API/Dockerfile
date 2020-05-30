FROM python:3.9.0b1-alpine3.11

ENV FLASK_APP=app.py FLASK_ENV=development FLASK_DEBUG=True

RUN RUN rm -rf /var/cache/apk/* && \
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

ADD API /API

WORKDIR /API

COPY requirements requirements.txt

RUN pip3 install -r requirements.txt
RUN flask db init && \
    flask db migrate && \
    flask db upgrade

CMD ["flask","run","--host=0.0.0.0"]