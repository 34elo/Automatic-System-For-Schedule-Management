import sqlite3


def check_worker_code(password, path_to_database) -> bool:
    """Возвращает является ли код верным"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    passwords = data_cursor.execute('''SELECT password 
                                      FROM employees_passwords''').fetchall()
    passwords = [i[0] for i in passwords]
    return True if password in passwords else False


def check_admin_code(password, path_to_database) -> bool:
    """Возвращает является ли код верным"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    passwords = data_cursor.execute('''SELECT password 
                                  FROM admin_passwords''').fetchall()
    passwords = [i[0] for i in passwords]
    return True if password in passwords else False


def put_data(chat_id, password, role, path_to_database) -> None:
    """Запоминает чат с пользователем в бд
    role - 'Администратор' / 'Сотрудник'
    """
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    if role == 'Администратор':
        data_cursor.execute(f'''UPDATE admin_passwords SET chat_id = {chat_id} WHERE password = "{password}"''')
    else:
        data_cursor.execute(f'''UPDATE employees_passwords SET chat_id = {chat_id} WHERE password = "{password}"''')
    data.commit()
    data.close()
