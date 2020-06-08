VENDOR_APPS = [
    'crispy_forms',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'forum',
    'accounts',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + VENDOR_APPS
