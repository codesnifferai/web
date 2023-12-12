run: env requirements server
	env server

env:
	virtualenv env
	source env/bin/activate

requirements: 
	pip install django
	pip install djangorestframework
	pip install torch
	pip install -U sentence-transformers
	# conda install -c conda-forge sentence-transformers
	# pip install -e
	pip install --upgrade pip
	pip install -r requirements.txt

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic 
	python manage.py runserver 

test: 
	pip install -r requirements.txt
