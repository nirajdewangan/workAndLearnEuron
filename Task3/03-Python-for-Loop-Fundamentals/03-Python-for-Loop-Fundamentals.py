
# Python for Loop Fundamentals
# Super30 Python Loop Task 1


# ==================================================
# Question 1
# Print numbers from 1 to 100
# ==================================================

print("\n--- Question 1: Numbers from 1 to 100 ---")

for number in range(1, 101):
    print(number, end=" ")

print()


# ==================================================
# Question 2
# Print even numbers from 1 to 100
# ==================================================

print("\n--- Question 2: Even Numbers from 1 to 100 ---")

for number in range(1, 101):
    if number % 2 == 0:
        print(number, end=" ")

print()


# ==================================================
# Question 3
# Print odd numbers from 1 to 100
# ==================================================

print("\n--- Question 3: Odd Numbers from 1 to 100 ---")

for number in range(1, 101):
    if number % 2 != 0:
        print(number, end=" ")

print()


# ==================================================
# Question 4
# Multiplication table from 1 to 20
# ==================================================

print("\n--- Question 4: Multiplication Table ---")

n = int(input("Enter a number for multiplication table: "))

for i in range(1, 21):
    print(n, "x", i, "=", n * i)


# ==================================================
# Question 5
# Calculate sum from 1 to n using loop
# ==================================================

print("\n--- Question 5: Sum from 1 to n ---")

n = int(input("Enter a number to calculate sum: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum from 1 to", n, "is:", total)


# ==================================================
# Question 6
# Calculate factorial without built-in function
# ==================================================

print("\n--- Question 6: Factorial ---")

number = int(input("Enter a number to calculate factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial of", number, "is:", factorial)


# ==================================================
# Question 7
# Print numbers divisible by 3
# ==================================================

print("\n--- Question 7: Numbers Divisible by 3 ---")

numbers = [12, 7, 9, 20, 33, 42, 8, 15]

print("Original List:", numbers)
print("Numbers divisible by 3:")

for number in numbers:
    if number % 3 == 0:
        print(number)


# ==================================================
# Question 8
# Print each language with its length
# ==================================================

print("\n--- Question 8: Languages and Length ---")

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

for language in languages:
    print(language, "-", len(language))


# ==================================================
# Question 9
# Iterate through dictionary
# ==================================================

print("\n--- Question 9: Student Dictionary ---")

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Data Science",
    "city": "Bangalore"
}

for key, value in student.items():
    print(key, ":", value)


# ==================================================
# Question 10
# Count vowels in user-provided string
# ==================================================

print("\n--- Question 10: Count Vowels ---")

text = input("Enter a string to count vowels: ")

vowel_count = 0

for character in text.lower():
    if character in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)


# ==================================================
# Question 11
# Reverse a string using for loop
# Without [::-1] or reversed()
# ==================================================

print("\n--- Question 11: Reverse a String ---")

text = input("Enter a string to reverse: ")

reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print("Original String:", text)
print("Reversed String:", reversed_text)


# ==================================================
# Question 12
# Find largest number without max()
# ==================================================

print("\n--- Question 12: Largest Number ---")

numbers = [12, 45, 7, 89, 34, 67, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("List:", numbers)
print("Largest Number:", largest)


# ==================================================
# End
# ==================================================

print("\nAll Python For Loop Fundamentals Challenges Completed!")