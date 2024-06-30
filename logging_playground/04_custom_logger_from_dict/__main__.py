import logging.config
import yaml


with open("config.yml", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.info("Warning message using dict config")
