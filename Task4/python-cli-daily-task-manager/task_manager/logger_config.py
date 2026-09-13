import logging
import os


def setup_logger():
    """Create and return the application logger."""

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            "logs/task_manager.log",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger