#runserver
run:
	python manage.py runserver 8080

#makemigrations and migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate

super:
	python manage.py createsuperuser