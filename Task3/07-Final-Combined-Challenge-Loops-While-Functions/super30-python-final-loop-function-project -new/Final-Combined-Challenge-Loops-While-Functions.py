# ============================================================
# Final Combined Challenge: Loops + While + Functions
# Super30 Python Final Loop & Function Project
# ============================================================


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


# ============================================================
# 2. BANKING APPLICATION
# ============================================================

def bank_check_balance(balance):
    """Display current bank balance."""
    print("Current Balance: ₹", balance)


def bank_deposit(balance, history):
    """Deposit money and return updated balance."""
    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Invalid deposit amount.")
        return balance

    balance += amount
    history.append(f"Deposited ₹{amount}")

    print("Deposit successful.")
    return balance


def bank_withdraw(balance, history):
    """Withdraw money and return updated balance."""
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        history.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful.")

    return balance


def show_transaction_history(history):
    """Display banking transaction history."""
    if len(history) == 0:
        print("No transactions available.")
        return

    print("\nTransaction History:")

    for transaction in history:
        print("-", transaction)


def banking_application():
    """Run menu-driven banking application."""
    balance = 10000
    history = []

    while True:
        print("\n--- BANKING APPLICATION ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            bank_check_balance(balance)

        elif choice == "2":
            balance = bank_deposit(balance, history)

        elif choice == "3":
            balance = bank_withdraw(balance, history)

        elif choice == "4":
            show_transaction_history(history)

        elif choice == "5":
            print("Exiting Banking Application.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# 3. INVENTORY MANAGEMENT
# ============================================================

def add_inventory_product(products):
    """Add a product to inventory."""
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products[name] = {
        "price": price,
        "quantity": quantity
    }

    print("Product added successfully.")


def display_inventory(products):
    """Display all inventory products."""
    if len(products) == 0:
        print("Inventory is empty.")
        return

    print("\nInventory:")

    for name, details in products.items():
        print(
            name,
            "- Price: ₹",
            details["price"],
            "- Quantity:",
            details["quantity"]
        )


def search_inventory_product(products):
    """Search for a product by name."""
    name = input("Enter product name to search: ")

    if name in products:
        print(name, products[name])
    else:
        print("Product not found.")


def update_inventory_quantity(products):
    """Update quantity of an existing product."""
    name = input("Enter product name: ")

    if name not in products:
        print("Product not found.")
        return

    quantity = int(input("Enter new quantity: "))
    products[name]["quantity"] = quantity

    print("Quantity updated.")


def calculate_inventory_value(products):
    """Calculate total value of inventory."""
    total = 0

    for details in products.values():
        total += details["price"] * details["quantity"]

    return total


def inventory_management():
    """Run inventory management application."""
    products = {}

    while True:
        print("\n--- INVENTORY MANAGEMENT ---")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Total Inventory Value")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_inventory_product(products)

        elif choice == "2":
            display_inventory(products)

        elif choice == "3":
            search_inventory_product(products)

        elif choice == "4":
            update_inventory_quantity(products)

        elif choice == "5":
            print(
                "Total Inventory Value: ₹",
                calculate_inventory_value(products)
            )

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


# ============================================================
# 4. QUIZ APPLICATION
# ============================================================

def quiz_application():
    """Run a five-question Python quiz."""

    questions = [
        {
            "question": "Which keyword is used to create a function?",
            "answer": "def"
        },
        {
            "question": "Which loop is condition controlled?",
            "answer": "while"
        },
        {
            "question": "Which function gives the length of a list?",
            "answer": "len"
        },
        {
            "question": "Which keyword immediately exits a loop?",
            "answer": "break"
        },
        {
            "question": "Which symbol starts a Python comment?",
            "answer": "#"
        }
    ]

    score = 0

    print("\n--- PYTHON QUIZ ---")

    for item in questions:
        print("\n", item["question"])

        answer = input("Your answer: ").strip().lower()

        if answer == item["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print("Correct Answer:", item["answer"])

    percentage = score / len(questions) * 100

    print("\nFinal Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")


# ============================================================
# 5. NUMBER ANALYSIS TOOL
# No min(), max(), sum()
# ============================================================

def analyze_numbers(numbers):
    """Analyze a list without min(), max(), or sum()."""

    if len(numbers) == 0:
        return None

    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        total += number

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if number > 0:
            positive_count += 1

        elif number < 0:
            negative_count += 1

    average = total / len(numbers)

    return {
        "largest": largest,
        "smallest": smallest,
        "total": total,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count,
        "positive_count": positive_count,
        "negative_count": negative_count
    }


def number_analysis_tool():
    """Run Number Analysis Tool."""
    numbers = [10, -5, 20, 7, -3, 0, 18, 11]

    result = analyze_numbers(numbers)

    print("\n--- NUMBER ANALYSIS TOOL ---")
    print("Numbers:", numbers)

    for key, value in result.items():
        print(key, ":", value)


# ============================================================
# 6. EMPLOYEE SALARY ANALYZER
# ============================================================

def salary_total(salaries):
    """Calculate total payroll."""
    total = 0

    for salary in salaries:
        total += salary

    return total


def salary_highest(salaries):
    """Return highest salary."""
    highest = salaries[0]

    for salary in salaries:
        if salary > highest:
            highest = salary

    return highest


def salary_lowest(salaries):
    """Return lowest salary."""
    lowest = salaries[0]

    for salary in salaries:
        if salary < lowest:
            lowest = salary

    return lowest


def salaries_above_average(salaries, average):
    """Return salaries above average."""
    result = []

    for salary in salaries:
        if salary > average:
            result.append(salary)

    return result


def employee_salary_analyzer():
    """Run Employee Salary Analyzer."""
    salaries = [35000, 50000, 42000, 75000, 60000, 90000]

    total = salary_total(salaries)
    average = total / len(salaries)
    highest = salary_highest(salaries)
    lowest = salary_lowest(salaries)
    above_average = salaries_above_average(salaries, average)

    print("\n--- EMPLOYEE SALARY ANALYZER ---")
    print("Salaries:", salaries)
    print("Total Payroll:", total)
    print("Average Salary:", average)
    print("Highest Salary:", highest)
    print("Lowest Salary:", lowest)
    print("Above Average Salaries:", above_average)


# ============================================================
# 7. SHOPPING CART
# ============================================================

def cart_add(cart):
    """Add a product to shopping cart."""
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))

    cart.append({
        "name": name,
        "price": price
    })

    print("Product added.")


def cart_remove(cart):
    """Remove a product from shopping cart."""
    name = input("Enter product name to remove: ")

    for product in cart:
        if product["name"].lower() == name.lower():
            cart.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def cart_view(cart):
    """Display shopping cart."""
    if len(cart) == 0:
        print("Cart is empty.")
        return

    print("\nShopping Cart:")

    for product in cart:
        print(product["name"], "- ₹", product["price"])


def calculate_cart_bill(cart):
    """Calculate total cart bill."""
    total = 0

    for product in cart:
        total += product["price"]

    return total


def shopping_cart():
    """Run shopping cart application."""
    cart = []

    while True:
        print("\n--- SHOPPING CART ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cart_add(cart)

        elif choice == "2":
            cart_remove(cart)

        elif choice == "3":
            cart_view(cart)

        elif choice == "4":
            print("Total Bill: ₹", calculate_cart_bill(cart))

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ============================================================
# 8. PASSWORD STRENGTH CHECKER
# ============================================================

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


# ============================================================
# 9. PRIME NUMBER ANALYZER
# ============================================================

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


def find_primes(start, end):
    """Return prime numbers within a range."""
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


def prime_total(primes):
    """Return total of prime numbers."""
    total = 0

    for number in primes:
        total += number

    return total


def largest_prime(primes):
    """Return largest prime without max()."""
    if len(primes) == 0:
        return None

    largest = primes[0]

    for number in primes:
        if number > largest:
            largest = number

    return largest


def prime_number_analyzer():
    """Run Prime Number Analyzer."""
    start = int(input("Enter range start: "))
    end = int(input("Enter range end: "))

    primes = find_primes(start, end)

    print("Prime Numbers:", primes)
    print("Prime Count:", len(primes))
    print("Prime Sum:", prime_total(primes))
    print("Largest Prime:", largest_prime(primes))


# ============================================================
# 10. EXPENSE TRACKER
# ============================================================

def add_expense(expenses):
    """Add a new expense."""
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added.")


def view_expenses(expenses):
    """Display all expenses."""
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(expense["name"], "- ₹", expense["amount"])


def expense_total(expenses):
    """Calculate total expenses."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def highest_expense(expenses):
    """Return highest expense."""
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def expense_tracker():
    """Run Expense Tracker."""
    expenses = []

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Highest Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Total Expenses: ₹", expense_total(expenses))

        elif choice == "4":
            highest = highest_expense(expenses)

            if highest is None:
                print("No expenses recorded.")
            else:
                print(
                    "Highest Expense:",
                    highest["name"],
                    "- ₹",
                    highest["amount"]
                )

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ============================================================
# 11. MINI AUTHENTICATION SYSTEM
# ============================================================

def authenticate(username, password):
    """Check username and password."""
    correct_username = "admin"
    correct_password = "python123"

    return (
        username == correct_username
        and password == correct_password
    )


def login():
    """Allow a maximum of three login attempts."""
    attempts = 0
    maximum_attempts = 3

    while attempts < maximum_attempts:

        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):
            print("Login successful.")
            return True

        attempts += 1

        print("Login failed.")
        print(
            "Attempts remaining:",
            maximum_attempts - attempts
        )

    print("Maximum login attempts reached.")
    return False


def mini_authentication_system():
    """Run authentication system with login and logout."""
    print("\n--- MINI AUTHENTICATION SYSTEM ---")

    logged_in = login()

    if not logged_in:
        return

    while logged_in:
        print("\n1. View Dashboard")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Welcome to the dashboard.")

        elif choice == "2":
            logged_in = False
            print("Logout successful.")

        else:
            print("Invalid choice.")


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


# ============================================================
# MASTER MENU
# Allows each mini-project to run independently
# ============================================================

def main():
    """Control all Final Combined Challenge mini-projects."""

    while True:

        print("\n======================================")
        print(" FINAL COMBINED CHALLENGE")
        print(" Loops + While + Functions")
        print("======================================")

        print("1. Student Result Management System")
        print("2. Banking Application")
        print("3. Inventory Management")
        print("4. Quiz Application")
        print("5. Number Analysis Tool")
        print("6. Employee Salary Analyzer")
        print("7. Shopping Cart")
        print("8. Password Strength Checker")
        print("9. Prime Number Analyzer")
        print("10. Expense Tracker")
        print("11. Mini Authentication System")
        print("12. Super30 Python Utility Application")
        print("13. Exit")

        choice = input("Select a project: ")

        if choice == "1":
            display_student_result()

        elif choice == "2":
            banking_application()

        elif choice == "3":
            inventory_management()

        elif choice == "4":
            quiz_application()

        elif choice == "5":
            number_analysis_tool()

        elif choice == "6":
            employee_salary_analyzer()

        elif choice == "7":
            shopping_cart()

        elif choice == "8":
            password_strength_checker()

        elif choice == "9":
            prime_number_analyzer()

        elif choice == "10":
            expense_tracker()

        elif choice == "11":
            mini_authentication_system()

        elif choice == "12":
            super30_utility_application()

        elif choice == "13":
            print("Final Combined Challenge Completed!")
            break

        else:
            print("Invalid project number.")


# Start program
if __name__ == "__main__":
    main()