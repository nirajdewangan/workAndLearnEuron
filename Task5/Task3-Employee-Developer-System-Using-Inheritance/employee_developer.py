"""Employee and Developer system demonstrating Python inheritance."""


class Employee:
    """Represent a general employee."""

    def __init__(self, employee_id, name, salary, department):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.employee_id = employee_id
        self.name = name
        self.salary = float(salary)
        self.department = department

    def display_details(self):
        """Display the common details of an employee."""
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : Rs. {self.salary:.2f}")
        print(f"Department  : {self.department}")


class Developer(Employee):
    """Represent a developer who inherits from Employee."""

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience,
    ):
        super().__init__(employee_id, name, salary, department)

        if experience < 0:
            raise ValueError("Experience cannot be negative.")

        self.programming_language = programming_language
        self.experience = experience

    def display_details(self):
        """Display inherited employee details and developer-specific details."""
        super().display_details()
        print(f"Language    : {self.programming_language}")
        print(f"Experience  : {self.experience} years")


def main():
    """Create Employee and Developer objects and display their details."""
    employee1 = Employee("EMP101", "Ananya Singh", 50000, "Human Resources")

    developer1 = Developer(
        "DEV201",
        "Aarav Sharma",
        75000,
        "Engineering",
        "Python",
        3,
    )

    developer2 = Developer(
        "DEV202",
        "Diya Verma",
        90000,
        "Product Development",
        "JavaScript",
        5,
    )

    team_members = [employee1, developer1, developer2]

    print("EMPLOYEE AND DEVELOPER SYSTEM")
    print(f"Total objects created: {len(team_members)}")

    for member in team_members:
        print(f"\n--- {member.__class__.__name__} Details ---")
        member.display_details()


if __name__ == "__main__":
    main()
