# coding=utf-8

import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = '=q@eild4ch4mg#lyso0^^gnd4r2bc&@lj*sw=ua1gpe$#ua4x6'

DEBUG = False

TEMPLATE_DEBUG = False

SITE_ID = 1

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ADMINS = (
    ('Dmitry Lyapun', 'dlyapun@gmail.com'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = [
    '127.0.0.1:8000',
    '.example.com',
    '.tkr.od.ua',
]

INTERNAL_IPS = ("127.0.0.1",)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

for root, dirs, files in os.walk(PROJECT_ROOT):
    if 'templates' in dirs:
        TEMPLATE_DIRS += (os.path.join(root, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'hike',
    'profile',
    'imagekit',
    'party',
    'force_blog',
    'bootstrap_pagination',
    'page_navigation',
    'materials',
    'info_pages',
    'django_cleanup',
    'photo_check',
    'redactor',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    'profile.context_processor.contex_profile',
    'info_pages.context_processor.contex_info_pages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'profile.middleware.AutoLogout',
)

ROOT_URLCONF = 'romantic.urls'

WSGI_APPLICATION = 'romantic.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dlyapun_romantic',
        'USER': 'dlyapun',
        'PASSWORD': 'vy8yfjx9MPbV',
        'HOST': '',
        'PORT': '',
    }
}


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common_static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

try:
    from local_settings import *
except ImportError:
    pass


SOCIAL_AUTH_FACEBOOK_KEY = '1602017563346275'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ebc2b04baf9d0421d766d31be62e8e2b'

SOCIAL_AUTH_TWITTER_KEY = 'eYzXFuk4K4L0siJwp7w9wm1Yt'
SOCIAL_AUTH_TWITTER_SECRET = 'qfHHktIzkvToq1dQeYxZY8udhUzVlMFtjBa9TzOTc5NnTimyoU'

LOGIN_URL = '/login/'
LOGOUT_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/blog/'

SOCIAL_AUTH_VK_APP_KEY = '4816303'
SOCIAL_AUTH_VK_OAUTH2_KEY = '4816303'
SOCIAL_AUTH_VK_APP_SECRET = '5HO4lXQiwRRfuoAFI4mh'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '5HO4lXQiwRRfuoAFI4mh'

AUTH_PROFILE_MODULE = "profile.CustomUser"

DEFAULT_BANNER_TITLE = 3

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'support@tkr.od.ua'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.wservices.ch'
EMAIL_HOST_USER = 'support@tkr.od.ua'
EMAIL_HOST_PASSWORD = 'Blasco5454588407@'
EMAIL_PORT = 587

SERVER_EMAIL = 'support@tkr.od.ua'
DEFAULT_FROM_EMAIL = 'support@tkr.od.ua'

REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'uploads/'

FORCE_SCRIPT_NAME = ''

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 13600

AUTO_LOGOUT_DELAY = 1
