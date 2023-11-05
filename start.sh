#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# To update run
pip install --upgrade pip

# Install required packages (change this if needed)
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
