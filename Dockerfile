FROM python:slim
WORKDIR /app
EXPOSE 8000
RUN pip install -U pip -U setuptools psycopg2-binary channels-redis
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT mkdir -p logs \
        && python manage.py migrate \
        && python manage.py collectstatic --no-input \
        && daphne server.asgi:application -b 0.0.0.0 --access-log logs/daphne.log
