from activity_logger.authentication import (
    login,
    logout
)

from activity_logger.calculator import (
    calculate
)

from activity_logger.exceptions import (
    ApplicationLoggerError,
    AuthenticationError,
    CalculationError,
    FileOperationError
)

from activity_logger.file_operations import (
    read_file,
    write_file
)

from activity_logger.logger_config import (
    setup_logger
)


logger = setup_logger()


def display_menu():
    """Display the application menu."""

    print(
        "\n=== APPLICATION ACTIVITY LOGGER ==="
    )

    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")
    print("6. Exit")


def handle_login():
    """Handle user login."""

    username = input(
        "Enter username: "
    ).strip()

    password = input(
        "Enter password: "
    )

    login(
        username,
        password,
        logger
    )

    print(
        "Login successful!"
    )

    return username


def handle_calculation():
    """Handle calculator operation."""

    try:

        first_number = float(
            input(
                "Enter first number: "
            )
        )

        operator = input(
            "Enter operator (+, -, *, /): "
        ).strip()

        second_number = float(
            input(
                "Enter second number: "
            )
        )

    except ValueError:

        logger.error(
            "Non-numeric calculator input received."
        )

        raise CalculationError(
            "Please enter valid numbers."
        )

    result = calculate(
        first_number,
        operator,
        second_number,
        logger
    )

    print(
        "Result:",
        result
    )


def handle_read_file():
    """Handle file reading operation."""

    file_name = input(
        "Enter file path: "
    ).strip()

    content = read_file(
        file_name,
        logger
    )

    if content:

        print(
            "\n--- FILE CONTENT ---"
        )

        print(content)

    else:

        print(
            "The file is empty."
        )


def handle_write_file():
    """Handle file writing operation."""

    file_name = input(
        "Enter file path: "
    ).strip()

    content = input(
        "Enter content: "
    )

    write_file(
        file_name,
        content,
        logger
    )

    print(
        "File written successfully."
    )


def run_application():
    """Run Application Activity Logger."""

    current_user = None

    logger.debug(
        "Application initialization completed."
    )

    logger.info(
        "Application started."
    )

    try:

        while True:

            display_menu()

            choice = input(
                "Enter your choice: "
            ).strip()

            logger.debug(
                "Menu option selected: %s",
                choice
            )

            try:

                if choice == "1":

                    if current_user:

                        logger.warning(
                            "Login attempted while "
                            "another user was logged in."
                        )

                        print(
                            "A user is already logged in."
                        )

                        continue

                    current_user = handle_login()

                elif choice == "2":

                    if not current_user:

                        logger.warning(
                            "Calculation attempted "
                            "without login."
                        )

                        print(
                            "Please login first."
                        )

                        continue

                    handle_calculation()

                elif choice == "3":

                    if not current_user:

                        logger.warning(
                            "File read attempted "
                            "without login."
                        )

                        print(
                            "Please login first."
                        )

                        continue

                    handle_read_file()

                elif choice == "4":

                    if not current_user:

                        logger.warning(
                            "File write attempted "
                            "without login."
                        )

                        print(
                            "Please login first."
                        )

                        continue

                    handle_write_file()

                elif choice == "5":

                    if not current_user:

                        logger.warning(
                            "Logout attempted "
                            "without active user."
                        )

                        print(
                            "No user is logged in."
                        )

                        continue

                    logout(
                        current_user,
                        logger
                    )

                    print(
                        "Logout successful!"
                    )

                    current_user = None

                elif choice == "6":

                    if current_user:

                        logout(
                            current_user,
                            logger
                        )

                    logger.info(
                        "Application closed normally."
                    )

                    print(
                        "Application closed."
                    )

                    break

                else:

                    logger.warning(
                        "Invalid menu option: %s",
                        choice
                    )

                    print(
                        "Invalid choice."
                    )

            except AuthenticationError as error:

                print(
                    "Login Error:",
                    error
                )

            except CalculationError as error:

                print(
                    "Calculation Error:",
                    error
                )

            except FileOperationError as error:

                print(
                    "File Error:",
                    error
                )

            except ApplicationLoggerError as error:

                logger.error(
                    "Application operation failed: %s",
                    error
                )

                print(
                    "Error:",
                    error
                )

            except Exception as error:

                logger.critical(
                    "Unexpected application failure: %s",
                    error,
                    exc_info=True
                )

                print(
                    "Unexpected error occurred, "
                    "but the application will continue."
                )

    except KeyboardInterrupt:

        logger.critical(
            "Application interrupted unexpectedly "
            "by the user."
        )

        print(
            "\nApplication interrupted."
        )

    except Exception as error:

        logger.critical(
            "Critical application failure: %s",
            error,
            exc_info=True
        )

        print(
            "A critical application error occurred."
        )

    finally:

        logger.debug(
            "Application cleanup completed."
        )


if __name__ == "__main__":
    run_application()