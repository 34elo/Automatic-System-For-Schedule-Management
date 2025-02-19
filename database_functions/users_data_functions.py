import sqlite3


def get_admin_names(path_to_database) -> list:
    """Возвращает список имён всех администраторов"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    admin_names = data_cursor.execute('''SELECT full_name
                                         FROM admin_passwords''').fetchall()
    admin_names = [name[0] for name in admin_names]
    return admin_names


def get_admin_contact(admin_name, path_to_database) -> str:
    """Возвращает username администратора по его фио"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    admin_contact = data_cursor.execute(f'''SELECT username
                                        FROM admin_passwords
                                        WHERE full_name = "{admin_name}"''').fetchone()
    return admin_contact[0]


def get_employee_contact(emlpoyee_name, path_to_database) -> tuple:
    """Возвращает телефон и username сотрудника по его фио"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    employee_contact = data_cursor.execute(f'''SELECT phone_number, username
                                        FROM employees_passwords
                                        WHERE full_name = "{emlpoyee_name}"''').fetchone()
    return employee_contact


def get_full_name_by_username(username, path_to_database) -> str:
    """Возвращает ФИО сотрудника по его username"""

    data_cursor = sqlite3.connect(path_to_database).cursor()
    full_name = data_cursor.execute(f'''SELECT full_name
                                        FROM employees_passwords
                                        WHERE username = "{username}"''').fetchone()[0]
    return full_name


def get_all_chat_ids(path_to_database) -> list:
    """Возвращает все айди чатов с сотрудниками"""

    data_cursor = sqlite3.connect(path_to_database).cursor()
    chat_ids = data_cursor.execute(f'''SELECT "chat_id"
                                        FROM "employees_passwords"''').fetchall()
    chat_ids = [int(id_[0]) for id_ in chat_ids]
    return chat_ids


def change_point_wishes(employee, point, mode, path_to_database) -> None:
    """Устанавливает или удаляет желаемую точку для сотрудника
       В зависимости от mode
       mode='set' или mode='remove'"""
    from database_functions.constants import POINTS

    if point in POINTS:

        data = sqlite3.connect(path_to_database)
        data_cursor = data.cursor()
        current_point_wishes = data_cursor.execute(f'''SELECT point_wishes
                                                       FROM "employees_wishes"
                                                       WHERE full_name = "{employee}"''').fetchone()[0].split(';')
        if '' in current_point_wishes:
            current_point_wishes.remove('')
        if mode == 'set' and point not in current_point_wishes:
            current_point_wishes.append(point)
        elif mode == 'remove' and point in current_point_wishes:
            current_point_wishes.remove(point)
        elif mode != 'set' and mode != 'remove':
            print('Wrong mode in change_point_wishes')
            raise TypeError
        point_wishes = ';'.join(current_point_wishes)
        data_cursor.execute(f'''UPDATE employees_wishes
                                SET "point_wishes" = "{point_wishes}"
                                WHERE full_name = "{employee}"''')
        data.commit()
        data.close()
    else:
        print('Wrong point')
        raise ValueError


def change_day_wishes(employee, day, mode, path_to_database) -> None:
    """Устанавливает или удаляет желаемую смену для сотрудника
       В зависимости от mode
       mode='set' или mode='remove'"""
    from database_functions.constants import DAYS

    if day in DAYS:

        data = sqlite3.connect(path_to_database)
        data_cursor = data.cursor()
        current_day_wishes = data_cursor.execute(f'''SELECT day_wishes
                                                       FROM "employees_wishes"
                                                       WHERE full_name = "{employee}"''').fetchone()[0].split(';')
        if '' in current_day_wishes:
            current_day_wishes.remove('')
        if mode == 'set' and day not in current_day_wishes:
            current_day_wishes.append(day)
        elif mode == 'remove' and day in current_day_wishes:
            current_day_wishes.remove(day)
        elif mode != 'set' and mode != 'remove':
            print('Wrong mode in change_point_wishes')
            raise TypeError
        day_wishes = ';'.join(current_day_wishes)
        data_cursor.execute(f'''UPDATE employees_wishes
                                SET "day_wishes" = "{day_wishes}"
                                WHERE full_name = "{employee}"''')
        data.commit()
        data.close()
    else:
        print('Wrong day')
        raise ValueError
