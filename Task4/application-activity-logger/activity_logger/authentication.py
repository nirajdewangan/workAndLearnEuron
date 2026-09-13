from activity_logger.exceptions import AuthenticationError


VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"


def login(username, password, logger):
    """Validate username and password."""

    logger.debug(
        "Login attempt received for username: %s",
        username
    )

    if username == VALID_USERNAME and password == VALID_PASSWORD:

        logger.info(
            "User logged in successfully: %s",
            username
        )

        return True

    logger.warning(
        "Failed login attempt for username: %s",
        username
    )

    raise AuthenticationError(
        "Invalid username or password."
    )


def logout(username, logger):
    """Log out the current user."""

    logger.info(
        "User logged out: %s",
        username
    )