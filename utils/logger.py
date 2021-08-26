import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from logging import StreamHandler

from settings import BASE_DIR


log_fname = os.path.join(BASE_DIR, "ptz_camera_controller.log")
log_formatter = Formatter(fmt="%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")
file_handler = RotatingFileHandler(filename=log_fname, mode='a', maxBytes=5 * 1024 * 1024, backupCount=5,
                                   encoding='utf8', delay=False)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(fmt=log_formatter)

console_handler = StreamHandler()
console_handler.setFormatter(fmt=log_formatter)
console_handler.setLevel(logging.INFO)

logger = logging.getLogger('CL')
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
