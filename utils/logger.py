import logging

def get_logger(name):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    return logging.getLogger(name)


# from utils.logger import get_logger
# logger = get_logger(__name__)
# logger.info("Starting download")