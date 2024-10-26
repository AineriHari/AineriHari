import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that the things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problems
# in the near future (e.g. 'disk space low'). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(filename='test.log', level=logging.DEBUG, 
# format="%(asctime)s:%(levelname)s:%(message)s")

# def add(x, y):
#     return x + y


# result = add(1, 2)
# logging.debug(result)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler(filename="test.log")
file_handler.setLevel(logging.DEBUG) # add the logs from debug in log file
file_handler.setFormatter(formatter)

stearm_handler = logging.StreamHandler() # printing the console logs
stearm_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stearm_handler)


def add(x, y):
    return x + y


result = add(1, 2)
logger.debug(result)