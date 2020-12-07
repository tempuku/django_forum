import os

from .path import TEMPLATES_PATH
from distutils.util import strtobool

DEBUG = bool(strtobool(os.getenv('DEBUG')))
TEST = bool(strtobool(os.getenv('TEST')))

ALLOWED_HOSTS = ['*']

DEFAULT_SECRET_KEY = 'secretsecret'
SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_PATH,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'garpix_menu.context_processors.menu_processor',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/forum'
LOGOUT_REDIRECT_URL = '/forum'

# FILE_UPLOAD_PERMISSIONS = 0o644
# AUTH_USER_MODEL = 'user.User'

SITE_ID = os.getenv('SITE_ID') or 1
SITE_URL = os.getenv('SITE_URL')

DEFAULT_PAGE_SIZE = 15

PASSWORD_DURATION_DAYS = 90

# RECAPTCHA_PRIVATE_KEY = 'get_key_from_google'
# RECAPTCHA_PUBLIC_KEY = 'get_key_from_google'
# RECAPTCHA_DEFAULT_ACTION = 'generic'
# RECAPTCHA_SCORE_THRESHOLD = 0.5
#
# CORS_ORIGIN_ALLOW_ALL = True