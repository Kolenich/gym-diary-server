FROM python:slim
WORKDIR /app
EXPOSE 8000
RUN pip install -U pip -U setuptools psycopg2-binary channels-redis
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x ./dockerentrypoint.sh
ENTRYPOINT ["./dockerentrypoint.sh"]
