import os

from activity_logger.exceptions import FileOperationError


def read_file(file_name, logger):
    """Read and return the contents of a file."""

    logger.debug(
        "Attempting to read file: %s",
        file_name
    )

    try:

        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

            if not content.strip():

                logger.warning(
                    "File was empty: %s",
                    file_name
                )

                return ""

            logger.info(
                "File read successfully: %s",
                file_name
            )

            return content

    except FileNotFoundError:

        logger.error(
            "File could not be opened because "
            "it does not exist: %s",
            file_name
        )

        raise FileOperationError(
            "File not found."
        )

    except PermissionError:

        logger.error(
            "Permission denied while reading: %s",
            file_name
        )

        raise FileOperationError(
            "Permission denied."
        )

    except OSError as error:

        logger.error(
            "File read error for %s: %s",
            file_name,
            error
        )

        raise FileOperationError(
            "Unable to read the file."
        )


def write_file(
    file_name,
    content,
    logger
):
    """Write content to a file."""

    logger.debug(
        "Attempting to write file: %s",
        file_name
    )

    try:

        parent_directory = os.path.dirname(
            file_name
        )

        if parent_directory:

            os.makedirs(
                parent_directory,
                exist_ok=True
            )

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        if not content.strip():

            logger.warning(
                "Empty content written to file: %s",
                file_name
            )

        logger.info(
            "File written successfully: %s",
            file_name
        )

        return True

    except PermissionError:

        logger.error(
            "Permission denied while writing: %s",
            file_name
        )

        raise FileOperationError(
            "Permission denied."
        )

    except OSError as error:

        logger.error(
            "File write error for %s: %s",
            file_name,
            error
        )

        raise FileOperationError(
            "Unable to write to the file."
        )