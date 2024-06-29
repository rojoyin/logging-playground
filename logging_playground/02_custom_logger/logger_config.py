from logging_handlers import console_handler, file_handler
from logging_formatters import console_formatter, file_formatter


console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)
