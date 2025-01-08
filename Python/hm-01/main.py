import json
import os

CONTACTS: dict[str, tuple[str, str]]
FILE_NAME: str = 'contact_book.json'


def init() -> dict[str, tuple[str, str]]:
    """
    Initialize the contacts dictionary from a JSON file if it exists.

    Returns:
        dict[str, tuple[str, str]]: A dictionary of contacts loaded from the file or an empty dictionary.

    Raises:
            ValueError: If the JSON data is not in the expected format.
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            try:
                return {
                    str(k): (str(v[0]), str(v[1]))
                    for k, v in data.items()
                }
            except (IndexError, TypeError):
                raise ValueError('Invalid data format in JSON file')
    return {}


def save() -> None:
    """
    Save the current contacts dictionary to a JSON file.
    """
    with open(FILE_NAME, 'w', encoding='UTF-8') as file:
        json.dump(CONTACTS, file, indent=2, ensure_ascii=False)


def contact_show_list() -> None:
    """
    Display the entire list of contacts.
    """
    print(' | '.join(key for key in ['name', 'phone', 'email']))

    for phone, (name, email) in CONTACTS.items():
        print(f'{name} | {phone} | {email}')

    print(f'Total: {len(CONTACTS)} rows')
    print()


def contact_find() -> None:
    """
    Find and display a contact by phone number.
    """
    phone: str = input('Enter phone: ')
    if phone not in CONTACTS:
        print('Contact with that number not exists')
    else:
        name, email = CONTACTS[phone]
        print(' | '.join(key for key in ['name', 'phone', 'email']))
        print(f'{name} | {phone} | {email}')
    print()


def contact_add() -> None:
    """
    Add a new contact to the dictionary.
    """
    phone: str = input('Enter phone: ')
    if phone in CONTACTS:
        print('Contact with that number already exists')
    else:
        name: str = input('Enter name: ')
        email: str = input('Enter email: ')
        CONTACTS[phone] = (name, email)
        print('New contact has been added successfully')
    print()


def contact_edit() -> None:
    """
    Edit an existing contact in the dictionary.
    """
    phone: str = input('Enter phone: ')
    if phone not in CONTACTS:
        print('Contact with that number not exists')
    else:
        name: str = input('Enter new name: ')
        email: str = input('Enter new email: ')
        CONTACTS[phone] = (name, email)
        print('Contact has been edited successfully')
    print()


def contact_delete() -> None:
    """
    Delete an existing contact from the dictionary.
    """
    phone: str = input('enter phone: ')
    if phone not in CONTACTS:
        print('Contact with that number not exists')
    else:
        CONTACTS.pop(phone)
        print('Contact has been deleted successfully')
    print()


def main() -> None:
    """
    Main function to run the contact book application.
    Handles user input and calls appropriate functions based on user choice.
    """
    global CONTACTS
    CONTACTS = init()
    actions = {
        1: 'Show the entire list',
        2: 'Find existing contact',
        3: 'Create new contact',
        4: 'Edit existing contact',
        5: 'Delete existing contact',
        6: 'Exit'
    }

    exit_main = False
    while not exit_main:
        print('Enter the action number: ')
        for num, item in actions.items():
            print(f'{num}: {item}')
        try:
            num = int(input('Enter num, then press Enter: '))

            if num in actions.keys():
                print(f'OK. Action selected: {actions[num]}')
                if num == 1:
                    contact_show_list()
                elif num == 2:
                    contact_find()
                elif num == 3:
                    contact_add()
                elif num == 4:
                    contact_edit()
                elif num == 5:
                    contact_delete()
                else:
                    save()
                    exit_main = True
            else:
                print('Invalid action. Please try again.')
                print()
        except ValueError:
            print('This is not a number. Please try again.')
            print()


if __name__ == "__main__":
    main()