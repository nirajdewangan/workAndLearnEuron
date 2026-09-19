"""A mini Super30 Learning Platform demonstrating core Python OOP concepts."""


class User:
    """Represent a general user of the learning platform."""

    total_users = 0

    def __init__(self, name, email, user_id):
        if not self.is_valid_email(email):
            raise ValueError("Please provide a valid email address.")

        self.name = name
        self.email = email
        self.user_id = user_id
        User.total_users += 1

    def display_user_info(self):
        """Display information shared by all users."""
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")

    @classmethod
    def get_total_users(cls):
        """Return the total number of Student and Mentor objects created."""
        return User.total_users

    @staticmethod
    def is_valid_email(email):
        """Return True when an email has a simple valid structure."""
        if not isinstance(email, str) or email.count("@") != 1:
            return False

        local_part, domain = email.split("@")
        return bool(local_part) and "." in domain and not domain.startswith(".")


class Student(User):
    """Represent a student enrolled on the learning platform."""

    def __init__(self, name, email, user_id, course_name="Not Assigned"):
        super().__init__(name, email, user_id)
        self.course_name = course_name
        self.completed_assignments = []

    def assign_course(self, course_name):
        """Assign a non-empty course to the student."""
        if not isinstance(course_name, str) or not course_name.strip():
            print("Course assignment failed: Course name cannot be empty.")
            return False

        self.course_name = course_name.strip()
        print(f"{self.course_name} assigned to {self.name}.")
        return True

    def submit_assignment(self, assignment_name):
        """Record a completed assignment when it has not been submitted before."""
        if not isinstance(assignment_name, str) or not assignment_name.strip():
            print("Submission failed: Assignment name cannot be empty.")
            return False

        assignment_name = assignment_name.strip()
        if assignment_name in self.completed_assignments:
            print(f"{assignment_name} was already submitted by {self.name}.")
            return False

        self.completed_assignments.append(assignment_name)
        print(f"{self.name} submitted {assignment_name}.")
        return True

    def display_student_info(self):
        """Display inherited user details and student-specific information."""
        super().display_user_info()
        print(f"Course  : {self.course_name}")
        print(f"Completed Assignments: {len(self.completed_assignments)}")

        if self.completed_assignments:
            print(f"Assignment List      : {', '.join(self.completed_assignments)}")
        else:
            print("Assignment List      : None")


class Mentor(User):
    """Represent a mentor who supports assigned students."""

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.assigned_students = []
        self.number_of_students_assigned = 0

    def assign_student(self, student):
        """Assign a valid Student object to this mentor."""
        if not isinstance(student, Student):
            print("Student assignment failed: A Student object is required.")
            return False

        if student in self.assigned_students:
            print(f"{student.name} is already assigned to {self.name}.")
            return False

        self.assigned_students.append(student)
        self.number_of_students_assigned = len(self.assigned_students)
        print(f"{student.name} assigned to mentor {self.name}.")
        return True

    def display_mentor_info(self):
        """Display inherited user details and mentor-specific information."""
        super().display_user_info()
        print(f"Expertise         : {self.expertise}")
        print(f"Students Assigned : {self.number_of_students_assigned}")

        if self.assigned_students:
            student_names = [student.name for student in self.assigned_students]
            print(f"Student List      : {', '.join(student_names)}")
        else:
            print("Student List      : None")


def main():
    """Demonstrate the complete Super30 Learning Platform."""
    student1 = Student("Aarav Sharma", "aarav@example.com", "STU101")
    student2 = Student("Diya Verma", "diya@example.com", "STU102")
    student3 = Student("Rohan Gupta", "rohan@example.com", "STU103")

    mentor1 = Mentor("Neha Singh", "neha@example.com", "MEN201", "Python")
    mentor2 = Mentor("Kabir Mehta", "kabir@example.com", "MEN202", "Web Development")

    print("SUPER30 LEARNING PLATFORM")

    print("\n--- Assigning Courses ---")
    student1.assign_course("Python Backend Development")
    student2.assign_course("Full Stack Web Development")
    student3.assign_course("Data Science Fundamentals")

    print("\n--- Submitting Assignments ---")
    student1.submit_assignment("Python OOP Assignment")
    student1.submit_assignment("File Handling Assignment")
    student2.submit_assignment("HTML and CSS Project")
    student3.submit_assignment("Data Analysis Assignment")

    print("\n--- Assigning Students to Mentors ---")
    mentor1.assign_student(student1)
    mentor1.assign_student(student3)
    mentor2.assign_student(student2)

    print("\n--- Student Information ---")
    for student in [student1, student2, student3]:
        print("\nStudent Details")
        student.display_student_info()

    print("\n--- Mentor Information ---")
    for mentor in [mentor1, mentor2]:
        print("\nMentor Details")
        mentor.display_mentor_info()

    print("\n--- Static Method Demonstration ---")
    print(f"Is learner@example.com valid? {User.is_valid_email('learner@example.com')}")
    print(f"Is learner.example.com valid? {User.is_valid_email('learner.example.com')}")

    print(f"\nTotal registered users: {User.get_total_users()}")


if __name__ == "__main__":
    main()
