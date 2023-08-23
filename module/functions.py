import os.path
import json
from typing import Dict, List


# Вывод названия программы
def welcome() -> None:
    print('\nТЕЛЕФОННЫЙ СПРАВОЧНИК')


# Проверка наличия файла базы данных
def check_db(path: str) -> None:
    if not os.path.isfile(path): # Создание пустого файла при его отсутствии
        with open(path, 'w') as f:
            data: List[Dict[str, str]] = []
            json.dump(data, f)


# Заголовок вывода записей из справочника
def make_title() -> str:
    title: str = '-' * 120 + '\n' + \
            'Фамилия'.ljust(15) + '|' + \
            'Имя'.ljust(15) + '|' + \
            'Отчество'.ljust(15) + '|' + \
            'Компания'.ljust(25) + '|' + \
            'Раб. тел'.ljust(20) + '|' + \
            'Личный тел'.ljust(25) + \
            '\n' + '-' * 120 
    return title


# Заголовок результатов поиска
def find_title(num: int) -> str:
    number: str = str(num) # Число найденных записей
    title: str = '-' * 120 + '\n' + 'РЕЗУЛЬТАТЫ ПОИСКА:' + '(' + number + ')' + \
            '\n' + '-' * 120 
    return title


# Заголовок редактирования данных
def edit_title() -> str:
    title: str = '-' * 120 + '\n' + 'РЕДАКТИРОВАНИЕ ДАННЫХ' + '\n' + '-' * 120
    return title


# Заголовок успешного редактирования данных
def suc_edit_title() -> str:
    title: str = '-' * 120 + '\n' + 'ЗАПИСЬ ОБНОВЛЕНА УСПЕШНО!' + '\n' + '-' * 120
    return title


# Заголовок успешного добавления новой записи
def suc_add_title() -> str:
    title: str = '-' * 120 + '\n' + 'ЗАПИСЬ ДОБАВЛЕНА УСПЕШНО!' + '\n' + '-' * 120
    return title


# Заголовок ошибки редактирования записи
def err_edit_title() -> str:
    title: str = '-' * 120 + '\n' + 'ОШИБКА ИЗМЕНЕНИЯ ЗАПИСИ' + '\n' + '-' * 120
    return title


# Создание экранного представления отдельной записи
def view_record(user: Dict[str, str]) -> str:
    string: str = user['last_name'].ljust(15) + '|' + \
             user['first_name'].ljust(15) + '|' + \
             user['middle_name'].ljust(15) + '|' + \
             user['company'].ljust(25) + '|' + \
             user['work_phone'].ljust(20) + '|' + \
             user['personal_phone'].ljust(25) + \
            '\n' + '-' * 120
    return string
