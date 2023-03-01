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

def import_contacts():
    phonebook = dict()
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
        print(phonebook)


def export_contacts(new_line):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
        # s = ' '.join(new_line)
        data.writelines(' '.join(new_line))
    

def input_contacts():
    new_contact = input('new contact: ').split()
    # потом проверка ввода
    print(new_contact)
    export_contacts(new_contact)

def find_contact(some_string, id):
    con_to_find = input('input someone: ')

phonebook = dict()

import_contacts()
# input_contacts()

    




