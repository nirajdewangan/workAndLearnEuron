import csv

from exceptions import (
    InvalidMarksError,
    MissingStudentInfoError
)

from logging_config import setup_logger

from student_operations import create_student

from result_calculator import calculate_result


logger = setup_logger()


def display_result(result):
    """Display processed student result."""

    print("\n--------------------------------")

    print("Name:", result["name"])
    print("Roll Number:", result["roll_number"])
    print("Marks:", result["marks"])
    print("Total:", result["total"])

    print(
        "Percentage:",
        f"{result['percentage']:.2f}%"
    )

    print("Grade:", result["grade"])
    print("Status:", result["status"])


def process_student(row):
    """Process one student row."""

    name = row.get("name", "")
    roll_number = row.get("roll_number", "")

    marks = [
        row.get("subject1"),
        row.get("subject2"),
        row.get("subject3"),
        row.get("subject4"),
        row.get("subject5")
    ]

    student = create_student(
        name,
        roll_number,
        marks
    )

    result = calculate_result(student)

    return result


def process_students(file_name):
    """Process all students without stopping on errors."""

    try:

        with open(
            file_name,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                student_name = row.get(
                    "name",
                    "Unknown Student"
                )

                try:

                    result = process_student(row)

                    display_result(result)

                    logger.info(
                        "Successfully processed student: %s",
                        result["name"]
                    )

                except InvalidMarksError as error:

                    print(
                        f"\nSkipping {student_name}: "
                        f"{error}"
                    )

                    logger.error(
                        "Invalid marks for student %s: %s",
                        student_name,
                        error
                    )

                except MissingStudentInfoError as error:

                    print(
                        f"\nSkipping student: {error}"
                    )

                    logger.error(
                        "Missing student information: %s",
                        error
                    )

                except ZeroDivisionError as error:

                    print(
                        f"\nCalculation error for "
                        f"{student_name}: {error}"
                    )

                    logger.exception(
                        "Calculation error for student %s",
                        student_name
                    )

                except Exception as error:

                    print(
                        f"\nUnexpected error for "
                        f"{student_name}: {error}"
                    )

                    logger.exception(
                        "Unexpected error for student %s",
                        student_name
                    )

    except FileNotFoundError:

        print(
            f"Input file '{file_name}' was not found."
        )

        logger.exception(
            "Student input file not found."
        )

    except PermissionError:

        print(
            f"Permission denied while reading "
            f"'{file_name}'."
        )

        logger.exception(
            "Permission error while opening input file."
        )


def main():
    """Start Fault-Tolerant Student Result Processor."""

    print(
        "=== Fault-Tolerant Student "
        "Result Processor ==="
    )

    process_students("students.csv")

    print("\nProcessing completed.")


if __name__ == "__main__":
    main()