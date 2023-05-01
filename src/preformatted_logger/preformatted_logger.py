import logging

### This logger defaults to the name 'root' and the INFO level. Its output
###    will be "TIME_STAMP | LEVEL | FILENAME:LINE_NUMBER - MESSAGE".
def get_logger(name='root', level='INFO'):
    logger = logging.getLogger(name)

    if len(logger.handlers) == 0:
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt='%(asctime)s | %(levelname).4s | %(filename)s:%(lineno)d - %(message)s'))
        logger.addHandler(handler)

    return logger
