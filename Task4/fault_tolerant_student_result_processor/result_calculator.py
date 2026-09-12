def calculate_total(marks):
    """Calculate total marks."""

    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_percentage(total, subject_count):
    """Calculate percentage."""

    if subject_count == 0:
        raise ZeroDivisionError(
            "Cannot calculate percentage with zero subjects."
        )

    return total / subject_count


def assign_grade(percentage):
    """Assign grade based on percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def determine_status(marks):
    """Determine Pass or Fail status."""

    for mark in marks:

        if mark < 35:
            return "Fail"

    return "Pass"


def calculate_result(student):
    """Calculate complete student result."""

    marks = student["marks"]

    total = calculate_total(marks)

    percentage = calculate_percentage(
        total,
        len(marks)
    )

    grade = assign_grade(percentage)

    status = determine_status(marks)

    return {
        "name": student["name"],
        "roll_number": student["roll_number"],
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }