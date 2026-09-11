from .exceptions import InvalidOperationError


def validate_number(value):
    """Check whether the value is an integer or float."""

    if not isinstance(value, (int, float)):
        raise TypeError("Value must be an integer or float.")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""

    validate_number(celsius)

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""

    validate_number(fahrenheit)

    return (fahrenheit - 32) * 5 / 9


def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius and Fahrenheit."""

    validate_number(value)

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Temperature units must be strings.")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return celsius_to_fahrenheit(value)

    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return fahrenheit_to_celsius(value)

    else:
        raise InvalidOperationError(
            f"Unsupported temperature conversion: "
            f"{from_unit} to {to_unit}"
        )


def convert_length(value, from_unit, to_unit):
    """Convert length between meter, kilometer and centimeter."""

    validate_number(value)

    if value < 0:
        raise ValueError("Length cannot be negative.")

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Length units must be strings.")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    conversion_to_meter = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01
    }

    if from_unit not in conversion_to_meter:
        raise InvalidOperationError(
            f"Unsupported unit: {from_unit}"
        )

    if to_unit not in conversion_to_meter:
        raise InvalidOperationError(
            f"Unsupported unit: {to_unit}"
        )

    value_in_meters = value * conversion_to_meter[from_unit]

    return value_in_meters / conversion_to_meter[to_unit]