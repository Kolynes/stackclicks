from .base import *
import os
from dotenv import load_dotenv

dotenv_file = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_file)

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.getenv("DATABASE_NAME"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'USER': os.getenv("DATABASE_USER"),
        'HOST': os.getenv("DATABASE_HOST"),   # Or an IP Address that your DB is hosted on
        'PORT': os.getenv("DATABASE_PORT"),
    }
}
