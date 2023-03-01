# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1.Программа должна выводить данные
# 2.Программа должна сохранять данные в текстовом файле
# 3.Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4.Использование функций. Ваша программа не должна быть линейной

# модули
# импорт данных в TXT
# экспорт данных в TXT
# внесение записи через консоль
# изменение и удаление записи через консоль
# поиск записи по любому вхождению
# user interface

# формат словаря:
# id surname name fathers_name tel

def main_import_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
        # print(phonebook)

def import_contacts(some_string):
    finded_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(phonebook[i])
    return finded_contacts        


def export_contacts(new_contact):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
        # s = ' '.join(new_line)
        data.writelines(' '.join(new_contact) + '\n')
    

def input_contacts():
    new_contact = [input('surname: ')]
    new_contact.append(input('name: '))
    new_contact.append(input('given name: '))
    new_contact.append(input('phone number: '))
    
    export_contacts(new_contact)

def find_contact():
    s = import_contacts(input('whadda we search?: '))
    print(*s)

def user_interface():
    main_import_contacts()
    print('phonebook\nwhadda want?\n1 - add contact\n2 - find contact\n3 - print whole book\nany other input - end program')
    user_input = input('your choice: ')
    while user_input in ('1', '2', '3'):
        if user_input == 1:
            input_contacts()
        elif user_input == '2':
            find_contact()
        elif user_input == '3':
            print()
            for i in phonebook:
                print(*phonebook[i])
        user_input = input('\nyour choice: ')

    print('bye')          


phonebook = dict()
user_interface()

    




