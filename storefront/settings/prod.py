import os
from .common import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['https://storefront3.onrender.com']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}

REDIS_URL = os.environ.get('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}