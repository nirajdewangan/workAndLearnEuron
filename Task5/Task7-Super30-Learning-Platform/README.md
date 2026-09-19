# Super30 Learning Platform

A mini online learning platform combining the main Python OOP concepts covered in the Super30 assignments.

## Required Concepts Covered

| Requirement | Implementation |
| --- | --- |
| Parent class | `User` |
| Child classes | `Student` and `Mentor` |
| Inheritance | `Student(User)` and `Mentor(User)` |
| Constructors | `__init__()` in all three classes |
| Class variable | `User.total_users` |
| Class method | `User.get_total_users()` |
| Static method | `User.is_valid_email()` |
| Instance methods | Course, assignment, mentor, and display methods |
| Multiple objects | Three students and two mentors |

## Features

- Register students and mentors through object creation
- Validate email addresses
- Assign courses to students
- Submit and track completed assignments
- Assign students to mentors
- Display complete student information
- Display complete mentor information
- Count all registered users
- Prevent duplicate assignment submissions and mentor allocations

## Project Structure

```text
super30-learning-platform/
├── super30_platform.py
├── README.md
├── YOUTUBE_SCRIPT.md
├── sample_output.txt
└── youtube-thumbnail.png
```

## How to Run

Open a terminal in this folder and run:

```bash
python super30_platform.py
```

On some systems, use:

```bash
python3 super30_platform.py
```

## Class Structure

```text
User
  |-- Student
  |-- Mentor
```

## Author

Niraj Kumar Dewangan
