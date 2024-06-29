import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",  # default 'a'ppend
    format="%(name)s - %(levelname)s - %(message)s"
)
logging.warning("This will be logged to a file")
