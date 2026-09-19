"""An online learning platform modeled with Python inheritance."""


class Course:
    """Represent a regular online course."""

    course_count = 0

    def __init__(self, course_name, instructor, duration, price):
        if price <= 0:
            raise ValueError("Course price must be greater than zero.")

        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = float(price)
        Course.course_count += 1

    def show_course_details(self):
        """Display the common details of a course."""
        print(f"Course Name : {self.course_name}")
        print(f"Instructor  : {self.instructor}")
        print(f"Duration    : {self.duration}")
        print(f"Price       : Rs. {self.price:.2f}")

    def calculate_discount(self, discount_percentage):
        """Return the course price after applying a valid discount."""
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = self.price * discount_percentage / 100
        return self.price - discount_amount

    @classmethod
    def get_course_count(cls):
        """Return the total number of regular and premium courses created."""
        return Course.course_count


class PremiumCourse(Course):
    """Represent a premium course with additional learning support."""

    def __init__(
        self,
        course_name,
        instructor,
        duration,
        price,
        mentor_support,
        live_sessions,
    ):
        super().__init__(course_name, instructor, duration, price)
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        """Display inherited course details and premium features."""
        super().show_course_details()
        print(f"Mentor Support : {self.mentor_support}")
        print(f"Live Sessions  : {self.live_sessions}")


def main():
    """Create regular and premium courses and demonstrate their features."""
    course1 = Course(
        "Python Fundamentals",
        "Anita Sharma",
        "6 weeks",
        4000,
    )

    course2 = Course(
        "Web Development Basics",
        "Rahul Verma",
        "8 weeks",
        6000,
    )

    premium_course1 = PremiumCourse(
        "Full Stack Development",
        "Vikram Singh",
        "16 weeks",
        18000,
        "Dedicated mentor",
        12,
    )

    premium_course2 = PremiumCourse(
        "Data Science Mastery",
        "Priya Mehta",
        "20 weeks",
        25000,
        "One-to-one mentor",
        16,
    )

    courses = [course1, course2, premium_course1, premium_course2]

    print("ONLINE LEARNING PLATFORM")

    for course in courses:
        print(f"\n--- {course.__class__.__name__} Details ---")
        course.show_course_details()

    print("\n--- Discount Demonstration ---")
    regular_price = course1.calculate_discount(10)
    premium_price = premium_course1.calculate_discount(20)
    print(f"Python Fundamentals after 10% discount: Rs. {regular_price:.2f}")
    print(f"Full Stack Development after 20% discount: Rs. {premium_price:.2f}")

    print(f"\nTotal courses created: {Course.get_course_count()}")


if __name__ == "__main__":
    main()
