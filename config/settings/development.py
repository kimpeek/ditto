import environ

from .base import *

env = environ.Env()
env.read_env()

SECRET_KEY = 'h&)6xdkip#3rqpudv)ddh^$^v3&x@lbm!uc6f!)8l5#!6369dr'

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

INTERNAL_IPS = ALLOWED_HOSTS