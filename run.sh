#!/bin/bash

virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install -r requirements_ai.txt
python manage.py makemigrations
python manage.py migrate

#xdg-open http://127.0.0.1:8000/

python manage.py runserver 