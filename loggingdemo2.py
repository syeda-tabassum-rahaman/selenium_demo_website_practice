import logging

logging.basicConfig(filename="C://selenium_projects//data//test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= "%m/%d/%Y %I:%M:%S %p",
                    level = logging.DEBUG
                    )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("this is a debug message")
logger.info("this is an info message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")