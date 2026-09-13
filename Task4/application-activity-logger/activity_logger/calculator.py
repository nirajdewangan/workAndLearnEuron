from activity_logger.exceptions import CalculationError


def calculate(
    first_number,
    operator,
    second_number,
    logger
):
    """Perform a mathematical calculation."""

    logger.debug(
        "Calculation requested: %s %s %s",
        first_number,
        operator,
        second_number
    )

    try:

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":

            if second_number == 0:

                logger.error(
                    "Division by zero attempted."
                )

                raise CalculationError(
                    "Cannot divide by zero."
                )

            result = first_number / second_number

        else:

            logger.warning(
                "Invalid calculator operator: %s",
                operator
            )

            raise CalculationError(
                "Invalid operator. "
                "Use +, -, *, or /."
            )

        logger.info(
            "Calculation completed successfully."
        )

        logger.debug(
            "Calculation result: %s",
            result
        )

        return result

    except CalculationError:
        raise

    except Exception as error:

        logger.error(
            "Calculation failed: %s",
            error
        )

        raise CalculationError(
            "Unable to complete calculation."
        )