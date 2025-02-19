from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Посмотреть свободные смены на определенной точке")
    kb.button(text="Посмотреть график в определенной точке")
    kb.button(text="Посмотреть все свои смены")
    kb.button(text="Связь с администратором")
    kb.button(text='Установить желаемые точки работы')
    kb.button(text='Установить желаемые смены')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
