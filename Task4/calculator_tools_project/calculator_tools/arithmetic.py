from .exceptions import InvalidOperationError


def validate_number(value):
    """Check whether the value is an integer or float."""

    if not isinstance(value, (int, float)):
        raise TypeError("Value must be an integer or float.")


def add(a, b):
    """Return the addition of two numbers."""

    validate_number(a)
    validate_number(b)

    return a + b


def subtract(a, b):
    """Return the subtraction of two numbers."""

    validate_number(a)
    validate_number(b)

    return a - b


def multiply(a, b):
    """Return the multiplication of two numbers."""

    validate_number(a)
    validate_number(b)

    return a * b


def divide(a, b):
    """Return the division of two numbers."""

    validate_number(a)
    validate_number(b)

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def percentage(value, total):
    """Calculate percentage."""

    validate_number(value)
    validate_number(total)

    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")

    return (value / total) * 100


def calculate(a, b, operation):
    """Perform an arithmetic operation based on operation name."""

    if not isinstance(operation, str):
        raise TypeError("Operation must be a string.")

    operation = operation.lower()

    if operation == "add":
        return add(a, b)

    elif operation == "subtract":
        return subtract(a, b)

    elif operation == "multiply":
        return multiply(a, b)

    elif operation == "divide":
        return divide(a, b)

    else:
        raise InvalidOperationError(
            f"Unsupported arithmetic operation: {operation}"
        )