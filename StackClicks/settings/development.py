from .base import *

SECRET_KEY = 'g-0fa7+o#*2@27n5xz0lsjo5=q=h+^bq(wn!%w5c0oqyukjbj$'

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}