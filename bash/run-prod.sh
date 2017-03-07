#!/bin/sh
set -e
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn payments.wsgi -b 0.0.0.0:8000 --log-file -