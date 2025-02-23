import json
import pytest
from model import Contact, ContactBook
from exceptions import ContactAlreadyExistsError, ContactNotFoundError, InvalidDataFormatError
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



def test_add_contact(contact_book):
    """
    Test adding a new contact to the contact book.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    assert contact_book.find_contact("+1234567890") == contact



def test_add_duplicate_contact(contact_book):
    """
    Test adding a duplicate contact to the contact book.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    with pytest.raises(ContactAlreadyExistsError):
        contact_book.add_contact(contact)



def test_find_contact(contact_book):
    """
    Test finding a contact by phone number.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    found_contact = contact_book.find_contact("+1234567890")
    assert found_contact == contact



def test_find_nonexistent_contact(contact_book):
    """
    Test finding a non-existent contact.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    assert contact_book.find_contact("+1234567890") is None



def test_edit_contact(contact_book):
    """
    Test editing an existing contact.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    contact_book.edit_contact("+1234567890", "Petrov Ivan", "petrov.ivan@example.com")
    edited_contact = contact_book.find_contact("+1234567890")
    assert edited_contact.name == "Petrov Ivan"
    assert edited_contact.email == "petrov.ivan@example.com"



def test_edit_nonexistent_contact(contact_book):
    """
    Test editing a non-existent contact.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    with pytest.raises(ContactNotFoundError):
        contact_book.edit_contact("+1234567890", "Petrov Ivan", "petrov.ivan@example.com")



def test_delete_contact(contact_book):
    """
    Test deleting a contact.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    contact_book.delete_contact("+1234567890")
    assert contact_book.find_contact("+1234567890") is None



def test_delete_nonexistent_contact(contact_book):
    """
    Test deleting a non-existent contact.

    Args:
        contact_book (ContactBook): The contact book instance.
    """
    with pytest.raises(ContactNotFoundError):
        contact_book.delete_contact("+1234567890")



def test_load_contacts(file_handler):
    """
    Test loading contacts from a file.

    Args:
        file_handler (FileHandler): The file handler instance.
    """
    contacts = file_handler.load_contacts("contact_book.json")
    assert isinstance(contacts, dict)
    assert "+79876543210" in contacts
    assert contacts["+79876543210"].name == "Соланов Роман"
    assert contacts["+79876543210"].email == "rsolanov@gmail.com"



def test_save_contacts(contact_book, file_handler, tmp_path):
    """
    Test saving contacts to a file.

    Args:
        contact_book (ContactBook): The contact book instance.
        file_handler (FileHandler): The file handler instance.
        tmp_path (pathlib.Path): Temporary directory provided by pytest.
    """
    contact = Contact("Ivanov Peter", "+1234567890", "ivanov.peter@example.com")
    contact_book.add_contact(contact)
    file_path = tmp_path / "test_contact_book.json"
    file_handler.save_contacts(file_path, contact_book.get_all_contacts())
    with open(file_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    assert "+1234567890" in data
    assert data["+1234567890"] == ["Ivanov Peter", "ivanov.peter@example.com"]



def test_invalid_data_format(file_handler, tmp_path):
    """
    Test handling invalid data format in a file.

    Args:
        file_handler (FileHandler): The file handler instance.
        tmp_path (pathlib.Path): Temporary directory provided by pytest.
    """
    invalid_data = {"+1234567890": "Ivanov Peter"}
    file_path = tmp_path / "invalid_contact_book.json"
    with open(file_path, 'w', encoding='UTF-8') as file:
        json.dump(invalid_data, file)
    with pytest.raises(InvalidDataFormatError):
        file_handler.load_contacts(file_path)