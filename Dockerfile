# syntax=docker/dockerfile:1

# Python official Image: https://hub.docker.com/_/python
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN pwd && ls
# Same as running locally but listen on every available network interface
# anybody on the Internet is able to connect to your server by typing in browser your server IP address.
CMD ["flask", "--app", "flaskr", "--debug", "run", "--host=0.0.0.0"]
