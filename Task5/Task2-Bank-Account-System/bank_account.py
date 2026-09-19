"""A simplified Bank Account System using Python OOP."""


class BankAccount:
    """Represent a bank account and its common operations."""

    bank_name = "Python National Bank"
    total_accounts = 0

    def __init__(self, account_holder_name, account_number, balance=0.0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = float(balance)
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        """Deposit a positive amount and return True when successful."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self.balance += amount
        print(f"Deposit successful: Rs. {amount:.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw money when the amount is valid and funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount > self.balance:
            print("Withdrawal failed: Insufficient balance.")
            return False

        self.balance -= amount
        print(f"Withdrawal successful: Rs. {amount:.2f}")
        return True

    def check_balance(self):
        """Display and return the current account balance."""
        print(f"Current balance: Rs. {self.balance:.2f}")
        return self.balance

    def display_account_details(self):
        """Display all account details."""
        print("\n--- Account Details ---")
        print(f"Bank Name      : {self.bank_name}")
        print(f"Account Holder : {self.account_holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs. {self.balance:.2f}")

    @classmethod
    def change_bank_name(cls, new_name):
        """Change the bank name for every account."""
        if not new_name.strip():
            print("Bank name cannot be empty.")
            return False

        cls.bank_name = new_name.strip()
        print(f"Bank name changed to {cls.bank_name}.")
        return True

    @classmethod
    def get_total_accounts(cls):
        """Return the total number of BankAccount objects created."""
        return cls.total_accounts


def main():
    """Create accounts and demonstrate all banking operations."""
    account1 = BankAccount("Aarav Sharma", "PNB1001", 10000)
    account2 = BankAccount("Diya Verma", "PNB1002", 15000)

    print("BANK ACCOUNT SYSTEM")
    account1.display_account_details()
    account2.display_account_details()

    print("\n--- Transactions for Aarav Sharma ---")
    account1.deposit(2500)
    account1.withdraw(3000)
    account1.check_balance()

    print("\n--- Invalid Withdrawal Test ---")
    account1.withdraw(20000)

    print("\n--- Changing Bank Name ---")
    BankAccount.change_bank_name("Python International Bank")
    account1.display_account_details()
    account2.display_account_details()

    print(f"\nTotal bank accounts created: {BankAccount.get_total_accounts()}")


if __name__ == "__main__":
    main()
