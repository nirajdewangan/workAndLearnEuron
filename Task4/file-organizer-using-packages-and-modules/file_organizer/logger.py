from datetime import datetime


LOG_FILE = "organizer.log"


def log_operation(message, status="INFO"):
    """Record every successful or failed operation."""

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_message = (
        f"[{timestamp}] "
        f"[{status}] "
        f"{message}\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_message)