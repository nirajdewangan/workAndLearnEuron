# ============================================================
# 11. MINI AUTHENTICATION SYSTEM
# ============================================================

def authenticate(username, password):
    """Check username and password."""
    correct_username = "admin"
    correct_password = "python123"

    return (
        username == correct_username
        and password == correct_password
    )


def login():
    """Allow a maximum of three login attempts."""
    attempts = 0
    maximum_attempts = 3

    while attempts < maximum_attempts:

        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):
            print("Login successful.")
            return True

        attempts += 1

        print("Login failed.")
        print(
            "Attempts remaining:",
            maximum_attempts - attempts
        )

    print("Maximum login attempts reached.")
    return False


def mini_authentication_system():
    """Run authentication system with login and logout."""
    print("\n--- MINI AUTHENTICATION SYSTEM ---")

    logged_in = login()

    if not logged_in:
        return

    while logged_in:
        print("\n1. View Dashboard")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Welcome to the dashboard.")

        elif choice == "2":
            logged_in = False
            print("Logout successful.")

        else:
            print("Invalid choice.")

mini_authentication_system()