import json
import os

from task_manager.exceptions import StorageError


DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

            if not isinstance(data, list):
                raise StorageError(
                    "Invalid task data format."
                )

            return data

    except json.JSONDecodeError as error:
        raise StorageError(
            f"Unable to read task data: {error}"
        )

    except OSError as error:
        raise StorageError(
            f"Unable to open task file: {error}"
        )


def save_tasks(tasks):
    """Save tasks to JSON file."""

    try:
        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                tasks,
                file,
                indent=4
            )

    except OSError as error:
        raise StorageError(
            f"Unable to save task data: {error}"
        )

    finally:
        print("Storage operation completed.")