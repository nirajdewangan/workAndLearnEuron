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

expense_tracker()