import os

# DB for docker-compose

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost', # set in docker-compose.yml
        'PORT': 5432 # default postgres port
    }
}


#SQLite

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Database Heroku

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'd8ij4o0tv5a3v',
#        'PASSWORD': '184360dca99810ef212e71e7770b7dc9d5d5a3b51564f58047580200b54a1ac2',
#        'HOST': 'ec2-54-235-92-43.compute-1.amazonaws.com',
#        'USER': 'itrdofreyezwjm',
#        'PORT': '5432',
#    }
#}

# Heroku: Update database configuration from $DATABASE_URL.

#import dj_database_url

#DATABASES['default'].update(dj_database_url.config('postgres://itrdofreyezwjm:184360dca99810ef212e71e7770b7dc9d5d5a3b51564f58047580200b54a1ac2@ec2-54-235-92-43.compute-1.amazonaws.com:5432/d8ij4o0tv5a3v'))