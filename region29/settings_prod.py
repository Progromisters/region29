# -*- coding: utf-8 -*-
DEBUG = False

ALLOWED_HOSTS = ['водитель29.рф','188.225.39.136', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'region29',
        'USER': 'region29user',
        'PASSWORD': 'Guido!956',
        'HOST': 'localhost',
        'PORT': '',
    }
}