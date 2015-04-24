# coding=utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, random
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = '=q@eild4ch4mg#lyso0^^gnd4r2bc&@lj*sw=ua1gpe$#ua4x6'

DEBUG = True

TEMPLATE_DEBUG = True

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
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
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
    # "django.contrib.redirects",
    # "django.contrib.sites",
    # "django.contrib.sitemaps",
    'hike',
    'profile',
    'imagekit',
    'django_summernote',
    # 'party',
    'force_blog',
    'bootstrap_pagination',
    'django_select2',
    'power_comments',
    'banner',
    'page_navigation',
    'debug_toolbar',
    'materials',
    'social_auth',
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
    'banner.context_processor.contex_banner',
    'party.context_processor.contex_party',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'romantic.urls'

WSGI_APPLICATION = 'romantic.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/ukrainem/domains/tkr.od.ua/public_html/media/'
STATIC_ROOT = '/home/ukrainem/domains/tkr.od.ua/public_html/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

try:
    from local_settings import *
except ImportError:
    pass


try:
    from django_summernote_settings import *
except ImportError:
    pass

FACEBOOK_APP_ID = '1602017563346275'
FACEBOOK_API_SECRET = 'ebc2b04baf9d0421d766d31be62e8e2b'

# TWITTER_CONSUMER_KEY = 'RYeEUefjidJ8ptuN9RSVWxTn8'
# TWITTER_CONSUMER_SECRET = 'Z4yQGYDMtdALSZhPZAsXrPcirhOH6uXVQZTkdOb6rFfTeiB0zt'

VK_APP_ID = '4816303'
VKONTAKTE_APP_ID = VK_APP_ID
VK_API_SECRET = '5HO4lXQiwRRfuoAFI4mh'
VKONTAKTE_APP_SECRET = VK_API_SECRET

# GOOGLE_OAUTH2_CLIENT_ID = '776153762160-r2qq335ctj8mdnqvidgnoi691m241v3k.apps.googleusercontent.com'
# GOOGLE_OAUTH2_CLIENT_SECRET = '22lDMovOA0-p8jcEdPQUF_mN'

AUTH_PROFILE_MODULE = "profile.CustomUser"

SOCIAL_AUTH_USER_MODEL = 'profile.CustomUser'

# INPLACEEDIT_DISABLE_CLICK = False
# THUMBNAIL_DEBUG = True
# INPLACEEDIT_EVENT = "click"

DEFAULT_KARMA = 15
DEFAULT_BANNER_TITLE = 3

DEBUG_TOOLBAR_PATCH_SETTINGS = False

CONFIG_DEFAULTS = {
    # Toolbar options
    'DISABLE_PANELS': set(['debug_toolbar.panels.redirects.RedirectsPanel']),
    'INSERT_BEFORE': '</body>',
    'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js',
    'RENDER_PANELS': None,
    'RESULTS_STORE_SIZE': 10,
    'ROOT_TAG_EXTRA_ATTRS': '',
    'SHOW_COLLAPSED': False,
    'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
}

# Если имя не удалось получить, то можно его сгенерировать
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth_Vader', 'Obi-Wan_Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
# Разрешаем создавать пользователей через social_auth
SOCIAL_AUTH_CREATE_USERS = True

# # Перечислим pipeline, которые последовательно буду обрабатывать респонс 
SOCIAL_AUTH_PIPELINE = (
    # Получает по backend и uid инстансы social_user и user
    'social_auth.backends.pipeline.social.social_auth_user',
    # Получает по user.email инстанс пользователя и заменяет собой тот, который получили выше.
    # Кстати, email выдает только Facebook и GitHub, а Vkontakte и Twitter не выдают
    'social_auth.backends.pipeline.associate.associate_by_email',
    # Пытается собрать правильный username, на основе уже имеющихся данных
    'social_auth.backends.pipeline.user.get_username',
    # Создает нового пользователя, если такого еще нет
    'social_auth.backends.pipeline.user.create_user',
    # Пытается связать аккаунты
    'social_auth.backends.pipeline.social.associate_user',
    # Получает и обновляет social_user.extra_data
    'social_auth.backends.pipeline.social.load_extra_data',
    # Обновляет инстанс user дополнительными данными с бекенда
    'social_auth.backends.pipeline.user.update_user_details'
)

# ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
# REGISTRATION_AUTO_LOGIN = True #
