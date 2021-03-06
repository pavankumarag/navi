"""Logger util which returns logger object"""
import logging


def configure_log(level=None, name=None, filename=None):
    """
    This function configures the LOG module(uses standdard logging module of python) setting level to DEBUG
    and setting timestamp to %Y:%m:%dT%H:%M:%S format. This will return LOG object.
    Args:
        level (int): logger level
        name (str) : logger name
        filename (str) : filename to write logs
    Returns:
        logger (object)
    """
    if name is None:
        logger = logging.getLogger(__name__)
    else:
        logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    ch_formatter = logging.Formatter("\n%(asctime)s ::%(name)s     %(levelname)s      %(message)s", "%Y-%m-%d %H:%M:%S")
    console_handler.setFormatter(ch_formatter)
    logger.addHandler(console_handler)

    hdlr = logging.FileHandler(filename, "w")
    hdlr.setFormatter(ch_formatter)
    logger.addHandler(hdlr)

    return logger