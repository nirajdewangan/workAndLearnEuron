import os

from .exceptions import UnsupportedFileError


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".txt": "Text",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "Data",
    ".xlsx": "Data",
}


def detect_file_type(file_path):
    """Return destination folder based on file extension."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

    if not os.path.isfile(file_path):
        raise ValueError(
            f"Path is not a file: {file_path}"
        )

    _, extension = os.path.splitext(file_path)

    extension = extension.lower()

    if extension not in FILE_CATEGORIES:
        raise UnsupportedFileError(extension)

    return FILE_CATEGORIES[extension]