import os

from file_organizer import (
    detect_file_type,
    create_destination_folder,
    move_file,
    log_operation,
    UnsupportedFileError
)


def organize_folder(folder_path):
    """Organize files inside the given folder."""

    if not os.path.exists(folder_path):
        print("Source folder does not exist.")

        log_operation(
            f"Source folder not found: {folder_path}",
            "FAILED"
        )

        return

    if not os.path.isdir(folder_path):
        print("The provided path is not a folder.")

        log_operation(
            f"Invalid folder path: {folder_path}",
            "FAILED"
        )

        return

    files = os.listdir(folder_path)

    if not files:
        print("Folder is empty.")

        log_operation(
            f"No files found in: {folder_path}",
            "INFO"
        )

        return

    print("\nStarting File Organizer")
    print("=" * 50)

    for filename in files:

        file_path = os.path.join(
            folder_path,
            filename
        )

        if not os.path.isfile(file_path):
            continue

        try:
            category = detect_file_type(
                file_path
            )

            destination_folder = (
                create_destination_folder(
                    folder_path,
                    category
                )
            )

            new_path = move_file(
                file_path,
                destination_folder
            )

            print(
                f"SUCCESS: {filename} -> {category}/"
            )

            print(
                f"Location: {new_path}"
            )

        except UnsupportedFileError as error:

            print(
                f"UNSUPPORTED: {filename}"
            )

            log_operation(
                f"Unsupported file "
                f"'{filename}': {error}",
                "FAILED"
            )

        except FileNotFoundError as error:

            print(
                f"FILE ERROR: {error}"
            )

            log_operation(
                str(error),
                "FAILED"
            )

        except PermissionError as error:

            print(
                f"PERMISSION ERROR: {error}"
            )

            log_operation(
                f"Permission error for "
                f"'{filename}': {error}",
                "FAILED"
            )

        except OSError as error:

            print(
                f"OPERATING SYSTEM ERROR: {error}"
            )

            log_operation(
                f"OS error for "
                f"'{filename}': {error}",
                "FAILED"
            )

    print("=" * 50)
    print("File organization completed.")


def main():

    folder_path = input(
        "Enter folder path to organize: "
    ).strip()

    organize_folder(folder_path)


if __name__ == "__main__":
    main()