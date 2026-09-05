# ============================================================
# 12. SUPER30 PYTHON UTILITY APPLICATION
# ============================================================

def utility_add(a, b):
    """Return addition result."""
    return a + b


def utility_calculator():
    """Simple calculator utility."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Result:", utility_add(a, b))


def utility_palindrome(text):
    """Return True if text is palindrome."""
    reversed_text = ""

    for character in text.lower():
        reversed_text = character + reversed_text

    return text.lower() == reversed_text


def utility_factorial(number):
    """Return factorial using loop."""
    if number < 0:
        return None

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


def utility_multiplication_table(number):
    """Display multiplication table."""
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


def utility_number_analyzer(number):
    """Return even/odd and positive/negative information."""
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    return parity, sign

def is_prime(number):
    """Return True if number is prime."""
    if number <= 1:
        return False

    divisor = 2

    while divisor * divisor <= number:

        if number % divisor == 0:
            return False

        divisor += 1

    return True

def check_password_strength(password):
    """Check password requirements and return a meaningful result."""

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"

    for character in password:

        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

        elif character.isdigit():
            has_number = True

        elif character in special_characters:
            has_special = True

    has_minimum_length = len(password) >= 8

    missing = []

    if not has_uppercase:
        missing.append("uppercase letter")

    if not has_lowercase:
        missing.append("lowercase letter")

    if not has_number:
        missing.append("number")

    if not has_special:
        missing.append("special character")

    if not has_minimum_length:
        missing.append("minimum 8 characters")

    if len(missing) == 0:
        return "Strong Password"

    return "Weak Password. Missing: " + ", ".join(missing)


def password_strength_checker():
    """Run Password Strength Checker."""
    password = input("Enter password: ")

    print(check_password_strength(password))


def super30_utility_application():
    """Run Super30 Python Utility Application."""

    while True:
        print("\n--- SUPER30 PYTHON UTILITY APPLICATION ---")
        print("1. Calculator")
        print("2. Palindrome Checker")
        print("3. Prime Checker")
        print("4. Factorial Calculator")
        print("5. Multiplication Table")
        print("6. Number Analyzer")
        print("7. Password Strength Checker")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            utility_calculator()

        elif choice == "2":
            text = input("Enter text: ")

            if utility_palindrome(text):
                print("Palindrome")
            else:
                print("Not a palindrome")

        elif choice == "3":
            number = int(input("Enter number: "))

            if is_prime(number):
                print("Prime Number")
            else:
                print("Not a Prime Number")

        elif choice == "4":
            number = int(input("Enter number: "))

            result = utility_factorial(number)

            if result is None:
                print("Factorial not defined for negative numbers.")
            else:
                print("Factorial:", result)

        elif choice == "5":
            number = int(input("Enter number: "))
            utility_multiplication_table(number)

        elif choice == "6":
            number = int(input("Enter number: "))

            parity, sign = utility_number_analyzer(number)

            print("Parity:", parity)
            print("Sign:", sign)

        elif choice == "7":
            password_strength_checker()

        elif choice == "8":
            print("Exiting Utility Application.")
            break

        else:
            print("Invalid choice.")
super30_utility_application()
