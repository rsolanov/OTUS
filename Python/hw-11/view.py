"""
This module contains the view class for the contact book application.
It handles all user interface related operations.
"""

class ContactView:
    """Handles the user interface for the contact book application."""

    @staticmethod
    def show_menu() -> None:
        """Display the main menu of the application."""
        print("\nТелефонный справочник")
        print("1. Показать все контакты")
        print("2. Найти контакт")
        print("3. Добавить контакт")
        print("4. Редактировать контакт")
        print("5. Удалить контакт")
        print("6. Выход")

    @staticmethod
    def get_user_input(prompt: str) -> str:
        """
        Get input from the user.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: The user's input.
        """
        return input(prompt)

    @staticmethod
    def show_contact(contact) -> None:
        """
        Display a single contact.

        Args:
            contact: The contact to display.
        """
        print(f"Имя: {contact.name}")
        print(f"Телефон: {contact.phone}")
        print(f"Email: {contact.email}")

    @staticmethod
    def show_message(message: str) -> None:
        """
        Display a message to the user.

        Args:
            message (str): The message to display.
        """
        print(message)

    @staticmethod
    def show_contacts(contacts) -> None:
        """
        Display all contacts.

        Args:
            contacts: A collection of contacts to display.
        """
        if not contacts:
            print("Справочник пуст.")
        else:
            print("Список всех контактов:")
            for contact in contacts.values():
                ContactView.show_contact(contact)
                print("-" * 20)

    @staticmethod
    def show_error(error_message: str) -> None:
        """
        Display an error message to the user.

        Args:
            error_message (str): The error message to display.
        """
        print(f"Ошибка: {error_message}")