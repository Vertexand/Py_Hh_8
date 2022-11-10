import view
import read
import additional
import write

empl_data = read.read_json()
def main_logic():
    # в additional закоментировали 56 строчку./ не пушить additional!
    pos = 2
    while 1 < pos < 14:
        pos = view.select_action()
        if pos == 11:
            what_find = view.find_empl()
            data_to_print = additional.find_what_empl(what_find, empl_data)
            view.print_all_contacts(data_to_print)
        if pos == 12:
            what_find = view.select_empl_position()
            data_to_print = additional.select_position(what_find, empl_data)
            view.print_all_contacts(data_to_print)
        if pos == 13:
            what_find = view.select_empl_salary()
            data_to_print = additional.select_salary_empl(what_find, empl_data)
            view.print_all_contacts(data_to_print)
        if pos == 2:
            what_find = view.add_empl()
            data_to_print = additional.find_what_empl(what_find['last_name'], empl_data)
            view.print_all_contacts(data_to_print)
            additional.new_emple_create(list(what_find.values()), empl_data)
            view.print_all_contacts(empl_data)
            write.write_json(empl_data)
            write.write_csv(empl_data)
        if pos == 3:
            what_find = view.delete_empl()
            additional.delet_what_empl(what_find, empl_data)
            view.print_all_contacts(empl_data)
            write.write_json(empl_data)
            write.write_csv(empl_data)
        if pos == 4:
            empl_list = list(view.edit_empl_data().values())
            additional.choose_what_empl(empl_list, empl_data)
            view.print_all_contacts(empl_data)
            print(empl_data)
            write.write_json(empl_data)
            write.write_csv(empl_data)
        if pos == 5:
            what_save = view.export_data()
            if what_save == 1:
                write.write_json(empl_data)
            elif what_save == 2:
                write.write_csv(empl_data)
            else:
                print('Некорректный ввод')
        if pos == 6:
            view.print_all_contacts(empl_data)
        if pos == 7:
            view.end_work()
            break
