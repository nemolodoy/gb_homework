""" 
Акунец Даниил

Делал домашнее задание из презентации. 
Добавил функционал для ввода данных с клавиатуры 

"""

def load_data(filename='phonebook.txt'):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            data = [line.strip().split(',') for line in lines]
            phonebook = [{'Номер записи': entry[0], 'Фамилия': entry[1], 'Имя': entry[2], 'Отчество': entry[3], 'Номер телефона': entry[4]} for entry in data]
        return phonebook
    except FileNotFoundError:
        return []
    
def add_entry(data):
    new_entry = {'Номер записи': len(data) + 1,
                 'Фамилия': input("Введите фамилию: "),
                 'Имя': input("Введите имя: "),
                 'Отчество': input("Введите отчество: "),
                 'Номер телефона': input("Введите номер телефона: ")}
    data.append(new_entry)
    print("Новая запись добавлена.")

def save_data(data, filename='phonebook.txt'):
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry['Номер записи']},{entry['Фамилия']},{entry['Имя']},{entry['Отчество']},{entry['Номер телефона']}\n")

def update_data(data, entry_number, updated_entry):
    data[entry_number - 1] = updated_entry

def delete_data(data, entry_number):
    del data[entry_number - 1]

def display_data(data):
    if not data:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for entry in data:
            print(f"{entry['Номер записи']}. {entry['Фамилия']} {entry['Имя']} {entry['Отчество']}: {entry['Номер телефона']}")
        print()

def search_data(data, key, value):
    result = [entry for entry in data if entry[key].lower() == value.lower()]
    return result


def main():
    phonebook = load_data()

    while True:
        print("1. Вывести данные")
        print("2. Сохранить данные")
        print("3. Поиск записи")
        print("4. Изменение данных")
        print("5. Удаление данных")
        print("6. Добавить новую запись")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            display_data(phonebook)
        elif choice == '2':
            save_data(phonebook)
            print("Данные сохранены.")
        elif choice == '3':
            search_key = input("Введите характеристику для поиска (Фамилия, Имя, Отчество): ")
            search_value = input(f"Введите значение для поиска {search_key}: ")
            search_result = search_data(phonebook, search_key, search_value)
            display_data(search_result)
        elif choice == '4':
            entry_number = int(input("Введите номер записи для изменения: "))
            if 1 <= entry_number <= len(phonebook):
                updated_entry = {'Номер записи': entry_number,
                                 'Фамилия': input("Введите новую фамилию: "),
                                 'Имя': input("Введите новое имя: "),
                                 'Отчество': input("Введите новое отчество: "),
                                 'Номер телефона': input("Введите новый номер телефона: ")}
                update_data(phonebook, entry_number, updated_entry)
                print(f"Запись {entry_number} изменена.")
            else:
                print("Неверный номер записи.")
        elif choice == '5':
            entry_number = int(input("Введите номер записи для удаления: "))
            if 1 <= entry_number <= len(phonebook):
                delete_data(phonebook, entry_number)
                print(f"Запись {entry_number} удалена.")
            else:
                print("Неверный номер записи.")
        elif choice == '6':
            add_entry(phonebook)
        elif choice == '7':
            save_data(phonebook)
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")


if __name__ == "__main__":
    main()
