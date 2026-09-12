import os
import shutil

from .logger import log_operation


def create_destination_folder(source_folder, category):
    """Create destination folder when it is missing."""

    destination_folder = os.path.join(
        source_folder,
        category
    )

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

        log_operation(
            f"Created destination folder: {destination_folder}",
            "SUCCESS"
        )

    return destination_folder


def get_unique_filename(destination_folder, filename):
    """Prevent duplicate filenames from being overwritten."""

    destination_path = os.path.join(
        destination_folder,
        filename
    )

    if not os.path.exists(destination_path):
        return destination_path

    name, extension = os.path.splitext(filename)

    counter = 1

    while True:
        new_filename = f"{name}_{counter}{extension}"

        destination_path = os.path.join(
            destination_folder,
            new_filename
        )

        if not os.path.exists(destination_path):
            return destination_path

        counter += 1


def move_file(file_path, destination_folder):
    """Move a file safely to its destination folder."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

    if not os.path.exists(destination_folder):
        raise FileNotFoundError(
            f"Destination folder does not exist: "
            f"{destination_folder}"
        )

    filename = os.path.basename(file_path)

    destination_path = get_unique_filename(
        destination_folder,
        filename
    )

    try:
        shutil.move(
            file_path,
            destination_path
        )

        log_operation(
            f"Moved '{filename}' to '{destination_path}'",
            "SUCCESS"
        )

        return destination_path

    except PermissionError as error:
        log_operation(
            f"Permission denied while moving "
            f"'{filename}': {error}",
            "FAILED"
        )

        raise