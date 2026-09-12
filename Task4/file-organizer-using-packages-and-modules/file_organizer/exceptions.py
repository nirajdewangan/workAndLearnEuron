class UnsupportedFileError(Exception):
    """Raised when a file type is not supported."""

    def __init__(self, extension):
        message = f"Unsupported file type: {extension}"
        super().__init__(message)