from task_manager.exceptions import (
    InvalidTaskError,
    StorageError,
    TaskNotFoundError
)

from task_manager.logger_config import (
    setup_logger
)

from task_manager.manager import (
    add_task,
    delete_task,
    mark_task_complete,
    show_statistics,
    update_task,
    view_tasks
)

from task_manager.storage import load_tasks


logger = setup_logger()


def get_task_id():
    """Accept and validate task ID."""

    try:
        return int(
            input("Enter task ID: ")
        )

    except ValueError:
        raise InvalidTaskError(
            "Task ID must be a number."
        )


def show_menu():
    """Display main application menu."""

    print(
        "\n=== DAILY TASK MANAGER ==="
    )

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. View Statistics")
    print("7. Exit")


def run_application():
    """Run Daily Task Manager."""

    try:

        tasks = load_tasks()

        logger.info(
            "Application started."
        )

    except StorageError as error:

        print(
            "Unable to load saved tasks:",
            error
        )

        logger.error(
            "Task loading failed: %s",
            error
        )

        tasks = []

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":

                title = input(
                    "Enter task title: "
                )

                description = input(
                    "Enter task description: "
                )

                due_date = input(
                    "Enter due date "
                    "(YYYY-MM-DD or leave empty): "
                ).strip()

                task = add_task(
                    tasks,
                    title,
                    description,
                    due_date
                )

                print(
                    "Task added successfully!"
                )

                logger.info(
                    "Task added: %s",
                    task["title"]
                )

            elif choice == "2":

                view_tasks(tasks)

            elif choice == "3":

                task_id = get_task_id()

                title = input(
                    "Enter new title "
                    "(leave empty to keep current): "
                )

                description = input(
                    "Enter new description "
                    "(leave empty to keep current): "
                )

                due_date = input(
                    "Enter new due date "
                    "(leave empty to keep current): "
                )

                task = update_task(
                    tasks,
                    task_id,
                    title,
                    description,
                    due_date
                )

                print(
                    "Task updated successfully!"
                )

                logger.info(
                    "Task updated: ID %s",
                    task["id"]
                )

            elif choice == "4":

                task_id = get_task_id()

                task = delete_task(
                    tasks,
                    task_id
                )

                print(
                    "Task deleted successfully!"
                )

                logger.info(
                    "Task deleted: %s",
                    task["title"]
                )

            elif choice == "5":

                task_id = get_task_id()

                task = mark_task_complete(
                    tasks,
                    task_id
                )

                print(
                    "Task marked as completed!"
                )

                logger.info(
                    "Task completed: %s",
                    task["title"]
                )

            elif choice == "6":

                show_statistics(tasks)

            elif choice == "7":

                print(
                    "Thank you for using "
                    "Daily Task Manager."
                )

                logger.info(
                    "Application closed."
                )

                break

            else:

                print(
                    "Invalid menu option."
                )

        except (
            InvalidTaskError,
            TaskNotFoundError,
            StorageError
        ) as error:

            print(
                "Error:",
                error
            )

            logger.error(
                "%s",
                error
            )

        except Exception as error:

            print(
                "Unexpected error:",
                error
            )

            logger.exception(
                "Unexpected application error."
            )


if __name__ == "__main__":
    run_application()