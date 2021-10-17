FROM python:3.9-slim

WORKDIR /app

EXPOSE 8000

RUN pip install -U pip -U setuptools gunicorn psycopg2-binary

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT gunicorn server.wsgi -b 0.0.0.0 --log-file - --access-logfile -
