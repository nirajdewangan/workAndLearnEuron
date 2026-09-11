# ============================================================
# 1. STUDENT RESULT MANAGEMENT SYSTEM
# ============================================================

def get_valid_mark(prompt):
    """Keep asking until the user enters a numeric mark from 0 to 100."""
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
            # return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def accept_marks():
    """Accept valid marks for five subjects and return them as a list."""
    marks = []

    for i in range(1, 6):
        marks.append(get_valid_mark(f"Enter marks for subject {i} (0-100): "))

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
if __name__ == "__main__":
    display_student_result()