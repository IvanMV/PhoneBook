import json
import sys
from typing import List, Dict
from module.functions import make_title, view_record, find_title, edit_title
from module.functions import suc_edit_title, err_edit_title, suc_add_title
from module.config import path


# Добавление новой записи в справочник
def add_data() -> None:
    print('\nДобавление новой записи в справочник\n')
    data_to_add: Dict[str, str] = get_data_from_user() # Ввод данных пользователем
    if data_to_add:
        is_added: bool = False # Флаг индикации необходимости сохранения бд
        data_to_modify: List[Dict[str, str]] = read_file() # Чтение существующих данных из базы
        
        # Проверка наличия записи в базе и добавление в случае отсутсвия
        if data_to_add not in data_to_modify:
            data_to_modify.append(data_to_add)
            is_added = True
        
        # Запись данных в файл
        if is_added:
            result: bool = write_file(data_to_modify)
            if result:
                print(suc_add_title())


# Обновление записи в справочнике
def edit_db(user_old: Dict[str, str], new_data: Dict[str, str]) -> bool:
    data: List[Dict[str, str]] = read_file() # Чтение существующих данных из базы
    try:
        ind = data.index(user_old) # Поиск номера записи для изменения в БД
        data[ind] = new_data # Запись новых данных взамен существующих
        write_file(data) # Запись в файл
    except:
        print('Запись не найдена в базе данных!')
        return False
    else:
        return True


# Чтение файла базы данных
def read_file() -> List[Dict[str, str]]:
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except:
        print('Ошибка чтения файла базы данных справочника!')
        print('Работа программы будет завершена')
        sys.exit()
    else:
        return data


# Запись файла базы данных
def write_file(data: List[Dict[str, str]]) -> bool:
    try:
        with open(path, 'w') as f:
            json.dump(data, f)
    except:
        return False
    else:
        return True


# Вывод записей на экран
def view_data(data: List[Dict[str, str]]) -> None:
    print(make_title())
    
    x: int = 10 # Число записей на одной странице
    # Переменные для вычисления числа страниц
    m: int = len(data) //x
    n: int = len(data) % x 
    
    # Определение общего числа страниц с записями для вывода (total)
    if n == 0:
        total: int = m
    else:
        total = m + 1
    
    #Постраничный вывод записей на экран
    for i in range(len(data)):
        print(view_record(data[i]))
        # Вывод номера текущей страницы, общего числа страниц и меню навигации
        if (i+1) % x == 0:
            print(f'Стр. {(i+1) // x} из {total}')
            text: str = 'Нажмите любую клавишу для продолжения просмотра или "0" для выхода:\n'
            choice: str = input(text)
            if choice == '0':
                break
        # Вывод номера последней (неполной) страницы
        elif (i+1) == len(data) and not (i+1) % x == 0:
            print(f'Стр. {((i+1) // x) + 1} из {total}')


# Вывод постранично всех данных из справочника
def read_data() -> None:
    old_data: List[Dict[str, str]] = read_file() # Чтение данных из файла
    view_data(old_data) # Постраничный вывод всех записей на экран


# Ввод пользователем данных для поиска
def find_input() -> Dict[str, str]:
    data_to_find: Dict[str, str] = {}
    temp_to_find: Dict[str, str] = {
                    'last_name': 'Фамилия: ',
                    'first_name': 'Имя: ',
                    'middle_name': 'Отчество: ',
                    'company': 'Компания: ',
                    'wp_index': 'Рабочий телефон: ',
                    'pp_index': 'Личный телефон: '
                    }
    print('\nВведите данные для поиска. "0" - остановить ввод новых данных.')
    for key, value in temp_to_find.items():
        input_data: str = input(value).strip().lower()
        if input_data and input_data != '0':
            # Индексация телефонов для поиска
            if key == 'wp_index' or key == 'pp_index':
                input_data = ''.join(x if x.isdigit() else '' for x in input_data)
            data_to_find[key] = input_data
        elif input_data == '0':
            break
    return data_to_find


