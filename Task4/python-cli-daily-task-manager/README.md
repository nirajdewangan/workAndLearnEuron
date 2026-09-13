# Daily Task Manager - Python CLI

## Project Overview

Daily Task Manager is a command-line Python application created as part of the Vibe Coding Challenge.

The application allows users to:

- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as completed
- View task statistics
- Save task data using JSON
- Log application activities and errors

## Project Structure

```text
python-cli-daily-task-manager/
│
├── main.py
├── README.md
├── requirements.txt
├── tasks.json
│
├── task_manager/
│   ├── __init__.py
│   ├── manager.py
│   ├── storage.py
│   ├── exceptions.py
│   └── logger_config.py
│
└── logs/
    └── task_manager.log


Vibe Coding Process

I developed this project using AI step-by-step instead of asking AI to generate the complete project in one prompt.

Prompt 1

Understand this requirement for a Python CLI Daily Task Manager. Explain the features I should implement and do not generate the complete code yet.

Prompt 2

Suggest a modular Python project structure for the Daily Task Manager using at least four Python files and one package.

Prompt 3

Help me create only the custom exceptions module for invalid tasks, missing tasks, and storage errors.

Prompt 4

Now help me build the JSON storage module. It should load and save tasks and handle file errors.

Prompt 5

Help me create the task manager module for adding, viewing, updating, deleting and completing tasks.

Prompt 6

My application should not crash if I enter a non-numeric task ID. Help me add exception handling.

Prompt 7

Add logging so successful operations and application errors are stored in a log file.

Prompt 8

Review the modules and suggest how I can reduce duplicate code and improve readability without changing functionality.

Prompt 9

Suggest test cases for valid input, invalid task IDs, missing tasks, incorrect dates and corrupted JSON data.

Prompt 10

Review my final application against these requirements: package, four modules, custom exception, try/except/finally, logging, imports and README.


=== DAILY TASK MANAGER ===

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. View Statistics
7. Exit

Enter your choice: 1

Enter task title: Complete Python project
Enter task description: Complete final assignment
Enter due date: 2026-09-14

Task added successfully!

Enter task ID: abc

Error: Task ID must be a number.



---

# 11. How the vibe-coding process should look

Don't say:

> I asked ChatGPT to create the project.

That works against the assignment.

Instead explain:

> I used AI as a coding assistant and developed the project incrementally. I first understood the requirement, then designed the structure, created modules individually, executed the application, fixed errors, added exception handling and logging, and finally refactored and tested it.

That's exactly what the challenge is testing.

---

# 12. YouTube explanation content

Use this as your speaking script.

:::writing{variant="document" id="69214" title="YouTube Script – Vibe Coding Daily Task Manager"}
# Introduction

Hello everyone.

In this video, I am going to explain my Vibe Coding Challenge project.

For this challenge, I selected a Daily Task Manager and built it as a command-line Python application.

An important requirement of this assignment was that I should not ask AI to generate the entire project using one prompt.

Instead, I used ChatGPT as a coding assistant and developed the application step-by-step.

I first understood the requirements, then planned the package structure, created individual modules, executed the application, handled errors, added logging, refactored the code, and finally tested the complete application.

---

# Features

My Daily Task Manager supports the following features:

Add a task.

View all tasks.

Update a task.

Delete a task.

Mark a task as completed.

View task statistics.

And Exit.

Task data is stored permanently inside a JSON file.

The project also has custom exceptions, error handling and file-based logging.

---

# Project Structure

My project contains a main Python file and a package called `task_manager`.

Inside this package, I have:

`manager.py`

`storage.py`

`exceptions.py`

`logger_config.py`

and `__init__.py`.

The main program is available in `main.py`.

I also have a `tasks.json` file to store task data, a log file, a README, and requirements.txt.

I created separate modules because each part of the program has a different responsibility.

---

# Why a Package?

The `task_manager` directory contains `__init__.py`.

Because of this, Python treats this directory as a package.

I can then import functionality from different modules.

For example, `main.py` imports functions from the manager, storage, logger and exception modules.

This demonstrates modular programming and imports between modules.

---

# Custom Exceptions

In `exceptions.py`, I created custom exceptions.

The first is `TaskManagerError`, which is the base exception.

Then I created:

`TaskNotFoundError`

`InvalidTaskError`

and

`StorageError`.

For example, when a user enters a task ID which does not exist, I raise `TaskNotFoundError`.

Using custom exceptions makes error handling more meaningful than handling everything using a generic Exception.

---

# Storage Module

The `storage.py` module is responsible for reading and writing task information.

I use JSON because it can easily store Python-style structured data.

The `load_tasks()` function reads `tasks.json`.

The `save_tasks()` function writes the updated task list back into the JSON file.

This module also contains `try`, `except`, and `finally`.

The `try` block attempts to save the file.

The `except` block handles operating system or file errors.

The `finally` block executes whether the operation succeeds or fails.

This satisfies the requirement to use try, except and finally.

---

# Task Manager Module

The main business logic is inside `manager.py`.

The `add_task()` function creates a new task.

Each task contains:

ID,

title,

description,

due date,

and status.

The initial status is Pending.

I created `generate_task_id()` so every task gets a unique ID.

The `view_tasks()` function uses a for loop to display the task list.

The `find_task()` function searches for a task using its ID.

If the ID does not exist, it raises `TaskNotFoundError`.

The update function allows existing task information to be changed.

The delete function removes a task.

And the mark-complete function changes the status from Pending to Completed.

---

# Validation

I also added validation.

For example, a task cannot have an empty title.

If the title is empty, I raise `InvalidTaskError`.

Due dates must be entered in YYYY-MM-DD format.

I use Python's `datetime.strptime()` to validate this.

If the format is incorrect, the custom exception is raised.

---

# Logging

The next important requirement is logging.

I created `logger_config.py`.

The program writes logs into:

`logs/task_manager.log`.

For successful actions, I use `logger.info()`.

For known errors, I use `logger.error()`.

And for unexpected exceptions, I use `logger.exception()`.

This means important application events are stored even after the application closes.

---

# Main Application

Now I will explain `main.py`.

The program first loads existing tasks.

Then I use a `while True` loop to continuously display the main menu.

I selected a while loop because I do not know how many operations the user wants to perform.

The program should continue until the user selects Exit.

The user's menu choice is handled using `if`, `elif`, and `else`.

Every menu option calls a function from one of the other modules.

This keeps my main program relatively simple because the actual task logic remains inside the package.

---

# Demo – Add Task

Now I will execute the application.

I select option 1 to add a task.

For example:

Title: Complete Python project.

Description: Complete final submission.

Due date: 2026-09-14.

The application confirms that the task has been added successfully.

It is also saved to `tasks.json`.

---

# Demo – View Tasks

Now I select View Tasks.

The application displays the task ID, title, description, due date and status.

The initial status is Pending.

---

# Demo – Invalid Input

Now I want to demonstrate exception handling.

I select an operation that requires a task ID.

Instead of entering a number, I enter:

`abc`.

Python cannot convert this to an integer.

The application catches this problem and raises `InvalidTaskError`.

Instead of crashing, it displays:

`Task ID must be a number`.

The application then continues running.

---

# Demo – Missing Task

Next, I enter a numeric task ID which does not exist.

The `find_task()` function cannot find that ID and raises `TaskNotFoundError`.

Again, the error is handled and the application continues.

---

# Demo – Invalid Date

I can also demonstrate date validation.

Instead of entering a date in YYYY-MM-DD format, I enter an incorrect date.

The program detects the problem using `datetime.strptime()` and displays an error.

---

# Demo – Mark Complete

Next, I mark one task as completed.

The task status changes from Pending to Completed.

Because data is saved in JSON, this status remains available when I restart the program.

---

# Task Statistics

Option 6 displays statistics.

The program calculates:

Total tasks.

Completed tasks.

And pending tasks.

I use a for loop to go through all tasks and count them based on status.

---

# Logging Demonstration

Now I will open:

`logs/task_manager.log`.

Here we can see entries for adding tasks, updating tasks, completing tasks, deleting tasks and errors.

This confirms that logging is working correctly.

---

# Vibe Coding Process

The main purpose of this challenge was also to demonstrate how I used AI.

I did not provide the entire assignment and ask AI to create everything in one prompt.

My first prompt was only to understand the requirement.

My second prompt was to suggest a modular package structure.

Then I separately asked for the exception module.

After that, I created storage functionality.

Then I implemented the task operations.

After running the code, I focused on error handling.

I then added logging.

After that, I asked AI to review the project and help with refactoring and test cases.

I have included these prompts in my README as required by the assignment.

---

# Challenges Faced

One challenge was maintaining task data after the application closed.

I solved this by storing tasks inside a JSON file.

Another challenge was preventing the application from crashing when users entered invalid task IDs or incorrect dates.

I solved this using custom exceptions and try-except blocks.

Another important learning was separating responsibilities.

Instead of placing everything inside one large Python file, I divided storage, task management, logging and exception handling into individual modules.

---

# What I Learned

Through this challenge, I learned both Python development and how to use AI more effectively as a coding assistant.

Instead of asking AI for a complete solution, I learned to break a problem into smaller tasks.

I also improved my understanding of Python packages, modules, imports, JSON file handling, custom exceptions, try-except-finally, logging and refactoring.

The biggest learning was that AI works better as a development partner when I understand and test each step instead of blindly accepting a complete generated solution.

Thank you.
:::

---

# 13. Test cases to show during video

Run these because they demonstrate most of the marks:

| Test | Input | Expected |
|---|---|---|
| Add task | Valid title/date | Task added |
| Empty title | blank | `InvalidTaskError` |
| Bad date | `14-09-2026` | Date format error |
| Bad ID | `abc` | Task ID must be number |
| Missing ID | `999` | Task not found |
| Complete task | existing ID | Status → Completed |
| Delete task | existing ID | Removed |
| Statistics | several tasks | Counts shown |
| Restart | reopen program | Existing JSON tasks loaded |

One useful improvement before submission: deliberately corrupt `tasks.json` once, run the program to demonstrate `StorageError`, and then restore it to `[]`. This makes your exception-handling explanation much stronger.

The generated thumbnail above is designed specifically for this project: **“AI-Powered Daily Task Manager — Vibe Coding Step-by-Step.”**