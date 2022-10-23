import read
import view
import write

# после того как совпадения по запросу пользователя нашлись эти совпадения мы отправляем ему списком, предлагаем ему выбрать из списка одну позицию 
# и его выбор запоминаем, как одну переменную - 1
# и обращаемся к элементу списка по новому индексу. переменная, которую нам ввел пользователь, является индексом

data = [{ 'id' : 1, 'last_name': 'Иванов', 'firs_tname': 'Иван Петрович' , 'position': 'генеральный директор', "phone_number": '111', "salary": 1000.0},
{ 'id' :2, 'last_name': 'Иванова', 'first_name': 'Мария Ивановна', 'position': 'главный бухгалтер', "phone_number": '222', "salary": 999.99},
{ 'id' :3, 'last_name': 'Иванов', 'first_name': 'Иван Иванович', 'position': 'менеджер', "phone_number": '333', "salary": 888.88},
{ 'id' :4, 'last_name': 'Петров', 'first_name': 'Петр', 'position': 'работник', "phone_number": '444', "salary": 150.0},
{ 'id' :5, 'last_name': 'Сидоров', 'first_name': 'Сидор Петрович', 'position': 'сторож', "phone_number": '555', "salary": 250.0},
{ 'id' :6, 'last_name': 'Шишкин', 'first_name': 'Анатолий', 'position': 'преподаватель', "phone_number": '666', "salary": 1000000.0}]
what_find = 'Иванов'
user_string = 'Костылев Кирилл Андревич программист +7325252223 99999999'
user_list = ['Иванов', "Иван Иванович", 'генеральный директор', '111', 1000.0]
key_data = ['id', 'last_name', 'firs_tname', 'position', "phone_number", "salary"]
def last_id():
    id_list = [i["id"] for i in data]
    return max(id_list)



# Найти сотрудника
def find_what_empl(what_find): #только одно слово - фамилия
    return [i for i in data if i['last_name'] == what_find]            
print(len(find_what_empl('')))
# Сделать выборку сотрудников по должности
def select_position(select_pos):
    return [i for i in data if i['position'] == select_pos]
# Сделать выборку сотрудников по зарплате
def select_salary_empl(select_salary):
    return[i for i in data if i['salary'] == select_salary]
# Создание нового сотрудника
def new_emple_create(user_list, data):
    last_name = user_list[0]
    if len(find_what_empl(last_name)) != 0:
        print("Похожий сотрудник есть! ")
        print(find_what_empl(last_name))
        print('Хотите изменить строчку? ') # Логику использовать во view
        user_choose = int(input('Добавить - 1, изменить строчку - 2: '))
        if user_choose == 1:
            empl_add_data(user_list, data)
        elif user_choose == 2:
            id_new = int(input(("Введите id строки, которую надо изменить: ")))
            index = -1
            for i in range(len(data)):
                if data[i]["id"] == id_new:
                    index = i
                    print(i)
                    # last_name[] = user_list[id_new]
    else:
         empl_add_data(user_list, data)

new_emple_create(user_list, data)
# Добавление сотрудника без проверки
def empl_add_data(user_list, data):
    new_empl = dict(zip(key_data, user_list))
    return data.append(new_empl)

# Удалить сотрудника (по тому же принципу)
def delet_what_empl(user_list, data):
    last_name = user_list[0]
    if len(find_what_empl(last_name)) != 0:
        print("Похожий сотрудник есть")
        print(find_what_empl(last_name))
        print('Какую строчку вы хотите удалить? Введите id строчки') # Логику использовать во view
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        return [i for i in data if i['id'] != user_choose]
    else:
        print("Похожий сотрудник не найден!")


def choose_what_empl(user_list, data):
    last_name = user_list[0]
    user_dict = dict(zip(key_data, user_list))
    if len(find_what_empl(last_name)) != 0:
        print("Похожий сотрудник есть")
        print(find_what_empl(last_name))
        print('Какую строчку вы хотите удалить? Введите id строчки') # Логику использовать во view
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        return [i if i['id'] != user_choose else user_dict for i in data]
    else:
        print("Похожий сотрудник не найден!")
