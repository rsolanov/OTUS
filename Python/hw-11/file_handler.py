import json
import os.path

from exceptions import InvalidDataFormatError
from model import Contact


class FileHandler:
    """Handles file operations for saving and loading contacts."""

    @staticmethod
    def load_contacts(filename: str) -> dict[str, Contact]:
        """
        Load contacts from a JSON file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            dict[str, Contact]: A dictionary of loaded contacts.
        """
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                contacts = {}
                for phone, info in data.items():
                    if isinstance(info, list) and len(info) == 2:
                        name, email = info
                        contacts[phone] = Contact(name, phone, email)
                    else:
                        raise InvalidDataFormatError(f"Неверный формат данных для контакта с телефоном {phone}")
                return contacts
        return {}

    @staticmethod
    def save_contacts(filename: str, contacts: dict[str, Contact]) -> None:
        """
        Save contacts to a JSON file.

        Args:
            filename (str): The name of the file to save to.
            contacts (dict[str, Contact]): The contacts to save.
        """

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump({
                contact.phone: [contact.name, contact.email]
                for contact in contacts.values()
            }, file, indent=2, ensure_ascii=False)