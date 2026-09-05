# ============================================================
# 8. PASSWORD STRENGTH CHECKER
# ============================================================

def check_password_strength(password):
    """Check password requirements and return a meaningful result."""

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"

    for character in password:

        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

        elif character.isdigit():
            has_number = True

        elif character in special_characters:
            has_special = True

    has_minimum_length = len(password) >= 8

    missing = []

    if not has_uppercase:
        missing.append("uppercase letter")

    if not has_lowercase:
        missing.append("lowercase letter")

    if not has_number:
        missing.append("number")

    if not has_special:
        missing.append("special character")

    if not has_minimum_length:
        missing.append("minimum 8 characters")

    if len(missing) == 0:
        return "Strong Password"

    return "Weak Password. Missing: " + ", ".join(missing)


def password_strength_checker():
    """Run Password Strength Checker."""
    password = input("Enter password: ")

    print(check_password_strength(password))

password_strength_checker()