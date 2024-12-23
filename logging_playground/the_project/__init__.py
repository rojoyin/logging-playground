import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler()

console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)
