class Contact:
    """
    Represents a single contact in the contact book.

    Attributes:
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
        email (str): The email address of the contact.
    """
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    """
    A class representing a contact book.

    This class implements the Singleton pattern to ensure only one instance
    of the contact book exists throughout the application.

    Attributes:
        _instance (ContactBook): The single instance of the ContactBook.
        contacts (dict[str, Contact]): A dictionary to store contacts,
                                       where the key is the phone number
                                       and the value is a Contact object.
    """
    _instance = None
    contacts: dict[str, Contact] = {}

    def __new__(cls):
        """
        Create a new instance of ContactBook if it doesn't exist,
        otherwise return the existing instance.

        Returns:
            ContactBook: The single instance of the ContactBook.
        """
        if cls._instance is None:
            cls._instance = super(ContactBook, cls).__new__(cls)
        return cls._instance

    def add_contact(self, contact: Contact) -> None:
        """
        Add a new contact to the contact book.

        Args:
            contact (Contact): The contact to be added.
        """
        self.contacts[contact.phone] = contact

    def find_contact(self, phone: str) -> Contact:
        """
        Find a contact by phone number.

        Args:
            phone (str): The phone number to search for.

        Returns:
            Contact: The found contact, or None if not found.
        """
        return self.contacts.get(phone)

    def edit_contact(self, phone: str, name: str, email: str) -> None:
        """
        Edit an existing contact's information.

        Args:
            phone (str): The phone number of the contact to edit.
            name (str): The new name for the contact.
            email (str): The new email for the contact.
        """
        if phone in self.contacts:
            self.contacts[phone].name = name
            self.contacts[phone].email = email

    def delete_contact(self, phone) -> None:
        """
        Delete a contact from the contact book.

        Args:
            phone (str): The phone number of the contact to delete.
        """
        if phone in self.contacts:
            self.contacts.pop(phone, None)