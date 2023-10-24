#!/bin/bash


pip instal django
pip instal djangorestframework
pip instal torch
pip install -U sentence-transformers
conda install -c conda-forge sentence-transformers
pip install -e

virtualenv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic -y
# http://127.0.0.1:8000/

python manage.py runserver 