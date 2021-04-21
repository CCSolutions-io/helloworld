FROM python:3.9.2-alpine3.13

MAINTAINER Antony R. Goetzschel CTO SendEx LLC <ago@ccsolutions.io>

RUN apk update && apk upgrade
RUN apk add --update python3-dev

# Adding Python Requirements
ADD requirements.txt /temp/requirements.txt

RUN pip3 install -r /temp/requirements.txt

# Add custom user and setup home directory
RUN adduser -s /bin/true -u 1000 -D -h /app lighton

ADD main.py /app/main.py

WORKDIR app

USER lighton

CMD ["python3", "main.py"]