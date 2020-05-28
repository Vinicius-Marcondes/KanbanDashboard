FROM python:3.9.0b1-alpine3.11

ENV FLASK_APP=API
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True

RUN apk add --no-cache gcc sudo bash
RUN adduser -D -s /bin/bash -h /KanbanDashboard -g '' python

WORKDIR /KanbanDashboard/
ADD . API

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN flask db init && \
    flask db migrate && \
    flask db upgrade

CMD ["flask","run","-p 80","--host=0.0.0.0"]