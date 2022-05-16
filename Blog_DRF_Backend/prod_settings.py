import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bl_drf',
        'USER' : 'sergey',
        'PASSWORD' : 'Demio125',
        'HOST' : 'localhost',
        'PORT' : '',
    }
}


STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR +'/blog_vuejs', 'stat')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')