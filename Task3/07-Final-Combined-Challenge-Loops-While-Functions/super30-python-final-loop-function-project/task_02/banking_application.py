# ============================================================
# 2. BANKING APPLICATION
# ============================================================

def get_valid_float(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def bank_check_balance(balance):
    """Display current bank balance."""
    print("Current Balance: ₹", balance)


def bank_deposit(balance, history):
    """Deposit money and return updated balance."""
    amount = get_valid_float("Enter deposit amount: ₹")

    if amount <= 0:
        print("Invalid deposit amount.")
        return balance

    balance += amount
    history.append(f"Deposited ₹{amount}")

    print("Deposit successful.")
    return balance


def bank_withdraw(balance, history):
    """Withdraw money and return updated balance."""
    amount = get_valid_float("Enter withdrawal amount: ₹")
    
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

banking_application()