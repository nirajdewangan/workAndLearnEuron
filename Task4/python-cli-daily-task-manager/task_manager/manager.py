from datetime import datetime

from task_manager.exceptions import (
    InvalidTaskError,
    TaskNotFoundError
)

from task_manager.storage import save_tasks


def generate_task_id(tasks):
    """Generate a unique task ID."""

    if not tasks:
        return 1

    largest_id = tasks[0]["id"]

    for task in tasks:
        if task["id"] > largest_id:
            largest_id = task["id"]

    return largest_id + 1


def validate_title(title):
    """Validate task title."""

    if not title or not title.strip():
        raise InvalidTaskError(
            "Task title cannot be empty."
        )


def validate_due_date(due_date):
    """Validate date in YYYY-MM-DD format."""

    if not due_date:
        return

    try:
        datetime.strptime(
            due_date,
            "%Y-%m-%d"
        )

    except ValueError:
        raise InvalidTaskError(
            "Due date must use YYYY-MM-DD format."
        )


def add_task(
    tasks,
    title,
    description,
    due_date
):
    """Add a new task."""

    validate_title(title)
    validate_due_date(due_date)

    task = {
        "id": generate_task_id(tasks),
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "status": "Pending"
    }

    tasks.append(task)

    save_tasks(tasks)

    return task


def view_tasks(tasks):
    """Display all tasks."""

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- TASK LIST ---")

    for task in tasks:

        print(
            f"\nID: {task['id']}"
        )

        print(
            f"Title: {task['title']}"
        )

        print(
            f"Description: "
            f"{task['description']}"
        )

        print(
            f"Due Date: "
            f"{task['due_date'] or 'Not set'}"
        )

        print(
            f"Status: {task['status']}"
        )


def find_task(tasks, task_id):
    """Find task using its ID."""

    for task in tasks:

        if task["id"] == task_id:
            return task

    raise TaskNotFoundError(
        f"Task with ID {task_id} was not found."
    )


def update_task(
    tasks,
    task_id,
    new_title,
    new_description,
    new_due_date
):
    """Update an existing task."""

    task = find_task(
        tasks,
        task_id
    )

    if new_title:
        validate_title(new_title)
        task["title"] = new_title.strip()

    if new_description:
        task["description"] = (
            new_description.strip()
        )

    if new_due_date:
        validate_due_date(new_due_date)

        task["due_date"] = new_due_date

    save_tasks(tasks)

    return task


def delete_task(tasks, task_id):
    """Delete task using task ID."""

    task = find_task(
        tasks,
        task_id
    )

    tasks.remove(task)

    save_tasks(tasks)

    return task


def mark_task_complete(
    tasks,
    task_id
):
    """Mark a task as completed."""

    task = find_task(
        tasks,
        task_id
    )

    task["status"] = "Completed"

    save_tasks(tasks)

    return task


def show_statistics(tasks):
    """Display task statistics."""

    total = len(tasks)

    completed = 0
    pending = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1

        else:
            pending += 1

    print("\n--- TASK STATISTICS ---")

    print(
        "Total Tasks:",
        total
    )

    print(
        "Completed:",
        completed
    )

    print(
        "Pending:",
        pending
    )