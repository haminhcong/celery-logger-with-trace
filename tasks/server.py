import logging
from celery.utils.log import get_task_logger

import time

from app import app

logger = get_task_logger(__name__)


@app.task(name='server.get_server_info')
def get_server_info(server_ip, server_name):
    logger.info(f'Server IP {server_ip}')
    time.sleep(10)
    logger.info(f'Server Name {server_name}')
