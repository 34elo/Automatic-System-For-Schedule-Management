import math

from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать частичный график")
    kb.button(text="Отправить уведомление сотрудникам")
    kb.button(text="Расписание на точках")
    kb.button(text="Связаться с сотрудником")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def points_list(all_points: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for i in all_points:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"get_schedule_{i}"
        ))

    # Располагаем все кнопки вертикально (по 2 в ряд)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


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
