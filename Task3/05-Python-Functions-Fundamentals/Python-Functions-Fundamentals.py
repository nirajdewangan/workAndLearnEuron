# Python Functions Fundamentals
# Super30 Python Functions Task 1


# ==================================================
# Question 1
# Create add(a, b)
# ==================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print("Addition:", add(10, 5))


# ==================================================
# Question 2
# Addition, subtraction, multiplication, division
# ==================================================

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result of two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by zero:", divide(10, 0))


# ==================================================
# Question 3
# Even or Odd
# ==================================================

def check_even_odd(number):
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


print("7 is:", check_even_odd(7))
print("10 is:", check_even_odd(10))


# ==================================================
# Question 4
# Largest of three without max()
# ==================================================

def largest_of_three(a, b, c):
    """Return the largest of three numbers without using max()."""
    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest


print("Largest Number:", largest_of_three(25, 60, 40))


# ==================================================
# Question 5
# Factorial
# ==================================================

def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        return "Factorial is not defined for negative numbers."

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial of 5:", factorial(5))


# ==================================================
# Question 6
# Prime Number Check
# ==================================================

def is_prime(number):
    """Return True if the number is prime, otherwise False."""
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


print("Is 7 prime?:", is_prime(7))
print("Is 12 prime?:", is_prime(12))


# ==================================================
# Question 7
# Default Discount
# ==================================================

def calculate_discount(price, discount=10):
    """Return final price after applying a discount percentage."""
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price


print("Price after default 10% discount:", calculate_discount(1000))
print("Price after 20% discount:", calculate_discount(1000, 20))


# ==================================================
# Question 8
# Sum of a list without sum()
# ==================================================

def list_total(numbers):
    """Return the total of all numbers in a list without using sum()."""
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40]
print("List Total:", list_total(numbers))


# ==================================================
# Question 9
# Count vowels
# ==================================================

def count_vowels(text):
    """Return the number of vowels in a string."""
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count += 1

    return count


print("Vowel Count:", count_vowels("Python Programming"))


# ==================================================
# Question 10
# Palindrome
# ==================================================

def is_palindrome(text):
    """Return True if the string is a palindrome, otherwise False."""
    cleaned_text = text.lower()
    reversed_text = ""

    for character in cleaned_text:
        reversed_text = character + reversed_text

    return cleaned_text == reversed_text


print("Is madam a palindrome?:", is_palindrome("madam"))
print("Is python a palindrome?:", is_palindrome("python"))


# ==================================================
# Question 11
# Student Profile
# Positional and Keyword Arguments
# ==================================================

def student_profile(name, age, course):
    """Return a formatted student profile string."""
    return (
        f"Name: {name}, Age: {age}, Course: {course}"
    )


# Positional arguments
profile1 = student_profile("Rahul", 22, "Python")
print("Positional Arguments:", profile1)

# Keyword arguments
profile2 = student_profile(
    course="Data Science",
    name="Priya",
    age=23
)
print("Keyword Arguments:", profile2)


# ==================================================
# Question 12
# Print vs Return
# ==================================================

def print_result(a, b):
    """Print the sum of two numbers directly."""
    print("Printed Result:", a + b)


def return_result(a, b):
    """Return the sum of two numbers so it can be reused."""
    return a + b


print_result(10, 20)

returned_value = return_result(10, 20)

print("Returned Value:", returned_value)

# Return value can be reused in another calculation
new_result = returned_value * 2

print("Returned Value Used Again:", new_result)


# ==================================================
# Scope Demonstration
# ==================================================

global_message = "I am a global variable"


def demonstrate_scope():
    """Demonstrate local and global variable scope."""
    local_message = "I am a local variable"

    print("Inside Function - Global:", global_message)
    print("Inside Function - Local:", local_message)


demonstrate_scope()

print("Outside Function - Global:", global_message)


print("\nAll Python Functions Fundamentals Programs Completed!")