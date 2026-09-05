# ============================================================
# 1. STUDENT RESULT MANAGEMENT SYSTEM
# ============================================================

def accept_marks():
    """Accept marks for five subjects and return them as a list."""
    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    return marks


def calculate_total(marks):
    """Calculate and return total marks."""
    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_percentage(total, number_of_subjects):
    """Calculate and return percentage."""
    return total / number_of_subjects


def assign_grade(percentage):
    """Return grade based on percentage."""
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


def determine_result(marks):
    """Return Pass if all marks are at least 35, otherwise Fail."""
    for mark in marks:
        if mark < 35:
            return "Fail"

    return "Pass"


def display_student_result():
    """Run the Student Result Management System."""
    print("\n--- STUDENT RESULT MANAGEMENT SYSTEM ---")

    marks = accept_marks()
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = assign_grade(percentage)
    result = determine_result(marks)

    print("\nMarks:", marks)
    print("Total:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)

display_student_result()