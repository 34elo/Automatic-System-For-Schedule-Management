import sqlite3


def already_auth(name, path_to_database) -> bool:
    """Возвращает является ли пользователь зарегестрированым"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    pass

def is_admin(name, path_to_database) -> bool:
    """Возвращает является ли пользователь админом"""
    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''''').fetchone()
    pass