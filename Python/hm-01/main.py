import json
import os

contacts: dict[str, tuple]
file_name:str = 'contact_book.json'

def init():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            return {k: tuple(v) for k, v in json.load(file).items()}
    return {}

def save():
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(contacts, file, indent=2)

def contact_show_list():
    print(' | '.join(key for key in ['name', 'phone', 'email']))

    for phone, (name, email) in contacts.items():
        print(f'{name} | {phone} | {email}')

    print(f'total: {len(contacts)} rows')
    print()

def contact_find():
    phone: str = input('enter phone: ')
    if phone not in contacts.keys():
        print('contact with that number not exists')
    else:
        name, email = contacts[phone]
        print(' | '.join(key for key in ['name', 'phone', 'email']))
        print(f'{name} | {phone} | {email}')
    print()

def contact_add():
    phone: str = input('enter phone: ')
    if phone in contacts.keys():
        print('contact with that number already exists')
    else:
        name: str = input('enter name: ')
        email: str = input('enter email: ')
        contacts[phone] = (name, email)
        print(f'new contact has been added successfully')
    print()

def contact_edit():
    phone: str = input('enter phone: ')
    if phone not in contacts.keys():
        print('contact with that number not exists')
    else:
        name: str = input('enter new name: ')
        email: str = input('enter new email: ')
        contacts[phone] = (name, email)
        print(f'contact has been edited successfully')
    print()

def contact_delete():
    phone: str = input('enter phone: ')
    if phone not in contacts.keys():
        print('contact with that number not exists')
    else:
        contacts.pop(phone)
        print(f'contact has been deleted successfully')
    print()

def main():
    global contacts
    contacts = init()
    actions = {
        1: 'Show the entire list',
        2: 'Find existing contact',
        3: 'Create new contact',
        4: 'Edit existing contact',
        5: 'Delete existing contact',
        6: 'Exit'
   }

    while True:
        print('Enter the action number: ')
        for num, item in actions.items():
            print(f'{num}: {item}')
        try:
            num = int(input('enter num, then press Enter: '))

            if num in actions.keys():
                print(f'ok. Action selected: {actions[num]}')
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
                    return
            else:
                print('Invalid action. Please try again.')
                print()
        except ValueError:
            print('This is not a number. Please try again.')
            print()

main() 