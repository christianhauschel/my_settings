import logging
from rich.logging import RichHandler
from logging.handlers import RotatingFileHandler


def logger_custom(
    name="name",
    fname=None,
    console=True,
    level_file=logging.DEBUG,
    level_console=logging.DEBUG,
    format_file="%(asctime)s:%(levelname)s:%(message)s",
    format_console="%(message)s",
    format_date="%Y-%m-%d %H:%M:%S",
    max_bytes=500e6,
    backup_count=10,
    **handler_file
):

    if console:
        logging.basicConfig(
            level=level_console,
            format=format_console,
            datefmt=format_date,
            handlers=[RichHandler()],
        )

    logger = logging.getLogger(name)

    # Create a FileHandler for file output
    if fname is not None:
        file_handler = RotatingFileHandler(
            fname, maxBytes=max_bytes, backupCount=backup_count, **handler_file
        )
        file_handler.setLevel(level_file)
        formatter = logging.Formatter(format_file, datefmt=format_date)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
