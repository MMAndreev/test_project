"""
Справочник
"""


from csv import DictReader, DictWriter
from os.path import exists


class Name_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Phone_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_user_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите Имя: ")
            if len(first_name) < 2:
                raise Name_Error('Невалидная длинна!')
            last_name = input("Введите Фамилию: ")
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) < 11:
                raise Phone_Error('Неверная длинна номера!')
            end = input("Закончить ввод?")
            if end == 'Да':
                flag = True
        except ValueError:
            print("Вы вводите символы вместо цифр!")
            continue
        except Name_Error as err:
            print(err)
            continue
        except Phone_Error as err:
            print(err)
            continue
    return first_name, last_name, phone_number


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


file_name = 'phone.csv'
file_name_2 = 'phone_2.csv'

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    user_data = get_user_data()
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(user_data[2]):
            print("Такой пользователь уже существует!")
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_file(file_name, file_name_2):
    list_1 = list(read_file(file_name))
    str_2 = int(input(f"Выберите номер строки с 1 по {len(list_1)}: "))
    res_2 = [list_1[str_2 - 1]]
    with open(file_name_2, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res_2)

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print("Данные успешно записаны.")
        elif command == "r":
            if not exists(file_name):
                print("Файл не создан! Создайте его.")
                continue
            print(read_file(file_name))
        elif command == "c":
            copy_file(file_name, file_name_2)


main()
