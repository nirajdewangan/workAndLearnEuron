# Employee & Developer System Using Inheritance

A beginner-friendly Python project demonstrating inheritance with an `Employee` parent class and a `Developer` child class.

## Requirements Covered

- Base class named `Employee`
- Employee ID, name, salary, and department attributes
- `display_details()` method
- Child class named `Developer`
- `Developer` inherits from `Employee`
- Programming language and experience attributes
- Three objects: one `Employee` and two `Developer` objects
- Child class accesses parent functionality with `super()`

## Additional Validation

- Salary cannot be negative
- Experience cannot be negative

## Project Structure

```text
employee-developer-inheritance/
├── employee_developer.py
├── README.md
├── YOUTUBE_SCRIPT.md
├── sample_output.txt
└── youtube-thumbnail.png
```

## How to Run

Open a terminal in this folder and run:

```bash
python employee_developer.py
```

On some systems, use:

```bash
python3 employee_developer.py
```

## Inheritance Structure

```text
Employee
   |
Developer
```

The `Developer` class uses `super().__init__()` to initialize inherited employee attributes. Its `display_details()` method uses `super().display_details()` before showing developer-specific information.

## Author

Niraj Kumar Dewangan
