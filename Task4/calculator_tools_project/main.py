import calculator_tools as calc


def main():

    print("=" * 50)
    print("CALCULATOR TOOLS PACKAGE DEMONSTRATION")
    print("=" * 50)

    # ----------------------------------------
    # Arithmetic Operations
    # ----------------------------------------

    print("\n1. ARITHMETIC OPERATIONS")

    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))

    # ----------------------------------------
    # Percentage
    # ----------------------------------------

    print("\n2. PERCENTAGE CALCULATION")

    result = calc.percentage(45, 50)

    print("Percentage:", result, "%")

    # ----------------------------------------
    # Average
    # ----------------------------------------

    print("\n3. AVERAGE CALCULATION")

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("Average:", calc.average(numbers))

    # ----------------------------------------
    # Temperature Conversion
    # ----------------------------------------

    print("\n4. TEMPERATURE CONVERSION")

    print(
        "25 Celsius to Fahrenheit:",
        calc.convert_temperature(
            25,
            "celsius",
            "fahrenheit"
        )
    )

    print(
        "77 Fahrenheit to Celsius:",
        calc.convert_temperature(
            77,
            "fahrenheit",
            "celsius"
        )
    )

    # ----------------------------------------
    # Unit Conversion
    # ----------------------------------------

    print("\n5. UNIT CONVERSION")

    print(
        "2 Kilometer to Meter:",
        calc.convert_length(
            2,
            "kilometer",
            "meter"
        )
    )

    print(
        "500 Centimeter to Meter:",
        calc.convert_length(
            500,
            "centimeter",
            "meter"
        )
    )

    # ----------------------------------------
    # Error Handling
    # ----------------------------------------

    print("\n6. ERROR HANDLING")

    try:
        calc.divide(10, 0)

    except ZeroDivisionError as error:
        print("Division Error:", error)

    try:
        calc.add("10", 5)

    except TypeError as error:
        print("Type Error:", error)

    try:
        calc.calculate(10, 5, "power")

    except calc.InvalidOperationError as error:
        print("Custom Exception:", error)

    try:
        calc.convert_length(
            10,
            "meter",
            "mile"
        )

    except calc.InvalidOperationError as error:
        print("Conversion Error:", error)

    print("\n" + "=" * 50)
    print("PACKAGE DEMONSTRATION COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()