
# Intermediate Loops & Loop Control
# Super30 Python Loop Task 2


# ==================================================
# Question 1
# Print numbers from 1-100 but skip numbers
# divisible by 5 using continue
# ==================================================

print("\n--- Question 1: Skip Numbers Divisible by 5 ---")

for number in range(1, 101):
    if number % 5 == 0:
        continue

    print(number, end=" ")

print()


# ==================================================
# Question 2
# Stop at the first number divisible by both 7 and 11
# ==================================================

print("\n--- Question 2: Break Example ---")

for number in range(1, 101):
    if number % 7 == 0 and number % 11 == 0:
        print("First number divisible by both 7 and 11:", number)
        break


# ==================================================
# Question 3
# Search for a number using for-else
# ==================================================

print("\n--- Question 3: Search Using For-Else ---")

numbers = [10, 20, 30, 40, 50]

search_number = int(input("Enter a number to search: "))

for number in numbers:
    if number == search_number:
        print("Number Found")
        break
else:
    print("Number Not Found")


# ==================================================
# Question 4
# Display names using enumerate()
# ==================================================

print("\n--- Question 4: Enumerate Names ---")

names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]

for position, name in enumerate(names, start=1):
    print(position, name)


# ==================================================
# Question 5
# Increasing Star Pattern
# ==================================================

print("\n--- Question 5: Increasing Star Pattern ---")

for row in range(1, 6):
    print("*" * row)


# ==================================================
# Question 6
# Decreasing Star Pattern
# ==================================================

print("\n--- Question 6: Decreasing Star Pattern ---")

for row in range(5, 0, -1):
    print("*" * row)


# ==================================================
# Question 7
# Multiplication tables from 1 to 10
# using nested loops
# ==================================================

print("\n--- Question 7: Multiplication Tables ---")

for table in range(1, 11):

    print("\nTable of", table)

    for number in range(1, 11):
        print(table, "x", number, "=", table * number)


# ==================================================
# Question 8
# Find numbers between 1 and 200
# divisible by both 3 and 5
# ==================================================

print("\n--- Question 8: Numbers Divisible by 3 and 5 ---")

for number in range(1, 201):
    if number % 3 == 0 and number % 5 == 0:
        print(number, end=" ")

print()


# ==================================================
# Question 9
# Remove duplicates without using set()
# ==================================================

print("\n--- Question 9: Remove Duplicates Without Set ---")

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original List:", numbers)
print("Unique List:", unique_numbers)


# ==================================================
# Question 10
# Count positive, negative and zero numbers
# ==================================================

print("\n--- Question 10: Positive, Negative and Zero ---")

numbers = [10, -4, 8, -2, 0, 15, -9, 21]

positive = 0
negative = 0
zeros = 0

for number in numbers:

    if number > 0:
        positive += 1

    elif number < 0:
        negative += 1

    else:
        zeros += 1

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)
print("Zeros:", zeros)


# ==================================================
# Question 11
# Check whether a number is prime
# ==================================================

print("\n--- Question 11: Prime Number Check ---")

number = int(input("Enter a number to check for prime: "))

if number <= 1:
    print(number, "is not a prime number.")

else:
    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")

    else:
        print(number, "is not a prime number.")


# ==================================================
# Question 12
# Print all prime numbers between 1 and 100
# ==================================================

print("\n--- Question 12: Prime Numbers Between 1 and 100 ---")

for number in range(2, 101):

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()


# ==================================================
# End
# ==================================================

print("\n\nAll Intermediate Loop Challenges Completed!")