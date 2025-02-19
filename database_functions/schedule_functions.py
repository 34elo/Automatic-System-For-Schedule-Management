import sqlite3


def get_schedule(point, path_to_database) -> tuple:
    """Возвращает расписание на определённой точке"""

    data = sqlite3.connect(path_to_database)
    data_cursor = data.cursor()
    schedule = data_cursor.execute(f'''SELECT Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
                                      FROM "{point}"''').fetchone()
    return schedule


def get_my_schedule(username, path_to_database_users_data, path_to_database_schedule) -> dict:
    """Возвращает свой график работы для сотрудника.
       out = {Понедельник: Рыленкова},
    """
    from database_functions.constants import POINTS, DAYS_DICT
    from database_functions.users_data_functions import get_full_name_by_username

    out = {}
    full_name = get_full_name_by_username(username, path_to_database_users_data)
    data_cursor = sqlite3.connect(path_to_database_schedule).cursor()

    for point in POINTS:
        schedule = data_cursor.execute(
            f'SELECT Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday FROM "{point}"').fetchone()

        if schedule:
            days = [DAYS_DICT[ind] for ind, name in enumerate(schedule) if name == full_name]
            for i in days:
                out[i] = point

    return out

def fix_edit_schedule(full_name, point, day, path_to_database_schedule) -> None:
    """
    Изменяет график
    """
    pass