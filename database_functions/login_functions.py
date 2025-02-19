import sqlite3


def already_auth(name, path_to_database) -> bool:
    """Возвращает является ли пользователь зарегестрированым"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    return True


def is_admin(name, path_to_database) -> bool:
    """Возвращает является ли пользователь админом"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    return True


def check_worker_code(code, path_to_database) -> bool:
    """Возвращает является ли код верным"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    return True


def check_admin_code(code, path_to_database) -> bool:
    """Возвращает является ли код верным"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    return True


def put_data(name, path_to_database) -> None:
    """Запоминает пользователя в бд"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    pass
