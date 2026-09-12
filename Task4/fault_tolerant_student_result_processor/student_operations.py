from exceptions import InvalidMarksError, MissingStudentInfoError


SUBJECT_COUNT = 5


def validate_student_info(name, roll_number):
    """Validate required student information."""

    if not name or not name.strip():
        raise MissingStudentInfoError(
            "Student name is missing."
        )

    if not roll_number or not roll_number.strip():
        raise MissingStudentInfoError(
            "Student roll number is missing."
        )


def validate_mark(mark):
    """Convert and validate a student mark."""

    try:
        numeric_mark = float(mark)

    except (ValueError, TypeError):
        raise InvalidMarksError(
            f"Non-numeric mark received: {mark}"
        )

    if numeric_mark < 0 or numeric_mark > 100:
        raise InvalidMarksError(
            f"Mark {numeric_mark} must be between 0 and 100."
        )

    return numeric_mark


def validate_marks(marks):
    """Validate marks for exactly five subjects."""

    if len(marks) != SUBJECT_COUNT:
        raise InvalidMarksError(
            f"Exactly {SUBJECT_COUNT} subject marks are required."
        )

    validated_marks = []

    for mark in marks:
        validated_mark = validate_mark(mark)
        validated_marks.append(validated_mark)

    return validated_marks


def create_student(name, roll_number, marks):
    """Validate and create a student dictionary."""

    validate_student_info(name, roll_number)

    validated_marks = validate_marks(marks)

    student = {
        "name": name.strip(),
        "roll_number": roll_number.strip(),
        "marks": validated_marks
    }

    return student