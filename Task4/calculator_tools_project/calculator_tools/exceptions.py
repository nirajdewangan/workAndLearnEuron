class InvalidOperationError(Exception):
    """Custom exception for unsupported calculator operations."""

    def __init__(self, message="Invalid or unsupported operation."):
        super().__init__(message)