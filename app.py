import os

from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
from celery.app.log import TaskFormatter
import logging
import settings

VERSION = 'dcim-1.7-dev'
LOGGING = getattr(settings, 'LOGGING', {})
os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')
app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    if settings.ENABLE_RSYSLOG:
        # FileHandler
        fh = logging.FileHandler(f'{os.getcwd()}/logs.txt')
        fh.setLevel(0)
        logger.addHandler(fh)
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))


@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    if settings.ENABLE_RSYSLOG:
        # FileHandler
        fh = logging.FileHandler(f'{os.getcwd()}/logs.txt')
        fh.setLevel(0)
        logger.addHandler(fh)
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter('%(asctime)s - %(levelname)s - %(name)s - %(task_id)s - %(task_name)s - %(message)s'))
