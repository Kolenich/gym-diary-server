#!/bin/sh

mkdir -p logs
python manage.py migrate
python manage.py collectstatic --no-input
daphne server.asgi:application -b 0.0.0.0 --access-log logs/daphne.log
