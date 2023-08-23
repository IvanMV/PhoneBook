from module.functions import welcome, check_db
from module.menu import menu_main
from module.config import path


# Функция запуска программы
def main() -> None:
    welcome()
    check_db(path)
    menu_main()


# Запуск программы
main()
