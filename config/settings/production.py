from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ["whitenoise.runserver_nostatic"]
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]