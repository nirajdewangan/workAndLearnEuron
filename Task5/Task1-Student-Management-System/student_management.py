"""A simple Student Management System using Python OOP."""


class Student:
    """Store and manage a student's academic details."""

    total_students = 0

    def __init__(self, name, email, student_id, course, marks):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = list(marks)
        Student.total_students += 1

    def display_details(self):
        """Display all details of the student."""
        print("\n--- Student Details ---")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Student ID : {self.student_id}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.marks}")
        print(f"Average    : {self.calculate_average():.2f}")

    def update_marks(self, subject_index, new_mark):
        """Update a mark using its position in the marks list."""
        if not 0 <= subject_index < len(self.marks):
            print("Invalid subject index. Marks were not updated.")
            return

        if not 0 <= new_mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        self.marks[subject_index] = new_mark
        print(f"Marks updated successfully for {self.name}.")

    def calculate_average(self):
        """Calculate and return the student's average marks."""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    @classmethod
    def get_total_students(cls):
        """Return the total number of Student objects created."""
        return cls.total_students


def main():
    """Create student objects and demonstrate the system."""
    student1 = Student(
        "Aarav Sharma",
        "aarav@example.com",
        "STU101",
        "Python Programming",
        [85, 90, 78],
    )

    student2 = Student(
        "Diya Verma",
        "diya@example.com",
        "STU102",
        "Data Science",
        [92, 88, 95],
    )

    student3 = Student(
        "Rohan Gupta",
        "rohan@example.com",
        "STU103",
        "Web Development",
        [75, 82, 80],
    )

    students = [student1, student2, student3]

    print("STUDENT MANAGEMENT SYSTEM")
    for student in students:
        student.display_details()

    print("\n--- Updating Marks ---")
    student1.update_marks(2, 88)
    student1.display_details()

    print(f"\nTotal number of students: {Student.get_total_students()}")


if __name__ == "__main__":
    main()
