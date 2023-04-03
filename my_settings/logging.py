import logging
from rich.logging import RichHandler
from logging.handlers import RotatingFileHandler
from rich.console import Console


def logger_custom(
    name="name",
    fname=None,
    console=True,
    level_file=logging.DEBUG,
    level_console=logging.DEBUG,
    format_file="%(asctime)s:%(levelname)s:%(message)s",
    format_console="%(message)s",
    format_date="%Y-%m-%d %H:%M:%S",
    maxBytes=500e6,
    backupCount=10,
):

    # if console:
    #     logging.basicConfig(
    #         level=level_console, format=format_console, datefmt=format_date, handlers=[RichHandler()]
    #     )

    logger = logging.getLogger(name)

    # Create a RichHandler for console output
    if console:
        logger.setLevel(level_console)
        console_handler = RichHandler(
            markup=True, log_time_format=format_date, level=level_console
        )
        # console_handler.setLevel(level_console)
        if format_console is None:
            formatter = logging.Formatter(format_console)
            console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # Create a FileHandler for file output
    if fname is not None:
        file_handler = RotatingFileHandler(
            fname, maxBytes=maxBytes, backupCount=backupCount
        )
        file_handler.setLevel(level_file)
        formatter = logging.Formatter(format_file, datefmt=format_date)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
