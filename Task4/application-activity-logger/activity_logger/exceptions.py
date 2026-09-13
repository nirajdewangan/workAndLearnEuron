class ApplicationLoggerError(Exception):
    """Base exception for the application."""
    pass


class AuthenticationError(ApplicationLoggerError):
    """Raised when login credentials are incorrect."""
    pass


class CalculationError(ApplicationLoggerError):
    """Raised when a calculation cannot be completed."""
    pass


class FileOperationError(ApplicationLoggerError):
    """Raised when a file operation fails."""
    pass