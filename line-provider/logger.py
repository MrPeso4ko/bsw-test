import logging
from config import settings


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(settings.log.level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(settings.log.format))
    logger.addHandler(handler)
    return logger
