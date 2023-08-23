from module.edit import add_data, read_data, find_data, edit_data
from module.config import path
import sys


# Выбор пользователем пункта меню
def menu_input() -> int:
    try:
        user_input: int = int(input("Выберите пункт меню: "))
    except ValueError:
        print("\n---> Неправильный ввод. Можно вводить только цифры из меню.\n")
    else:
        return user_input


# Основное меню программы
def menu_main() -> None:
    choice = None
    while choice !=0:
        print("""
    МЕНЮ:
    
    1 - Вывести постранично данные из справочника
    2 - Добавление новой записи в справочник
    3 - Редактирование записей в справочнике
    4 - Поиск записей в справочнике
    0 - Выход из программы
    """)
        choice = menu_input()
        if choice == 0:
            print("\nРабота программы завершена")
            sys.exit()
        elif choice == 1:
            read_data()
        elif choice == 2:
            add_data()
        elif choice == 3:
            edit_data()
        elif choice == 4:
            find_data()
        else:
            print('Выберите существующий пункт меню')
