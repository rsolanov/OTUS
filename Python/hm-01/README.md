# Телефонный справочник

Это консольное приложение предназначено для управления телефонным справочником. 
Оно позволяет сохранять, просматривать, редактировать и удалять контакты.

## Функциональность

Приложение предоставляет следующие возможности:

1. Показать все контакты
2. Найти контакт по номеру телефона
3. Создать новый контакт
4. Изменить существующий контакт
5. Удалить контакт
6. Сохранить изменения и выйти

## Установка и запуск

1. Cкачайте файлы проекта;

2. Откройте терминал и перейдите в директорию проекта;

3. Запустите программу командой:
python main.py

## Использование

После запуска программы вы увидите меню с доступными действиями. 
Введите номер действия и следуйте инструкциям на экране.

- Для просмотра всех контактов выберите опцию 1;
- Для поиска контакта выберите опцию 2 и введите номер телефона;
- Для создания нового контакта выберите опцию 3 и введите запрашиваемую информацию;
- Для редактирования контакта выберите опцию 4 и следуйте подсказкам;
- Для удаления контакта выберите опцию 5 и введите номер телефона;
- Для сохранения изменений и выхода выберите опцию 6.

## Хранение данных

Контакты сохраняются в файл `contact_book.json` в той же директории, где находится скрипт. 
При запуске программа автоматически загружает существующие контакты из этого файла, если он существует.
Убедитесь, что у вас есть права на чтение и запись в директории, где находится скрипт, чтобы программа могла корректно сохранять и загружать данные.

# Project Documentation

## init

Initialize the contacts dictionary from a JSON file if it exists.

Returns:
    dict[str, tuple[str, str]]: A dictionary of contacts loaded from the file or an empty dictionary.

Raises:
        ValueError: If the JSON data is not in the expected format.

## save

Save the current contacts dictionary to a JSON file.

## contact_show_list

Display the entire list of contacts.

## contact_find

Find and display a contact by phone number.

## contact_add

Add a new contact to the dictionary.

## contact_edit

Edit an existing contact in the dictionary.

## contact_delete

Delete an existing contact from the dictionary.

## main

Main function to run the contact book application.
Handles user input and calls appropriate functions based on user choice.