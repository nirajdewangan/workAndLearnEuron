# Advanced Function Challenges
# Super30 Python Functions Task 2


# ==================================================
# Question 1
# *args - Accept any number of values and return total
# ==================================================

def total_numbers(*args):
    """Return the total of any number of supplied values."""
    total = 0

    for number in args:
        total += number

    return total


print("Total:", total_numbers(10, 20, 30, 40))


# ==================================================
# Question 2
# *args - Return largest supplied number
# ==================================================

def largest_number(*args):
    """Return the largest supplied number without using max()."""

    if len(args) == 0:
        return None

    largest = args[0]

    for number in args:
        if number > largest:
            largest = number

    return largest


print("Largest Number:", largest_number(10, 45, 23, 89, 34))


# ==================================================
# Question 3
# **kwargs - Dynamic Profile
# ==================================================

def create_profile(**kwargs):
    """Print dynamically supplied profile information."""

    print("\nUser Profile:")

    for key, value in kwargs.items():
        print(key, ":", value)


create_profile(
    name="Niraj",
    age=36,
    city="Bengaluru",
    course="Python"
)


# ==================================================
# Question 4
# Function as an argument
# ==================================================

def add(a, b):
    """Return addition of two numbers."""
    return a + b


def multiply(a, b):
    """Return multiplication of two numbers."""
    return a * b


def calculate(operation, a, b):
    """Accept another function and execute it."""
    return operation(a, b)


print("\nCalculate with add:", calculate(add, 10, 20))
print("Calculate with multiply:", calculate(multiply, 10, 20))


# ==================================================
# Question 5
# Lambda function to square a number
# ==================================================

square = lambda number: number * number

print("\nSquare of 5:", square(5))


# ==================================================
# Question 6
# Lambda with map()
# ==================================================

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = list(
    map(lambda number: number * number, numbers)
)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)


# ==================================================
# Question 7
# Lambda with filter()
# ==================================================

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("Even Numbers:", even_numbers)


# ==================================================
# Question 8
# Recursive Factorial
# ==================================================

def recursive_factorial(number):
    """Return factorial using recursion."""

    if number < 0:
        return "Factorial is not defined for negative numbers."

    # Base case
    if number == 0 or number == 1:
        return 1

    # Recursive case
    return number * recursive_factorial(number - 1)


print("\nRecursive Factorial of 5:", recursive_factorial(5))


# ==================================================
# Question 9
# Recursive Sum: 1 + 2 + ... + n
# ==================================================

def recursive_sum(number):
    """Return the sum from 1 to number using recursion."""

    if number <= 0:
        return 0

    # Base case
    if number == 1:
        return 1

    # Recursive case
    return number + recursive_sum(number - 1)


print("Recursive Sum from 1 to 5:", recursive_sum(5))


# ==================================================
# Question 10
# Recursive Fibonacci - nth Fibonacci number
# ==================================================

def fibonacci(number):
    """Return the nth Fibonacci number using recursion."""

    if number < 0:
        return "Fibonacci is not defined for negative numbers."

    # Base cases
    if number == 0:
        return 0

    if number == 1:
        return 1

    # Recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


print("Fibonacci position 7:", fibonacci(7))


# ==================================================
# Question 11
# Local and Global Scope
# ==================================================

global_message = "I am a global variable"


def demonstrate_scope():
    """Demonstrate local and global variable scope."""

    local_message = "I am a local variable"

    print("\nInside Function:")
    print("Global Variable:", global_message)
    print("Local Variable:", local_message)


demonstrate_scope()

print("\nOutside Function:")
print("Global Variable:", global_message)

# local_message cannot be used here because it is local
# print(local_message)


# ==================================================
# Question 12
# Mini Calculator
# Every operation is a separate function
# ==================================================

def calculator_add(a, b):
    """Return addition of two numbers."""
    return a + b


def calculator_subtract(a, b):
    """Return subtraction of two numbers."""
    return a - b


def calculator_multiply(a, b):
    """Return multiplication of two numbers."""
    return a * b


def calculator_divide(a, b):
    """Return division result or an error message."""

    if b == 0:
        return "Cannot divide by zero."

    return a / b


def main():
    """Control the mini calculator program."""

    while True:

        print("\n--- MINI CALCULATOR ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == "1":
            result = calculator_add(
                first_number,
                second_number
            )

        elif choice == "2":
            result = calculator_subtract(
                first_number,
                second_number
            )

        elif choice == "3":
            result = calculator_multiply(
                first_number,
                second_number
            )

        else:
            result = calculator_divide(
                first_number,
                second_number
            )

        print("Result:", result)


# Call the main calculator function
main()


print("\nAll Advanced Function Challenges Completed!")