import logging
from logger_config import console_handler, file_handler


logger = logging.getLogger(__name__)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.warning("This is a warning message")
logger.critical("This is a critical message")
