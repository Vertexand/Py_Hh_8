from tabulate import tabulate
from tkinter import *
from select import select

# def select_action() -> int:
#     print("\n" + "=" * 20)
#     print("Выберите необходимое действие")
#     print("1. Найти сотрудника по фамилии")
#     print("2. Сделать выборку сотрудников по должности")
#     print("3. Сделать выборку сотрудников по зарплате")
#     print("4. Добавить сотрудника")
#     print("5. Удалить сотрудника")#фамилия+имя, далее должность
#     print("6. Обновить данные сотрудника")#фамилия+имя, далее должность затем список действий что обновляем по ключу
#     print("7. Экспортировать данные в формате json")
#     print("8. Экспортировать данные в формате csv")
#     print("9. Закончить работу")
#     return int(input("Введите номер необходимого действия: "))

# Тестовое окно от 19 до 34 строки (работает)
# from tkinter import *

# def hello(event):
#   print("Привет ублюдок!")

# root = Tk()
# root.title("То самое мать его первое окно")
# root.geometry("600x500")
# but1 = Button(root)
# but1["text"] = "Кнопка для приветствия"
# but1.bind("<Button-1>",hello)

# but1.pack()
# root.mainloop()
# input()


# root = Tk()  # создание главного окна
# value = StringVar()
# root.title("Главное окно")  # название главного окна
# root.geometry("600x600+700+300")  # где 400 ширина 200 высота,
# # счёт идёт от верхнего левого угла где 700 отступ слева 300 отступ вниз
# root.resizable(width=False, height=False)  # запрет на изминение размера окна
#
# l = Label(text="Добро пожаловать в тестовую версию окна")  # текст
# e = Entry(textvariable=value)  # поле ввода
# b = Button(text="Старт")  # кнопка
#
#
# def chanche_label():
#     print("hello")
#
#
# b.bind('<Button - 1>', chanche_label())
#
# # l.grid(row = 1, column = 1)
# # e.grid(row = 2, column = 1)
# # b.grid(row = 3, column = 1)
#
#
# l.pack(side=BOTTOM)
# e.pack()
# b.pack()
# root.mainloop()  # конец tkinter функции


def select_action() -> int:
    # print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Поиск сотрудника")
    print("2. Добавить сотрудника")
    print("3. Удалить сотрудника")  # фамилия+имя, далее должность
    # фамилия+имя, далее должность затем список действий что обновляем по ключу
    print("4. Обновить данные сотрудника")
    print("5. Экспортировать данные ")
    print("6. Вывести список сотрудников")
    print("7. Закончить работу")
    user_choice = int(input("Введите номер необходимого действия: "))

    if user_choice == 1:
        print("По какому критерию предпочитаете осуществить поиск сотрудника(ов)")
        print("1. Найти сотрудника по фамилии")
        print("2. Сделать выборку сотрудников по должности")
        print("3. Сделать выборку сотрудников по зарплате")
        user_choice = int(input("Введите цифру ")) + 10
        print(user_choice)
        return user_choice
    else:
        return user_choice
    # print(second_menue())


# 1. Найти сотрудника
def find_empl():
    search_empl = input("Введите фамилию сотрудника: ")  # фамилию

    return search_empl
# print(find_empl())

# 2. Сделать выборку сотрудников по должности
def select_empl_position():
    select_pos = input("Введите искомую позицию: ")
    return select_pos
# print(select_empl_position())

# 3. Сделать выборку сотрудников по зарплате
def select_empl_salary():
    select_salary = input("Введите зарплату: ")
    return select_salary
# print(select_empl_salary())


# 4. Добавить сотрудника, найден похожий сотрудник
def add_empl():
    add_somebody = input("Добавьте сотрудника: ")
    archive = {"id": ""}
    archive["last_name"] = (input("Введите фамилию сотрудника: "))
    archive["first_name"] = (input("Введите имя сотрудника: "))
    archive["position"] = (input("Введите должность сотрудника: "))
    archive["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    archive["salary"] = (input("Введите зарплату сотрудника: "))
    return add_somebody


# print(add_empl())


# 5. Удалить сотрудника
def delete_empl():
    del_empl = input("Введите фамилию сотрудника, которого хотите удалить: ")
    return del_empl


# print(delete_empl())


# 6. Обновить данные сотрудника
def edit_empl_data():
    # edit_data = input("Обновите данные сотрудника: ")
    print("Введите все данные сотрудника")
    edit = {"id": ""}
    edit["last_name"] = (input("Введите фамилию сотрудника: "))
    edit["first_name"] = (input("Введите имя сотрудника: "))
    edit["position"] = (input("Введите должность сотрудника: "))
    edit["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    edit["salary"] = (input("Введите зарплату сотрудника: "))
    return edit


# print(edit_empl_data())


# 7. Экспортировать данные в формате json/csv
def export_data():
    # print("Выберите формат экспорта файла json/csv: ")
    return int(input("Введите 1 для экспорта в формате json или 2 для экспорта в формате csv: "))

# print(export_data_json())


# # 8. Экспортировать данные в формате csv
# def export_data_csv():
#     export_csv = input("Экспортировать в csv: ")
#     return export_csv
# # print(export_data_csv())


# 9. Закончить работу
def end_work():
    print("Программа завершена")
# print(end_work())


def print_all_contacts(data):
    data_to_print = []

    for i in range(len(data)):
        listik = list(data[i].values())
        listik.pop(0)
        data_to_print.append(listik)

    col_names = ["Фамилия", "Имя Отчество", "Должность", "Телефон", "Зарплата"]
    # print(data_to_print)
    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))

# #print_all_contacts(data)


# Функционал
#     print("1. Найти сотрудника")
# def find_empl
#     print("2. Сделать выборку сотрудников по должности")
# def select_empl_position
#     print("3. Сделать выборку сотрудников по зарплате")
# def select_empl_salary
#     print("4. Добавить сотрудника")
# def add_empl
#     print("5. Удалить сотрудника")
# def delete_empl
#     print("6. Обновить данные сотрудника")
# def edit_empl_data
#     print("7. Экспортировать данные в формате json")
# def export_data_json
#     print("8. Экспортировать данные в формате csv")
# def export_data_cmv
#     print("9. Закончить работу")
# def end_work
