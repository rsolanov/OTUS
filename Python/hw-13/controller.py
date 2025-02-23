from exceptions import ContactAlreadyExistsError, ContactNotFoundError
from file_handler import FileHandler
from model import ContactBook, Contact
from view import ContactView


class ContactController:
    """
    Controls the flow of the contact book application.

    Attributes:
        model (ContactBook): The contact book model.
        view (ContactView): The view for user interaction.
        file_handler (FileHandler): Handles file operations.
    """

    _FILE_NAME: str = 'contact_book.json'

    def __init__(self, model: ContactBook, view: ContactView):
        """
        Initializes the contact controller.

        Args:
            model (ContactBook): The contact book model.
            view (ContactView): The view for user interaction.
        """
        self.model = model
        self.view = view
        self.file_handler = FileHandler()

    def run(self):
        """Run the main application loop."""
        self.load_contacts()

        exit_main = False
        while not exit_main:
            self.view.show_menu()
            choice = self.view.get_user_input("Enter action: ")

            if choice == '1':
                self.show_all_contacts()
            elif choice == '2':
                self.find_contact()
            elif choice == '3':
                self.add_contact()
            elif choice == '4':
                self.edit_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                self.save_and_exit()
                exit_main = True
            else:
                self.view.show_message("Invalid choice. Try again.")

    def load_contacts(self):
        """Load contacts from file."""
        try:
            self.model.contacts = self.file_handler.load_contacts(self._FILE_NAME)
        except Exception as e:
            self.view.show_error(f"Error loading contacts: {str(e)}")

    def show_all_contacts(self):
        """Display all contacts in the book."""
        contacts = self.model.get_all_contacts()
        self.view.show_contacts(contacts)

    def find_contact(self):
        """Find and display a specific contact."""
        phone = self.view.get_user_input("Enter phone number: ")
        contact = self.model.find_contact(phone)
        if contact:
            self.view.show_contact(contact)
        else:
            self.view.show_message("Contact not found.")

    def add_contact(self):
        """Add a new contact to the book."""
        name = self.view.get_user_input("Enter name: ")
        phone = self.view.get_user_input("Enter phone number: ")
        email = self.view.get_user_input("Enter email: ")
        try:
            new_contact = Contact(name, phone, email)
            self.model.add_contact(new_contact)
            self.view.show_message("Contact added successfully.")
        except ContactAlreadyExistsError as e:
            self.view.show_error(str(e))

    def edit_contact(self):
        """Edit an existing contact."""
        phone = self.view.get_user_input("Enter the phone number of the contact to edit: ")
        contact = self.model.find_contact(phone)
        if contact:
            name = self.view.get_user_input("Enter new name (leave blank to keep current): ")
            email = self.view.get_user_input("Enter new email (leave blank to keep current): ")
            if not name:
                name = contact.name
            if not email:
                email = contact.email
            try:
                self.model.edit_contact(phone, name, email)
                self.view.show_message("Contact updated successfully.")
            except ContactNotFoundError as e:
                self.view.show_error(str(e))
        else:
            self.view.show_error("Contact not found.")

    def delete_contact(self):
        """Delete a contact from the book."""
        phone = self.view.get_user_input("Enter the phone number of the contact to delete: ")
        try:
            self.model.delete_contact(phone)
            self.view.show_message("Contact deleted successfully.")
        except ContactNotFoundError as e:
            self.view.show_error(str(e))

    def save_and_exit(self):
        """Save contacts to file and exit the application."""
        try:
            self.file_handler.save_contacts(self._FILE_NAME, self.model.get_all_contacts())
            self.view.show_message("Contacts saved. Exiting program.")
        except Exception as e:
            self.view.show_error(f"Error saving contacts: {str(e)}")