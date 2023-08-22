import logging


def setup_logging(log_file='test.log', log_level=logging.INFO):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='w'
    )


def get_logger(name):
    return logging.getLogger(name)
