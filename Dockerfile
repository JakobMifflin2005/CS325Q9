FROM python:latest

WORKDIR /home


COPY req /home

RUN pip install --no-cache-dir -r requirements.txt



COPY . .
