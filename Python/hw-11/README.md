# Contact Book Application

This console application is designed to manage a contact book. It allows you to store, view, edit, and delete contacts. The application follows the Model-View-Controller (MVC) pattern to ensure a clear separation of concerns.

## Functionality

The application provides the following functionalities:

1.  Show all contacts
2.  Find a contact by phone number
3.  Create a new contact
4.  Edit an existing contact
5.  Delete a contact
6.  Save changes and exit

## Installation and Setup

1.  Download the project files.
2.  Open a terminal and navigate to the project directory.
3.  Run the program using the command:

    ```
    python main.py
    ```

## Usage

After starting the program, you will see a menu with available actions. Enter the number of the action and follow the on-screen instructions.

*   To view all contacts, select option `1`.
*   To find a contact, select option `2` and enter the phone number.
*   To create a new contact, select option `3` and enter the requested information.
*   To edit a contact, select option `4` and follow the prompts.
*   To delete a contact, select option `5` and enter the phone number.
*   To save changes and exit, select option `6`.

## Data Storage

Contacts are stored in the `contact_book.json` file in the same directory as the script. Upon startup, the program automatically loads existing contacts from this file if it exists. Ensure that you have read and write permissions in the directory where the script is located so that the program can correctly save and load data.

## Project Structure

The project is structured into the following modules:

*   `model.py`: Contains the data model and business logic.
*   `view.py`: Handles the user interface.
*   `controller.py`: Manages the flow of the application.
*   `exceptions.py`: Defines custom exception classes.
*   `file_handler.py`: Handles file operations for loading and saving contacts.
*   `main.py`: The entry point of the application.

## Class and Method Documentation

### model.py

#### Contact Class

Represents a single contact in the contact book.

*   **`__init__(self, name: str, phone: str, email: str)`**

    *   Initializes a new contact.
    *   Parameters:
        *   `name` (str): The name of the contact.
        *   `phone` (str): The phone number of the contact.
        *   `email` (str): The email address of the contact.

*   **`__repr__(self)`**

    *   Returns a string representation of the Contact object for debugging.

#### ContactBook Class

A class representing a contact book, implemented as a Singleton.

*   **`__new__(cls)`**

    *   Creates a new instance of ContactBook if it doesn't exist, otherwise returns the existing instance.
    *   Returns: The single instance of the ContactBook.

*   **`add_contact(self, contact: Contact) -> None`**

    *   Adds a new contact to the contact book.
    *   Parameters:
        *   `contact` (Contact): The contact to be added.
    *   Raises:
        *   `ContactAlreadyExistsError`: If a contact with the same phone number already exists.

*   **`find_contact(self, phone: str) -> Contact | None`**

    *   Finds a contact by phone number.
    *   Parameters:
        *   `phone` (str): The phone number to search for.
    *   Returns: The found contact, or `None` if not found.

*   **`edit_contact(self, phone: str, name: str, email: str) -> None`**

    *   Edits an existing contact's information.
    *   Parameters:
        *   `phone` (str): The phone number of the contact to edit.
        *   `name` (str): The new name for the contact.
        *   `email` (str): The new email for the contact.
    *   Raises:
        *   `ContactNotFoundError`: If the contact with the specified phone number is not found.

*   **`delete_contact(self, phone: str) -> None`**

    *   Deletes a contact from the contact book.
    *   Parameters:
        *   `phone` (str): The phone number of the contact to delete.
    *   Raises:
        *   `ContactNotFoundError`: If the contact with the specified phone number is not found.

*   **`get_all_contacts(self) -> dict[str, Contact]`**

    *   Gets all contacts in the contact book.
    *   Returns: A dictionary of all contacts.

### view.py

#### ContactView Class

Handles the user interface for the contact book application.

*   **`show_menu() -> None`**

    *   Displays the main menu of the application.

*   **`get_user_input(prompt: str) -> str`**

    *   Gets input from the user.
    *   Parameters:
        *   `prompt` (str): The prompt to display to the user.
    *   Returns: The user's input.

*   **`show_contact(contact: Contact) -> None`**

    *   Displays a single contact.
    *   Parameters:
        *   `contact` (Contact): The contact to display.

*   **`show_message(message: str) -> None`**

    *   Displays a message to the user.
    *   Parameters:
        *   `message` (str): The message to display.

*   **`show_contacts(contacts: dict[str, Contact]) -> None`**

    *   Displays all contacts.
    *   Parameters:
        *   `contacts` (dict[str, Contact]): A collection of contacts to display.

*   **`show_error(error_message: str) -> None`**

    *   Displays an error message to the user.
    *   Parameters:
        *   `error_message` (str): The error message to display.

### controller.py

#### ContactController Class

Controls the flow of the contact book application.

*   **`__init__(self, model: ContactBook, view: ContactView)`**

    *   Initializes the contact controller.
    *   Parameters:
        *   `model` (ContactBook): The contact book model.
        *   `view` (ContactView): The view for user interaction.

*   **`run(self)`**

    *   Runs the main application loop.

*   **`load_contacts(self)`**

    *   Loads contacts from file.

*   **`show_all_contacts(self)`**

    *   Displays all contacts in the book.

*   **`find_contact(self)`**

    *   Finds and displays a specific contact.

*   **`add_contact(self)`**

    *   Adds a new contact to the book.

*   **`edit_contact(self)`**

    *   Edits an existing contact.

*   **`delete_contact(self)`**

    *   Deletes a contact from the book.

*   **`save_and_exit(self)`**

    *   Saves contacts to file and exits the application.

### exceptions.py

Defines custom exception classes for the application.

*   **`ContactBookError(Exception)`**

    *   Base exception class for ContactBook errors.

*   **`InvalidDataFormatError(ContactBookError)`**

    *   Exception raised when the data format in the file is invalid.

*   **`ContactNotFoundError(ContactBookError)`**

    *   Exception raised when a contact is not found.

*   **`ContactAlreadyExistsError(ContactBookError)`**

    *   Exception raised when trying to add a contact that already exists.

### file\_handler.py

#### FileHandler Class

Handles file operations for saving and loading contacts.

*   **`load_contacts(filename: str) -> dict[str, Contact]`**

    *   Loads contacts from a JSON file.
    *   Parameters:
        *   `filename` (str): The name of the file to load from.
    *   Returns: A dictionary of loaded contacts.
    *   Raises:
        *   `InvalidDataFormatError`: If the data format in the file is invalid.

*   **`save_contacts(filename: str, contacts: dict[str, Contact]) -> None`**

    *   Saves contacts to a JSON file.
    *   Parameters:
        *   `filename` (str): The name of the file to save to.
        *   `contacts` (dict[str, Contact]): The contacts to save.

### main.py

*   The entry point of the application.
*   Creates instances of `ContactBook`, `ContactView`, and `ContactController` and starts the application.