# Romantic

Web-site of sport-club "Romantic".

Deploing server

The first you need make clone romantic rep from githun

```sh
git clone https://github.com/dlyapun/romantic.git
```
After you need create virtual environment.

For Windows:
```sh
virtualenv-3.4.exe romantic --no-site-packages
cd .\romantic\Scripts\
.\activate
```
For Linux:
```sh
virtualenv romantic --no-site-packages
source romanitc/bin/activate
```
The third step - you need install the packages. If you are using pip version 7.1.2, you need upgrade pip
```sh
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Create file "local_settings.py" and paste this blog:
```sh
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

DEBUG = True

MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, "./media"))
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, "./static"))
```

Create file "secret_key_settings.py" with the SECRET_KEY, or generate one:
```sh
SECRET_KEY='romantik9)4hi36z21fiqz@mht9%&n)-oljgiv6l)a*ayrda$0^a))zig(local'
```

Create database and run server
```sh
python manage.py migrate
python manage.py runserver
```

### Troubleshooting

* Troubles installing **Pillow** module:

```sh
apt-get install libjpeg-dev libjpeg8-dev
pip install --no-cache-dir -I pillow
```

* Problems with greenlet
Try this (sorry, no idea what helped exactly:
```sh
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7  libgle3 python-dev
sudo pip install greenlet
```

Good luck!
