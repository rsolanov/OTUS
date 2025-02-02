"""
This module contains the controller for the contact book application.
It handles the logic and flow of the application.
"""
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
        self.model = model
        self.view = view
        self.file_handler = FileHandler()

    def run(self):
        """Run the main application loop."""
        self.load_contacts()

        exit_main = False
        while not exit_main:
            self.view.show_menu()
            choice = self.view.get_user_input("Выберите действие: ")

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
                self.view.show_message("Неверный выбор. Попробуйте снова.")

    def load_contacts(self):
        """Load contacts from file."""
        try:
            self.model.contacts = self.file_handler.load_contacts(self._FILE_NAME)
        except Exception as e:
            self.view.show_error(f"Ошибка при загрузке контактов: {str(e)}")

    def show_all_contacts(self):
        """Display all contacts in the book."""
        self.view.show_contacts(self.model.contacts)

    def find_contact(self):
        """Find and display a specific contact."""
        phone = self.view.get_user_input("Введите номер телефона: ")
        contact = self.model.find_contact(phone)
        if contact:
            self.view.show_contact(contact)
        else:
            self.view.show_message("Контакт не найден.")

    def add_contact(self):
        """Add a new contact to the book."""
        name = self.view.get_user_input("Введите имя: ")
        phone = self.view.get_user_input("Введите номер телефона: ")
        email = self.view.get_user_input("Введите email: ")
        try:
            new_contact = Contact(name, phone, email)
            self.model.add_contact(new_contact)
            self.view.show_message("Контакт успешно добавлен.")
        except ContactAlreadyExistsError:
            self.view.show_error("Контакт с таким номером телефона уже существует.")

    def edit_contact(self):
        """Edit an existing contact."""
        phone = self.view.get_user_input("Введите номер телефона контакта для редактирования: ")
        contact = self.model.find_contact(phone)
        if contact:
            name = self.view.get_user_input("Введите новое имя (или оставьте пустым для сохранения текущего): ")
            email = self.view.get_user_input("Введите новый email (или оставьте пустым для сохранения текущего): ")
            if name:
                contact.name = name
            if email:
                contact.email = email
            self.view.show_message("Контакт успешно отредактирован.")
        else:
            self.view.show_error("Контакт не найден.")

    def delete_contact(self):
        """Delete a contact from the book."""
        phone = self.view.get_user_input("Введите номер телефона контакта для удаления: ")
        try:
            self.model.delete_contact(phone)
            self.view.show_message("Контакт успешно удален.")
        except ContactNotFoundError:
            self.view.show_error("Контакт не найден.")

    def save_and_exit(self):
        """Save contacts to file and exit the application."""
        try:
            self.file_handler.save_contacts(self._FILE_NAME, self.model.contacts)
            self.view.show_message("Контакты сохранены. Выход из программы.")
        except Exception as e:
            self.view.show_error(f"Ошибка при сохранении контактов: {str(e)}")