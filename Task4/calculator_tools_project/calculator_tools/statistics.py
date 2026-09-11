def average(numbers):
    """Calculate the average of a list of numbers."""

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")

    total = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All values must be integers or floats.")

        total += number

    return total / len(numbers)