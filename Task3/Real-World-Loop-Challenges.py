# 1. Transaction Analysis
transactions = [1200, 450, 800, 1500, 2300, 700, 100]

total = 0

for transaction in transactions:
    total += transaction

print("Total Transaction Value:", total)

highest = transactions[0]
lowest = transactions[0]

for transaction in transactions:
    if transaction > highest:
        highest = transaction

    if transaction < lowest:
        lowest = transaction

print("Highest Transaction:", highest)
print("Lowest Transaction:", lowest)

# 2. Average Temperature
temperatures = [32, 35, 28, 40, 38, 31, 42]

total_temperature = 0

for temperature in temperatures:
    total_temperature += temperature

average = total_temperature / len(temperatures)

print("Average Temperature:", average)

# 3. Student Grades
marks = [78, 92, 45, 67, 88, 53, 99]

above_90 = 0
between_75_89 = 0
between_50_74 = 0
below_50 = 0

for mark in marks:

    if mark >= 90:
        above_90 += 1

    elif mark >= 75:
        between_75_89 += 1

    elif mark >= 50:
        between_50_74 += 1

    else:
        below_50 += 1

print("90+:", above_90)
print("75-89:", between_75_89)
print("50-74:", between_50_74)
print("Below 50:", below_50)

# 4. Login Attempt System
correct_password = "python123"

for attempt in range(1, 4):

    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    else:
        print("Incorrect password.")

        remaining = 3 - attempt

        if remaining > 0:
            print("Attempts remaining:", remaining)

else:
    print("Maximum attempts reached. Login blocked.")

# 5. Filter Products Above ₹2,000
products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000,
    "Mouse": 700,
    "Keyboard": 1500
}

for product, price in products.items():

    if price > 2000:
        print(product, "-", price)

# 6. Accept 10 Numbers
numbers = []

for i in range(10):

    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Numbers:", numbers)

# 7. Character Frequency
text = input("Enter a string: ")

frequency = {}

for character in text:

    if character in frequency:
        frequency[character] += 1

    else:
        frequency[character] = 1

print("Character Frequency:")

for character, count in frequency.items():
    print(character, "->", count)

# 8. Second-Largest Number
numbers = [10, 45, 23, 67, 67, 34, 56]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:

        if number != largest:
            second_largest = largest

        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

if second_largest is None:
    print("Second-largest value does not exist.")
else:
    print("Largest:", largest)
    print("Second Largest:", second_largest)

# 9. Palindrome Using Loops
text = input("Enter a string: ")

is_palindrome = True

left = 0
right = len(text) - 1

while left < right:

    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")

# 10. Number Pattern
for row in range(1, 6):

    for number in range(1, row + 1):
        print(number, end="")

    print()

# 11. ATM Simulation
balance = 10000


def check_balance():
    print("Current Balance: ₹", balance)


def deposit_money():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print("Deposit successful.")
        print("Updated Balance: ₹", balance)

    else:
        print("Invalid deposit amount.")


def withdraw_money():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining Balance: ₹", balance)


while True:

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")

        