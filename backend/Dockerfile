FROM python:3.9.0b1-alpine3.11
RUN apk add --no-cache gcc sudo bash
RUN adduser -D -s /bin/bash -h /KanbanDashboard -g '' python
WORKDIR /KanbanDashboard/app
RUN pip3 install flask && \
    pip3 install python-dotenv
CMD ["flask","run","-p 80","--host=0.0.0.0"]