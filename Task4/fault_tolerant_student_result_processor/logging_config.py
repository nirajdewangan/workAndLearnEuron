import logging


def setup_logger():
    """Configure and return application logger."""

    logging.basicConfig(
        filename="student_result.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)