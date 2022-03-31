"""desafio_celero Celery Configuration. """
from __future__ import absolute_import, unicode_literals
import os
from logging.config import dictConfig
from celery import Celery
from celery.signals import setup_logging
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desafio_celero.settings')

APP = Celery('desafio_celero')

APP.config_from_object('django.conf:settings', namespace='CELERY')

APP.autodiscover_tasks()


@APP.task(bind=True)
def debug_task(self):
    """
    Debug Task.
    """
    print(f'Request: {self.request!r}')


if settings.DEBUG:
    @setup_logging.connect
    def config_loggers(*args, **kwags):  # pylint: disable=unused-argument
        """
        Configures loggers.
        """
        dictConfig(settings.LOGGING)
