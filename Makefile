MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=romantic.settings $(MANAGE) test blog

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=romantic.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=romantic.settings $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=romantic.settings $(MANAGE) migrate blog

schema:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=romantic.settings $(MANAGE) schemamigration blog --auto

port:
	sudo fuser -k 8000/tcp