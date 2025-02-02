class ContactBookError(Exception):
    """Base exception class for ContactBook errors."""
    pass


class InvalidDataFormatError(ContactBookError):
    """Exception raised when the data format in the file is invalid."""
    pass


class ContactNotFoundError(ContactBookError):
    """Exception raised when a contact is not found."""
    pass


class ContactAlreadyExistsError(ContactBookError):
    """Exception raised when trying to add a contact that already exists."""
    pass