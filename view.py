from tabulate import tabulate


def select_action() -> int:
    print("Выберите необходимое действие")
    print("1. Поиск сотрудника")
    print("2. Добавить сотрудника")
    print("3. Удалить сотрудника")  
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
    

def find_empl():
    search_empl = input("Введите фамилию сотрудника: ") 
    return search_empl



def select_empl_position():
    select_pos = input("Введите искомую позицию: ")
    return select_pos


def select_empl_salary():
    select_salary = input("Введите зарплату: ")
    return select_salary


def add_empl():
    print("Добавьте сотрудника: ")
    archive = {"id": ""}
    archive["last_name"] = (input("Введите фамилию сотрудника: "))
    archive["first_name"] = (input("Введите имя сотрудника: "))
    archive["position"] = (input("Введите должность сотрудника: "))
    archive["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    archive["salary"] = (input("Введите зарплату сотрудника: "))
    return archive



def delete_empl():
    del_empl = input("Введите фамилию сотрудника, которого хотите удалить: ")
    return del_empl


def edit_empl_data():
    print("Введите все данные сотрудника")
    edit = {"id": ""}
    edit["last_name"] = (input("Введите фамилию сотрудника: "))
    edit["first_name"] = (input("Введите имя сотрудника: "))
    edit["position"] = (input("Введите должность сотрудника: "))
    edit["phone_number"] = (input("Введите телефонный номер сотрудника: "))
    edit["salary"] = (input("Введите зарплату сотрудника: "))
    return edit



def export_data():
    return int(input("Введите 1 для экспорта в формате json или 2 для экспорта в формате csv: "))



def end_work():
    print("Программа завершена")



def print_all_contacts(data):
    data_to_print = []

    for i in range(len(data)):
        listik = list(data[i].values())
        listik.pop(0)
        data_to_print.append(listik)

    col_names = ["Фамилия", "Имя Отчество", "Должность", "Телефон", "Зарплата"]
    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))
