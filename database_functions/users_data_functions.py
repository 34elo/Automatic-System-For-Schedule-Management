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


def get_employee_contact(emlpoyee_name, path_to_database) -> list:
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
