class TaskManagerError(Exception):
    """Base exception for the Task Manager application."""
    pass


class TaskNotFoundError(TaskManagerError):
    """Raised when a requested task cannot be found."""
    pass


class InvalidTaskError(TaskManagerError):
    """Raised when task information is invalid."""
    pass


class StorageError(TaskManagerError):
    """Raised when task data cannot be loaded or saved."""
    pass