
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

FORCE_SCRIPT_NAME = ''

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

# try:
#     from local_settings import *
# except ImportError:
#     pass