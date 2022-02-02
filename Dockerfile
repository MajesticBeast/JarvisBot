# syntax=docker/dockerfile:1

FROM python:3.9.10-slim-buster

WORKDIR /jarvis/

COPY . /jarvis/

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
