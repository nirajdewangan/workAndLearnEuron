# while Loop Mastery
# Super30 Python Task


# ==================================================
# Question 1
# Print numbers from 1 to 100 using while
# ==================================================

print("\n--- Question 1: Numbers from 1 to 100 ---")

number = 1

# Initialization: number starts at 1
# Condition: loop continues while number <= 100
# Update/Termination: number increases by 1 until it becomes greater than 100
while number <= 100:
    print(number, end=" ")
    number += 1

print()


# ==================================================
# Question 2
# Print numbers from 100 to 1
# ==================================================

print("\n--- Question 2: Numbers from 100 to 1 ---")

number = 100

# Initialization: number starts at 100
# Condition: loop continues while number >= 1
# Update/Termination: number decreases by 1 until it becomes less than 1
while number >= 1:
    print(number, end=" ")
    number -= 1

print()


# ==================================================
# Question 3
# Print even numbers from 1 to 100
# ==================================================

print("\n--- Question 3: Even Numbers ---")

number = 2

# Initialization: number starts at 2
# Condition: loop continues while number <= 100
# Update/Termination: number increases by 2 until it becomes greater than 100
while number <= 100:
    print(number, end=" ")
    number += 2

print()


# ==================================================
# Question 4
# Calculate sum of digits
# ==================================================

print("\n--- Question 4: Sum of Digits ---")

number = int(input("Enter a number: "))

temp = abs(number)
digit_sum = 0

# Initialization: temp stores the absolute input number and digit_sum starts at 0
# Condition: loop continues while temp > 0
# Update/Termination: temp loses its last digit using temp //= 10 until it becomes 0
while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print("Sum of Digits:", digit_sum)


# ==================================================
# Question 5
# Reverse an integer using while
# ==================================================

print("\n--- Question 5: Reverse an Integer ---")

number = int(input("Enter an integer to reverse: "))

temp = abs(number)
reversed_number = 0

# Initialization: temp stores the input number and reversed_number starts at 0
# Condition: loop continues while temp > 0
# Update/Termination: temp loses one digit using temp //= 10 until it becomes 0
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

if number < 0:
    reversed_number = -reversed_number

print("Reversed Integer:", reversed_number)


# ==================================================
# Question 6
# Count number of digits
# ==================================================

print("\n--- Question 6: Count Digits ---")

number = int(input("Enter an integer to count digits: "))

temp = abs(number)
digit_count = 0

if temp == 0:
    digit_count = 1

else:
    # Initialization: temp stores the absolute input number and digit_count starts at 0
    # Condition: loop continues while temp > 0
    # Update/Termination: temp is divided by 10 each iteration until it becomes 0
    while temp > 0:
        digit_count += 1
        temp //= 10

print("Number of Digits:", digit_count)


# ==================================================
# Question 7
# Calculate factorial using while
# ==================================================

print("\n--- Question 7: Factorial ---")

number = int(input("Enter a number for factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1
    i = 1

    # Initialization: factorial starts at 1 and i starts at 1
    # Condition: loop continues while i <= number
    # Update/Termination: i increases by 1 until it becomes greater than number
    while i <= number:
        factorial *= i
        i += 1

    print("Factorial of", number, "is:", factorial)


# ==================================================
# Question 8
# Keep asking numbers until user enters 0
# ==================================================

print("\n--- Question 8: Sum Until Zero ---")

total = 0
number = int(input("Enter a number (0 to stop): "))

# Initialization: total starts at 0 and number stores the first user input
# Condition: loop continues while number != 0
# Update/Termination: user enters a new number each iteration; entering 0 terminates the loop
while number != 0:
    total += number
    number = int(input("Enter another number (0 to stop): "))

print("Total Sum:", total)


# ==================================================
# Question 9
# Password checker
# ==================================================

print("\n--- Question 9: Password Checker ---")

correct_password = "python123"
password = input("Enter password: ")

# Initialization: password stores the first user-entered password
# Condition: loop continues while password != correct_password
# Update/Termination: password is requested again; correct password terminates the loop
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter password: ")

print("Password correct. Access granted!")


# ==================================================
# Question 10
# Guessing Game
# ==================================================

print("\n--- Question 10: Number Guessing Game ---")

secret_number = 27
guess = int(input("Guess the secret number: "))

# Initialization: secret_number is predefined and guess stores the first user guess
# Condition: loop continues while guess != secret_number
# Update/Termination: user enters another guess; correct guess terminates the loop
while guess != secret_number:

    if guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    guess = int(input("Try again: "))

print("Correct! You guessed the secret number.")


# ==================================================
# Question 11
# Menu-driven Calculator
# ==================================================

print("\n--- Question 11: Menu-Driven Calculator ---")

choice = ""

# Initialization: choice starts as an empty string
# Condition: loop continues while choice != "5"
# Update/Termination: user selects a new menu choice each iteration; choice 5 or break exits
while choice != "5":

    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Calculator.")
        break

    if choice in ["1", "2", "3", "4"]:

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", first_number + second_number)

        elif choice == "2":
            print("Result:", first_number - second_number)

        elif choice == "3":
            print("Result:", first_number * second_number)

        elif choice == "4":

            if second_number == 0:
                print("Cannot divide by zero.")

            else:
                print("Result:", first_number / second_number)

    else:
        print("Invalid choice. Please select 1 to 5.")


# ==================================================
# Question 12
# ATM Menu using while
# ==================================================

print("\n--- Question 12: ATM Simulation ---")

balance = 10000
choice = ""

# Initialization: balance starts at 10000 and choice starts as an empty string
# Condition: loop continues while choice != "4"
# Update/Termination: user selects a new ATM option; choosing 4 terminates the loop
while choice != "4":

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":

        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("Updated Balance: ₹", balance)

        else:
            print("Invalid deposit amount.")

    elif choice == "3":

        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the ATM.")

    else:
        print("Invalid choice. Please select 1 to 4.")


print("\nAll While Loop Mastery Programs Completed!")