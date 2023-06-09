#!/usr/bin/env bash
# exit on error
set -o errexit
python -m pip install --upgrade pip setuptools
poetry install
poetry lock
cd kollabhunt_backend
python manage.py collectstatic --no-input
python manage.py migrate