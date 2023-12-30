# Открыть файл
# Сохранить файл
# Создание контакта
# Изменить контакт
# Найти контакт
# Удалить контакт
# Показать контакт
# Выход


def menu_app():
    file_name = "Contact.txt"
    print("1. Создать контакт")
    print("2. Изменить контакт")
    print("3. Найти контакт")
    print("4. Удалить контакт")
    print("5. Показать контакты")
    print("6. Выход")
    choise = int(input("Что вы хотите сделать?: "))
    if choise == 1:
        create_contact(file_name)
        extension = input("Для продолжения работы нажмите Enter ...")
        menu_app()
    elif choise == 5:
        show_contacts(file_name)
        extension = input("Для продолжения работы нажмите Enter ...")
        menu_app()
    elif choise == 3:
        find_contact(file_name)
        extension = input("Для продолжения работы нажмите Enter ...")
        menu_app()
    elif choise == 2:
        change_contact(file_name)
        extension = input("Для продолжения работы нажмите Enter ...")
        menu_app()
    elif choise == 4:
        delete_contact(file_name)
        extension = input("Для продолжения работы нажмите Enter ...")
        menu_app()




def create_contact(file_name):
    contact = get_input_contact(file_name)
    with open(file_name, "a+", encoding='UTF-8') as file_contact:
        file_contact.writelines("; ".join(contact) + '\n')
    print("Контакт сохранен!")


def show_contacts(file_name):
    with open(file_name, "r", encoding='UTF-8') as file_contact:
        for line in file_contact:
            print(line.rstrip())


def change_contact(file_name):
    with open(file_name, "r", encoding='UTF-8') as file_contact:
        lines = file_contact.readlines()
    for line in lines:
        print(line.rstrip())
    id_for_change = int(input("Введите индекс контакта для изменения: "))
    if 0 <= id_for_change <= len(lines):
        contact = get_input_contact(file_name)
        contact[0] = str(id_for_change)
        contact = "; ".join(contact) + '\n'
        lines[id_for_change] = contact
    with open(file_name, "w", encoding='UTF-8') as file_contact:
        file_contact.writelines(lines)


def count_contact(file_name):
    with open(file_name, "r", encoding='UTF-8') as file_contact:
        return sum([1 for line in file_contact])


def get_input_contact(file_name):
    count = count_contact(file_name)
    information = list()
    information.append(str(count))
    information.append(input("Введите имя контакта: "))
    information.append(input("Введите номер телефона контакта: "))
    information.append(input("Введите электронный адрес: "))
    return information



def find_contact(file_name):
    name = input("Введите имя человека: ")
    with open(file_name, "r", encoding='UTF-8') as file_contact:
        lines = file_contact.readlines()
    for line in lines:
        if name in line:
            print(line)



def delete_contact(file_name):
    show_contacts(file_name)
    position = int(input("Введите индекс контакта, который хотите удалить: "))
    with open(file_name, "r", encoding='UTF-8') as contact_file:
        lines = contact_file.readlines()
        ptr = 0
    with open(file_name, "w", encoding='UTF-8') as file:
        for line in lines:
            if ptr != position:
                file.write(line)
            ptr += 1

menu_app()
















