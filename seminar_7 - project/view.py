def error(error):
    print("Введенное значение должно равняться 1 или 2")
    if error == 1:
        global action
        action = int(input())
    else:
        global file_format
        file_format = int(input())

def show_users(data):
    print(data)

def add_user():
    print("Введите данные пользователя в формате 'Фамилия, Имя, Телефон, Описание'")
    return input()

action = int(input("Справочник\nВыберите действие:\n1. Показать контакты\n2. Добавить контакт\n"))
if action == 1:
    file_format = int(input("Выберите формат файла:\n1.\nФамилия\nИмя\nТелефон\nОписание\n2. Фамилия, Имя, Телефон, Описание\n"))