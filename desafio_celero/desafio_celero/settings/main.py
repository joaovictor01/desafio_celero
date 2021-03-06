"""
Django settings for desafio_celero project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from kombu import Exchange, Queue
from celery.schedules import crontab
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODE = os.environ.get('MODE', default='development')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$ul%ti*dl0y&=8t3b^w8k%vze=vgu^d^vxvn@@e!hc042+o0d#'

ALLOWED_HOSTS = []

# Application definition

INTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'desafio_celero',
    'olympics',
]

EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'django_celery_results'
]

INSTALLED_APPS = INTERNAL_APPS + LOCAL_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'desafio_celero.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'desafio_celero.wsgi.application'

ASGI_APPLICATION = 'desafio_celero.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(PROJECT_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432')
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
    ('pt-br', 'Portugu??s Brasileiro'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'en'

DEFAULT_LANGUAGE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'desafio_celero/static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# RabbitMQ and Celery config

user = os.getenv('RABBITMQ_DEFAULT_USER')
password = os.getenv('RABBITMQ_DEFAULT_PASS')
host = os.getenv('RABBITMQ_HOST')
port = os.getenv('RABBITMQ_PORT')
vhost = os.getenv('RABBITMQ_DEFAULT_VHOST')
CELERY_BROKER_URL = f'amqp://{user}:{password}@{host}:{port}/{vhost}'

BROKER_POOL_LIMIT = 100  # the maximum number of connections that can be open in the connection pool

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True

CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default_tasks'),
)

CELERY_ROUTES = {
    '*': {
        'queue': 'default', 'routing_key': 'default_tasks',
    }
}

CELERY_RESULT_BACKEND = 'django-db'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%d/%m/%Y %H:%M:%S",
}


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(levelname)s] %(message)s',
        },
        'file': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
        },
    },
    'filters': {
        'debug': {
            '()': 'olympics.log_filters.DebugFilter',
        },
        'info': {
            '()': 'olympics.log_filters.InfoFilter',
        },
        'error': {
            '()': 'olympics.log_filters.ErrorFilter',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/desafio_celero/celery.log',
            'formatter': 'console',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
        },
        'file.debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/desafio_celero/django_debug.log',
            'formatter': 'file',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['debug'],
        },
        'file.info': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/desafio_celero/django_info.log',
            'formatter': 'file',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['info'],
        },
        'file.error': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/desafio_celero/django_error.log',
            'formatter': 'file',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['error'],
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console', 'file.debug', 'file.info', 'file.error'],
            'propagate': True,
        },
        'olympics': {
            'level': 'DEBUG',
            'handlers': ['console', 'file.debug', 'file.info', 'file.error'],
            'propagate': True,
        },
        'desafio_celero': {
            'level': 'DEBUG',
            'handlers': ['console', 'file.debug', 'file.info', 'file.error'],
            'propagate': True,
        },
        'celery': {
            'level': 'DEBUG',
            'handlers': ['celery', 'console'],
            'propagate': True,
        },
    },
}
