# Course & Premium Course System

A beginner-friendly online learning platform modeled using Python inheritance.

## Requirements Covered

- Parent class named `Course`
- Course name, instructor, duration, and price attributes
- `show_course_details()` method
- `calculate_discount()` method
- Child class named `PremiumCourse`
- `PremiumCourse` inherits from `Course`
- Mentor support and live sessions attributes
- Class variable `course_count`
- Class method `get_course_count()`
- Regular and premium course objects

## Inheritance Demonstration

- `PremiumCourse` calls `super().__init__()` to initialize Course attributes.
- It overrides `show_course_details()` and calls the parent version with `super()`.
- It directly inherits `calculate_discount()` from `Course`.
- Both Course and PremiumCourse objects increase the same course counter.

## Project Structure

```text
course-premium-course-system/
├── course_system.py
├── README.md
├── YOUTUBE_SCRIPT.md
├── sample_output.txt
└── youtube-thumbnail.png
```

## How to Run

Open a terminal in this folder and run:

```bash
python course_system.py
```

On some systems, use:

```bash
python3 course_system.py
```

## Inheritance Structure

```text
Course
  |
PremiumCourse
```

## Author

Niraj Kumar Dewangan
