import logging

console_formatter = logging.Formatter("%(name)s | %(levelname)s | %(message)s")
file_formatter = logging.Formatter("%(asctime)s | %(process)d | %(name)s | %(levelname)s | %(message)s")
