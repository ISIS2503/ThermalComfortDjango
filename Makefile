migrate:
	docker-compose run --rm app ./manage.py makemigrations --settings=thermalComfort.settings
	docker-compose run --rm app ./manage.py migrate auth --settings=thermalComfort.settings
	docker-compose run --rm app ./manage.py migrate --settings=thermalComfort.settings

requirements:
	docker-compose run --rm app pip install -r ./requirements.txt

statics:
	docker-compose run --rm app ./manage.py collectstatic --no-input --settings=thermalComfort.settings

superuser:
	docker-compose run --rm app ./manage.py createsuperuser --settings=thermalComfort.settings
