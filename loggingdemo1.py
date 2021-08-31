import logging

logging.basicConfig(filename="C://selenium_projects//data//test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= "%m/%d/%Y %I:%M:%S %p",
                    level = logging.DEBUG
                    )

logging.debug("this is a debug message")
logging.info("this is an info message")
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")