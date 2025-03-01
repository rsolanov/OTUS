import pytest
from model import ContactBook
from file_handler import FileHandler



@pytest.fixture
def contact_book():
    """
    Fixture to provide a clean instance of ContactBook for each test.

    Returns:
        ContactBook: A new instance of ContactBook with no contacts.
    """
    book = ContactBook()
    book.clear()
    return book



@pytest.fixture
def file_handler():
    """
    Fixture to provide an instance of FileHandler for file operations.

    Returns:
        FileHandler: An instance of FileHandler.
    """
    return FileHandler()
