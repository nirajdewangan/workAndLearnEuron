class InvalidMarksError(Exception):
    """Raised when student marks are outside the valid range."""
    pass


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""
    pass