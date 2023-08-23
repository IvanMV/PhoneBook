**ОПИСАНИЕ ПРОГРАММЫ**

Данная программа является телефонным справочником, позволяющим хранить следующие данные:
- Фамилия
- Имя
- Отчество
- Компания
- Рабочий телефон
- Личный телефон

**ЗАПУСК ПРОГРАММЫ**

Запуск программы осуществляется файлом "main.py"

**ХРАНЕНИЕ ДАННЫХ**

Данные хранятся в json формате в файле "phonebook.json" в папке "database"

**РАБОТА С ПРОГРАММОЙ**

Работа с программой осуществляется из командной строки путем ввода данных с клавиатуры.

**ОПИСАНИЕ ПУНКТОВ МЕНЮ**

1. **Вывести постранично данные из справочника**
   
   Выводит все данные из справочника на экран постранично (10 записей на страницу)
   
   
   Выводит номер текущей страницы и общее число страниц
   
   
   Позволяет прервать просмотр и выйти в главное меню программы
   
2. **Добавление новой записи в справочник**
   
   Позволяет построчно ввести новую запись
   
   
   Если запись уже существует, она не будет добавлена повторно
   
   
   Если не введена фамилия, и не введено имя - запись не будет добавлена
   
   
   Если не введен хотя бы один телефон (рабочий или личный) - запись не будет добавлена
   
   
   ФИО преобразуются при вводе к заглавному первому символу
   
   
   На ввод номеров телефонов ограничений нет, чтобы позволить пользователям сохранять данные в удобном им виде (например указать добавочный номер сотрудника)

3. **Редактирование записей в справочнике**
   
   Для изменения существующей записи, необходимо ее найти путем ввода соответствующей информации
   
   
   Более подробно о режиме поиска в п.4
   
   
   Если запись не найдена, выдается сообщение
   
   
   Если найдено несколько записей, соответствующих введенным параметрам - выводятся все  найденные записи для ознакомления и требование о проведении нового поиска с уточненными параметрами

   
   Если найдена одна запись, она выводится на экран и далее пользователь должен заново ввести все данные для записи (включая те, которые не требовали изменений). Старые данные записи выводятся рядом с названием полей для заполнения, что облегчит ввод информации.

4. **Поиск записей в справочнике**
   
   Поиск данных возможен как по любому одному полю, так и по любой комбинации полей.

   
   Для поиска необходимо ввести данные в предлагаемые поля.

   
   Если по текущему полю поиск не требуется, следует нажать "ENTER" для его игнорирования и переходу к заполнению следующего поля.

   
   Если дальнейший ввод данных не требуется (например поиск будет вестить только по "Фамилии", то ввод "0" с клавиатуры и нажатия "ENTER" прервет последующий ввод данных для поиска.

   
   Например: в поле "Фамилия" ввести "Иванов", нажать "ENTER", ввести "0" и нажать "ENTER" - в таком случае поиск будет вестись только по фамилии "Иванов".

   
   При поиске ФИО и названия компании - все данные (как из базы, так и введенные для поиска) приводятся к нижнему регистру, что делает поиск регистронезависимым.

   
   При поиске телефона (и рабочего, и личного) поиск ведется только по цифрам, т.е. все символы, не являющиеся цифрами, будут проигнорированы.

   
   Например: в базе сохранен телефон в таком виде: "(343) 147 - 17 - 15". Поиск будет успешен, если пользователь введет в соответствующем поле например "343 147-17-15", или же "(343)1471715" и т.п., т.е. все данные варианты поиска позволят найти запись с данным телефоном.
   
5. **Для выхода из программы необходимо в основном меню ввести "0" и нажать "ENTER"**. 
