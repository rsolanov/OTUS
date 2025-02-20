from model import Contact


class ContactView:
    """Handles the user interface for the contact book application."""

    @staticmethod
    def show_menu() -> None:
        """Display the main menu of the application."""
        print("\nContact Book Menu")
        print("1. Show all contacts")
        print("2. Find contact")
        print("3. Add contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")

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
    def show_contact(contact: Contact) -> None:
        """
        Display a single contact.

        Args:
            contact (Contact): The contact to display.
        """
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
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
    def show_contacts(contacts: dict[str, Contact]) -> None:
        """
        Display all contacts.

        Args:
            contacts (dict[str, Contact]): A collection of contacts to display.
        """
        if not contacts:
            print("Contact book is empty.")
        else:
            print("List of all contacts:")
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
        print(f"Error: {error_message}")