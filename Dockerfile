FROM python:3-slim
WORKDIR /app
EXPOSE 8000
RUN pip install -U pip -U setuptools gunicorn psycopg2-binary
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT mkdir -p logs \
        && python manage.py migrate \
        && python manage.py collectstatic --no-input \
        && gunicorn server.wsgi -b 0.0.0.0 --log-file logs/gunicorn.log --access-logfile logs/gunicorn.log
