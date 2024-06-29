import logging

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler("file.log")
file_handler.setLevel(logging.ERROR)
