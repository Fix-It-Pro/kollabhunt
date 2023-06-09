#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade poetry==1.5.1
poetry_version=$(poetry --version)
echo "Poetry version: $poetry_version"
poetry install
poetry lock
cd kollabhunt_backend
python manage.py collectstatic --no-input
python manage.py migrate