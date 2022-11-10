
key_data = ['id', 'last_name', 'firs_tname', 'position', "phone_number", "salary"]


def last_id(data):
    id_list = [i["id"] for i in data if type(i["id"]) is int]
    return max(id_list)


# Найти сотрудника

def find_what_empl(what_find, data): #только одно слово - фамилия
    return [i for i in data if i['last_name'] == what_find]


# Сделать выборку сотрудников по должности
def select_position(select_pos, data):
    return [i for i in data if i['position'] == select_pos]

# Сделать выборку сотрудников по зарплате


def select_salary_empl(select_salary, data):
    return[i for i in data if i['salary'] == select_salary]

# Добавление сотрудника без проверки
def empl_add_data(user_list, data_new):
    new_empl = dict(zip(key_data, user_list))
    new_empl["id"] = last_id(data_new) + 1
    return data_new.append(new_empl)

# Создание нового сотрудника
def new_emple_create(user_list, data_new):
    last_name = user_list[1]
    if len(find_what_empl(last_name, data_new)) != 0:
        print("Похожий сотрудник есть! ")
        print(find_what_empl(last_name, data_new))
        print('Хотите изменить строчку? ') # Логику использовать во view
        user_choose = int(input('Добавить - 1, изменить строчку - 2: '))

        if user_choose == 1:
            empl_add_data(user_list, data_new)
        elif user_choose == 2:
            id_old = int(input(("Введите id строки, которую надо изменить: ")))
            index_el = 0
            for i in range(len(data_new)):
                if data_new[i]["id"] == id_old:
                    index_el = i
                    break
            new_empl = dict(zip(key_data, user_list))
            new_empl["id"] = id_old
            data_new[index_el] = new_empl
    else: empl_add_data(user_list, data_new)


# Удалить сотрудника (по тому же принципу)
def delet_what_empl(del_empl, data):

    if len(find_what_empl(del_empl, data)) != 0:
        print("Похожий сотрудник есть")
        print(find_what_empl(del_empl, data))
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        index_el = None
        for i in range(len(data)):
            if data[i]["id"] == user_choose:
                index_el = i
                break
        del data[index_el]
    else:
        print("Похожий сотрудник не найден!")


def choose_what_empl(edit, data): # добавили переменную edit из view, в которой находятся данные от пользователя
    last_name = edit[1]
    if len(find_what_empl(last_name, data)) != 0:
        print("Похожий сотрудник есть")
        print(find_what_empl(last_name, data))
        print('Какую строчку вы хотите удалить? Введите id строчки') # Логику использовать во view
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        index_el = 0
        for i in range(len(data)):
            if data[i]["id"] == user_choose:
                index_el = i
                break
        new_empl = dict(zip(key_data, edit))
        new_empl["id"] = user_choose
        data[index_el] = new_empl
    else:
        print("Похожий сотрудник не найден!")
