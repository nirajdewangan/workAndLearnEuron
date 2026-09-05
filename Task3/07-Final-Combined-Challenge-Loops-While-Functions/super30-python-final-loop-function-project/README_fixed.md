# Super30 Python Final Loop & Function Project

## Project Objective

The objective of this project is to combine Python **for loops, while loops, functions, conditional statements, lists, dictionaries, user input, validation, and reusable programming** into practical mini-applications.

This repository contains **12 independently executable Python programs** created for the **Final Combined Challenge: Loops + While + Functions**.

## Repository Structure

```text
super30-python-final-loop-function-project/
│
├── README.md
├── requirements.txt
├── task_01/
│   ├── student_result_management.py
│   └── sample_output.txt
├── task_02/
│   ├── banking_application.py
│   └── sample_output.txt
├── task_03/
│   ├── inventory_management.py
│   └── sample_output.txt
├── task_04/
│   ├── quiz_application.py
│   └── sample_output.txt
├── task_05/
│   ├── number_analysis_tool.py
│   └── sample_output.txt
├── task_06/
│   ├── employee_salary_analyzer.py
│   └── sample_output.txt
├── task_07/
│   ├── shopping_cart.py
│   └── sample_output.txt
├── task_08/
│   ├── password_strength_checker.py
│   └── sample_output.txt
├── task_09/
│   ├── prime_number_analyzer.py
│   └── sample_output.txt
├── task_10/
│   ├── expense_tracker.py
│   └── sample_output.txt
├── task_11/
│   ├── authentication_system.py
│   └── sample_output.txt
└── task_12/
    ├── super30_utility_application.py
    └── sample_output.txt
```

## Requirements

- Python 3.10 or later recommended
- No external Python packages are required
- Only Python built-in features and standard library functionality are used

## How to Run

Open Terminal, move into the project folder, and run any task using Python:

```bash
cd super30-python-final-loop-function-project
python3 task_01/student_result_management.py
```

Replace the task path with the program you want to execute.

---

## Task 01 - Student Result Management System

### Purpose

Accept marks for five subjects and calculate:

- Total marks
- Percentage
- Grade
- Pass/Fail result

### Concepts Used

Functions, `for` loops, lists, conditions, return values, user input.

### Run

```bash
python3 task_01/student_result_management.py
```

### Sample Input/Output

```text
--- STUDENT RESULT MANAGEMENT SYSTEM ---
Enter marks for subject 1: 80
Enter marks for subject 2: 75
Enter marks for subject 3: 90
Enter marks for subject 4: 70
Enter marks for subject 5: 85

Marks: [80.0, 75.0, 90.0, 70.0, 85.0]
Total: 400.0
Percentage: 80.0 %
Grade: A
Result: Pass
```

---

## Task 02 - Banking Application

### Purpose

A menu-driven banking application that supports:

- Check balance
- Deposit
- Withdraw
- Transaction history
- Exit

### Concepts Used

Functions, `while` loop, conditions, lists, input validation, transaction history.

### Run

```bash
python3 task_02/banking_application.py
```

### Sample Input/Output

```text
--- BANKING APPLICATION ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter choice: 2
Enter deposit amount: ₹500
Deposit successful.

Enter choice: 1
Current Balance: ₹ 10500.0
```

---

## Task 03 - Inventory Management

### Purpose

Maintain product information containing product name, price, and quantity.

The program can:

- Add products
- Display products
- Search products
- Update quantity
- Calculate total inventory value

### Concepts Used

Functions, dictionaries, `while` loop, `for` loop, conditions, user input.

### Run

```bash
python3 task_03/inventory_management.py
```

### Sample Input/Output

```text
--- INVENTORY MANAGEMENT ---
1. Add Product
2. Display Products
3. Search Product
4. Update Quantity
5. Total Inventory Value
6. Exit
Enter choice: 1
Enter product name: Laptop
Enter price: 50000
Enter quantity: 2
Product added successfully.

Enter choice: 5
Total Inventory Value: ₹ 100000.0
```

---

## Task 04 - Quiz Application

### Purpose

Run a Python quiz with at least five questions.

The program:

- Displays one question at a time
- Accepts answers
- Checks answers
- Maintains score
- Shows final percentage

### Concepts Used

Lists, dictionaries, `for` loop, conditions, strings, score calculation.

### Run

```bash
python3 task_04/quiz_application.py
```

### Sample Input/Output

```text
--- PYTHON QUIZ ---

Which keyword is used to create a function?
Your answer: def
Correct!

Final Score: 5 / 5
Percentage: 100.0 %
```

---

## Task 05 - Number Analysis Tool

### Purpose

Analyze a list of numbers and calculate:

- Largest number
- Smallest number
- Total
- Average
- Even count
- Odd count
- Positive count
- Negative count

The program calculates these values without using `min()`, `max()`, or `sum()`.

### Concepts Used

Functions, lists, `for` loops, conditions, counters, manual calculations.

### Run

```bash
python3 task_05/number_analysis_tool.py
```

### Sample Output

```text
--- NUMBER ANALYSIS TOOL ---
Numbers: [10, -5, 20, 7, -3, 0, 18, 11]
largest : 20
smallest : -5
total : 58
average : 7.25
even_count : 4
odd_count : 4
positive_count : 5
negative_count : 2
```

---

## Task 06 - Employee Salary Analyzer

### Purpose

Analyze employee salaries and determine:

- Total payroll
- Average salary
- Highest salary
- Lowest salary
- Salaries above average

### Concepts Used

Functions, lists, loops, conditions, calculations.

### Run

