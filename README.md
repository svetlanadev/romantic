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
cd source romanitc/bin/activate
```
The third step - you need install the packages. If you are using pip version 7.1.2, you need upgrade pip
```sh
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Create database and run server
```sh
python manage.py migrate
python manage.py runserver
```

Good luck!