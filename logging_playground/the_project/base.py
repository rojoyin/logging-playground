import logging

# from logging_playground.project import add_module_handler

logger = logging.getLogger(__name__)
# add_module_handler(logger)


def func1():
    logger.debug("debug called from base.func1()")
    logger.critical("critical called from base.func1()")
