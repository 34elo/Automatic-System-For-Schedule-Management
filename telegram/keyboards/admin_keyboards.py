import math

from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать частичный график")
    kb.button(text="Отправить уведомление сотрудникам")
    kb.button(text="Расписание на точках")
    kb.button(text="Связаться с сотрудником")
    kb.button(text="Количество смен у сотрудников")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)



def points_list(arg: list[str]) -> ReplyKeyboardMarkup:
    arg.append('Меню')
    num_elements = len(arg)
    if num_elements == 0:
        return ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)

    # Находим ближайшее целое число к квадратному корню, чтобы сделать клавиатуру более "квадратной"
    row_size = int(round(math.sqrt(num_elements)))

    # Уточняем row_size: если row_size*row_size не хватает, добавляем +1 для row_size
    if row_size * row_size < num_elements:
        row_size += 1

    keyboard_buttons = []
    for i in range(0, num_elements, row_size):
        row = [KeyboardButton(text=item) for item in arg[i:i + row_size]]
        keyboard_buttons.append(row)

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)
    return keyboard


def edit_schedule() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Редактировать",
        callback_data="Редактировать")
    )
    return builder


def day_week() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Понедельник")
    kb.button(text="Вторник")
    kb.button(text="Среда")
    kb.button(text="Четверг")
    kb.button(text='Пятница')
    kb.button(text='Суббота')
    kb.button(text="Воскресенье")
    return kb.as_markup(resize_keyboard=True)
