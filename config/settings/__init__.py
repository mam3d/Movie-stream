import os

if os.environ.get("PRODUCTION") == "true":
    from .production import *
    
from .local import *