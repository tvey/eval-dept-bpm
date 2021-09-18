from .base import *

dotenv.load_dotenv(BASE_DIR / 'local.env')

SECRET_KEY = 'wow-much-mystery'

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