# Поиск записей в БД по введенным пользователем данным
def find_in_db(users: Dict[str, str]) -> List[Dict[str, str]]:
    data: List[Dict[str, str]] = read_file() # Чтение данных из файла
    temp: List[Dict[str, str]] = [] # Список найденных записей
    for record in data:
        # Преобразуем данные из базы к нижнему регистру для регистронезависимого поиска
        record_lower = dict([k.lower(), v.lower()] for k, v in record.items())
        if users.items() <= record_lower.items():
            temp.append(record)
    return temp


# Поиск записей в справочнике по введенным параметрам
def find_data() -> None:
    data_to_find: Dict[str, str] = find_input() # Ввод пользователем данных для поиска
    temp: List[Dict[str, str]] = find_in_db(data_to_find) # Поиск записей в БД по введенным данным
    
    # Вывод результатов
    print(find_title(len(temp)))
    if temp:
        view_data(temp)
    else:
        print('Поиск не дал результатов.')


# Редактирование данных
def edit_data() -> None:
    data_to_find: Dict[str, str] = find_input() # Ввод пользователем данных для поиска
    temp: List[Dict[str, str]] = find_in_db(data_to_find) # Поиск записей в БД по введенным данным
    if not temp:
        print('Поиск не дал результатов.')
    elif len(temp) >1:
        print(find_title(len(temp)))
        view_data(temp)
        print('Найдено слишком много совпадений, попробуйте уточнить параметры поиска')
    else:
        user: List[str] = list(temp[0].values()) # Список значений записи для редактирования
        print(edit_title())
        view_data(temp)
        print('Введите новые данные')
        # Ввод пользователем данных для редактирования существующей записи
        new_data: Dict[str, str] = get_new_data(user)
        if new_data:
            result: bool = edit_db(temp[0], new_data)
            if result:
                print(suc_edit_title())
            else:
                print(err_edit_title())


# Ввод пользователем данных для добавления новой записи
def get_data_from_user() -> Dict[str, str]:
    last_name: str = input("Фамилия: ").strip().capitalize()
    first_name: str = input("Имя: ").strip().capitalize()
    middle_name: str = input("Отчество: ").strip().capitalize()
    company: str = input("Компания: ").strip()
    work_phone: str = input("Рабочий телефон: ").strip()
    wp_index: str = ''.join(x if x.isdigit() else '' for x in work_phone) # индексация поля
    personal_phone: str = input("Личный телефон: ").strip()
    pp_index: str = ''.join(x if x.isdigit() else '' for x in personal_phone) # индексация поля
    if not last_name and not first_name:
        print('\nНеобходимо указать фамилию или имя.\nДанные не сохранены!')
        return {}
    if not work_phone and not personal_phone:
        print('\Нужно указать хотя бы один телефон.\nДанные не сохранены!')
        return {}
    data: Dict[str, str] = {
            'last_name': last_name, 
            'first_name': first_name,
            'middle_name': middle_name,
            'company': company,
            'work_phone': work_phone,
            'wp_index': wp_index,
            'personal_phone': personal_phone,
            'pp_index': pp_index
            }
    return data


# Ввод пользователем данных для редактирования существующей записи
def get_new_data(user: List[str]) -> Dict[str, str]:
    last_name: str = input(f"Фамилия ({user[0]}): ").strip().capitalize()
    first_name: str = input(f"Имя ({user[1]}): ").strip().capitalize()
    middle_name: str = input(f"Отчество ({user[2]}): ").strip().capitalize()
    company: str = input(f"Компания ({user[3]}): ").strip()
    work_phone: str = input(f"Рабочий телефон ({user[4]}): ").strip()
    wp_index: str = ''.join(x if x.isdigit() else '' for x in work_phone) # индексация поля
    personal_phone: str = input(f"Личный телефон ({user[6]}): ").strip()
    pp_index: str = ''.join(x if x.isdigit() else '' for x in personal_phone) # индексация поля
    if not last_name and not first_name:
        print('\nНеобходимо указать фамилию или имя.\nДанные не сохранены!')
        return {}
    if not work_phone and not personal_phone:
        print('\Нужно указать хотя бы один телефон.\nДанные не сохранены!')
        return {}
    data: Dict[str, str] = {
            'last_name': last_name, 
            'first_name': first_name, 
            'middle_name': middle_name,
            'company': company, 
            'work_phone': work_phone,
            'wp_index': wp_index,
            'personal_phone': personal_phone,
            'pp_index': pp_index
            }
    return data