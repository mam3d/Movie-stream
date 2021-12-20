import os

if os.environ.get("PRODUCTION") == "true":
    from .production import *
else:   
    from .local import *

from config.celery import app

__all__ = ["app"]