```bash
python3 task_06/employee_salary_analyzer.py
```

### Sample Output

```text
--- EMPLOYEE SALARY ANALYZER ---
Salaries: [35000, 50000, 42000, 75000, 60000, 90000]
Total Payroll: 352000
Average Salary: 58666.666666666664
Highest Salary: 90000
Lowest Salary: 35000
Above Average Salaries: [75000, 60000, 90000]
```

---

## Task 07 - Shopping Cart

### Purpose

A menu-driven shopping cart where users can:

- Add products
- Remove products
- View cart
- Calculate total bill
- Exit

### Concepts Used

Functions, lists, dictionaries, `while` loop, `for` loop, conditions.

### Run

```bash
python3 task_07/shopping_cart.py
```

### Sample Input/Output

```text
--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 1
Enter product name: Keyboard
Enter product price: ₹1500
Product added.

Enter choice: 4
Total Bill: ₹ 1500.0
```

---

## Task 08 - Password Strength Checker

### Purpose

Check whether a password contains:

- Uppercase letter
- Lowercase letter
- Number
- Special character
- Minimum eight characters

The program returns a meaningful password-strength result.

### Concepts Used

Functions, strings, loops, conditions, character validation.

### Run

```bash
python3 task_08/password_strength_checker.py
```

### Sample Input/Output

```text
Enter password: Python@123
Strong Password
```

Example of a weak password:

```text
Enter password: python
Weak Password. Missing: uppercase letter, number, special character, minimum 8 characters
```

---

## Task 09 - Prime Number Analyzer

### Purpose

Accept a start and end number, then:

- Find prime numbers in the range
- Count prime numbers
- Calculate their total
- Display the largest prime

### Concepts Used

Functions, `for` loops, `while` loop, conditions, lists, prime-number logic.

### Run

```bash
python3 task_09/prime_number_analyzer.py
```

### Sample Input/Output

```text
Enter range start: 1
Enter range end: 20
Prime Numbers: [2, 3, 5, 7, 11, 13, 17, 19]
Prime Count: 8
Prime Sum: 77
Largest Prime: 19
```

---

## Task 10 - Expense Tracker

### Purpose

A menu-driven expense tracker that allows users to:

- Add expenses
- View expenses
- Calculate total expenses
- Find the highest expense
- Exit

### Concepts Used

Functions, lists, dictionaries, `while` loop, `for` loop, conditions.

### Run

```bash
python3 task_10/expense_tracker.py
```

### Sample Input/Output

```text
--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 1
Enter expense name: Groceries
Enter amount: ₹1200
Expense added.

Enter choice: 3
Total Expenses: ₹ 1200.0
```

---

## Task 11 - Mini Authentication System

### Purpose

A small authentication application supporting:

- Predefined username and password
- Maximum login attempts
- Successful login
- Failed login
- Retry logic
- Dashboard
- Logout

### Concepts Used

Functions, `while` loops, conditions, Boolean values, authentication logic.

### Run

```bash
python3 task_11/authentication_system.py
```

### Sample Input/Output

```text
--- MINI AUTHENTICATION SYSTEM ---
Username: admin
Password: python123
Login successful.

1. View Dashboard
2. Logout
Enter choice: 1
Welcome to the dashboard.

Enter choice: 2
Logout successful.
```

---

## Task 12 - Super30 Python Utility Application

### Purpose

A menu-driven utility application containing multiple reusable tools:

- Calculator
- Palindrome checker
- Prime checker
- Factorial calculator
- Multiplication table
- Number analyzer
- Password strength checker

### Concepts Used

Functions, `while` loops, `for` loops, conditions, reusable logic, strings, numbers.

### Run

```bash
python3 task_12/super30_utility_application.py
```

### Sample Input/Output

```text
--- SUPER30 PYTHON UTILITY APPLICATION ---
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial Calculator
5. Multiplication Table
6. Number Analyzer
7. Password Strength Checker
8. Exit
Enter choice: 4
Enter number: 5
Factorial: 120
```

---

## Concepts Used Across the Project

The project demonstrates practical use of:

- Python functions
- Function parameters and return values
- `for` loops
- `while` loops
- Conditional statements
- Lists
- Dictionaries
- Strings
- Numeric calculations
- Counters and accumulators
- Menu-driven applications
- User input
- Input validation and error handling
- Reusable program logic

## Learning Outcomes

After completing this project, I learned how to:

- Break larger problems into smaller reusable functions
- Choose between `for` and `while` loops based on the requirement
- Build menu-driven applications that continue until the user exits
- Store and process data using lists and dictionaries
- Perform calculations manually using loops
- Validate user input and handle invalid choices
- Build reusable logic for authentication, prime checking, password validation, and calculations
- Organize multiple Python programs into a clean GitHub repository
- Document programs with meaningful names, comments, docstrings, execution commands, and sample output

## Error Handling

Numeric-input programs should handle invalid text input with `try/except ValueError` so that the application does not crash when a number is expected.

Example:

```python
while True:
    try:
        amount = float(input("Enter amount: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
```

## GitHub Repository

https://github.com/nirajdewangan/super30-python-final-loop-function-project/tree/master

## YouTube Demonstration

Add the public or unlisted YouTube explanation link here after recording:

```text
YouTube Explanation: <your-youtube-video-link>
```

The technical explanation should demonstrate the problem statement, approach, important functions, loop logic, why `for` or `while` was selected, execution, test cases, errors/challenges faced, and learning outcomes.

## Author

**Niraj Kumar Dewangan**

Super30 Python - Final Combined Challenge: Loops + While + Functions
