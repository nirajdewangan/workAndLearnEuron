import logging
import os


def setup_logger():
    """Configure and return the application logger."""

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("activity_logger")

    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    # All logs: DEBUG and above
    application_handler = logging.FileHandler(
        "logs/application.log",
        encoding="utf-8"
    )

    application_handler.setLevel(logging.DEBUG)

    # Only ERROR and CRITICAL logs
    error_handler = logging.FileHandler(
        "logs/error.log",
        encoding="utf-8"
    )

    error_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    application_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    logger.addHandler(application_handler)
    logger.addHandler(error_handler)

    return logger