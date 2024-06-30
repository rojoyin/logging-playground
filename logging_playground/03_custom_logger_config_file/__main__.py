import logging.config

logging.config.fileConfig(
    fname="logger_configuration.conf",
    disable_existing_loggers=False
)

logger = logging.getLogger(__name__)

logger.warning("This is my warning message")
