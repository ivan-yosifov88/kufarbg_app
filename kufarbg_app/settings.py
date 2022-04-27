import os
from pathlib import Path

# TODO UNMARK PASSWORD
# TODO ADD .ENV
# TODO ABOUT US CONTACT
# TODO 400 403 404
# TODO MEDIA FILES
# TODO SOME BASIC STYLE WORK
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%e!%5_ro!l#szp_=+9w^k!qd@y6_loe+urkz^a)8v+*7c87rin'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'kufarbg.herokuapp.com',
]

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'django_countries',
)

KUFARBG_APPS = (
    'kufarbg_app.main_app',
    'kufarbg_app.auth_app',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + KUFARBG_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kufarbg_app.url'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kufarbg_app.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'kufar_app_db',
#         'USER': 'postgres',
#         'PASSWORD': '1123QwER',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd92ruocard477h',
        'USER': 'kucbfzfouvypyj',
        'PASSWORD': '9c9e99cfc4e905b517136d859a14caaad8dc49b1fd4c45800be117476d64427a',
        'HOST': 'ec2-52-48-159-67.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

# TODO just for debug
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = BASE_DIR / 'mediafiles'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'auth_app.AppUser'

LOGOUT_REDIRECT_URL = '/'

cloudinary.config(
    cloud_name="hrrbsagau",
    api_key="779171527341692",
    api_secret="XXmisQhptqTUgtX0Hi3Fa3fSN9I"
)