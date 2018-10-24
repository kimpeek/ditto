import environ

from .base import *

env = environ.Env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db('DATABASE_URL')
}

ADMIN_URL = env('ADMIN_URL', default='admin/')

# Individuals to receive email notification on 500 server error
ADMINS = [
    # ('FULL_NAME', 'NAME@EMAIL.COM'),
]