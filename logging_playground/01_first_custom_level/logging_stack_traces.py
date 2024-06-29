import logging

num_1 = 5
num_2 = 0

try:
    result = num_1/num_2
except Exception as e:
    logging.error("Exception ocurred", exc_info=True)
    logging.exception("Exception ocurred")
    # logging.exception = logging.error with exc_info=True
