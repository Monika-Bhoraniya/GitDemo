import logging
class BaseClass:
    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        logger.debug("A debug statement")
        logger.info("information statement")
        logger.warning("something is in warning mode")
        logger.error("A major error")
        logger.critical("criticaal issue")

        return logger
