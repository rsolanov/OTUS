# Testing and Debugging a Contact Book Application

This project focuses on writing and running tests for a contact book application using `pytest`. 
The goal is to ensure that all key functionalities of the application are covered by tests, including edge cases and exception handling.

## Installation and Setup

1.  Download the project files.
2.  Open a terminal and navigate to the project directory.
3.  Install requirements using the command:

    ```
    pip install --no-cache-dir -r requirements.txt
    ```

4.  To run the tests, use the following command:

    ```
    pytest test_contact_book.py
    ```


## Test Coverage

The tests cover the following functionalities:

- Adding a contact.
- Finding a contact by phone number.
- Editing an existing contact.
- Deleting a contact.
- Handling exceptions (e.g., adding a duplicate contact, editing/deleting a non-existent contact).
- Loading and saving contacts from/to a file.

## Test File: `test_contact_book.py`

The test file contains unit tests for the contact book application. Below is an overview of the test cases:

### Fixtures

- `contact_book`: Provides a clean instance of `ContactBook` for each test.
- `file_handler`: Provides an instance of `FileHandler` for file operations.

### Test Cases

1. **Adding a Contact**:
   - Verifies that a new contact can be added to the contact book.

2. **Adding a Duplicate Contact**:
   - Ensures that adding a contact with an existing phone number raises a `ContactAlreadyExistsError`.

3. **Finding a Contact**:
   - Tests the ability to find a contact by phone number.

4. **Finding a Non-Existent Contact**:
   - Verifies that searching for a non-existent contact returns `None`.

5. **Editing a Contact**:
   - Tests updating the name and email of an existing contact.

6. **Editing a Non-Existent Contact**:
   - Ensures that editing a non-existent contact raises a `ContactNotFoundError`.

7. **Deleting a Contact**:
   - Tests the removal of a contact from the contact book.

8. **Deleting a Non-Existent Contact**:
   - Verifies that deleting a non-existent contact raises a `ContactNotFoundError`.

9. **Loading Contacts from a File**:
   - Tests loading contacts from a JSON file.

10. **Saving Contacts to a File**:
    - Tests saving contacts to a JSON file.

11. **Handling Invalid Data Format**:
    - Ensures that loading a file with invalid data format raises an `InvalidDataFormatError`.

## Requirements

- Python 3.8 or higher.
- Dependencies listed in `requirements.txt`.