# 11_atm_simulation.py

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