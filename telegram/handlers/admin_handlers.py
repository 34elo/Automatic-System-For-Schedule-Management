from aiogram import Router, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackQueryFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.utils.text_decorations import MarkdownDecoration

from database_functions.constants import POINTS, DAYS
from database_functions.schedule_functions import get_schedule
from database_functions.users_data_functions import get_all_chat_ids, get_employee_contact
from telegram.config import config
from telegram.keyboards import admin_keyboards
from telegram.keyboards.admin_keyboards import points_list

admin_router = Router()
path_to_database_users = '../data/users_data.sqlite'
path_to_database_schedule = '../data/schedule.sqlite'


def auto_schedule_create():
    pass


class NotificationText(StatesGroup):
    text = State()


class ScheduleText(StatesGroup):
    worker = State()
    smena = State()
    points = State()


class Contact(StatesGroup):
    contact = State()


def send_notifications(message) -> None:
    chats = get_all_chat_ids(path_to_database_users)

    for chat in chats:
        Bot(token=config.bot_token.get_secret_value()).send_message(chat, message.text)


def get_points() -> list[str]:  # список таблиц с точками
    return POINTS


@admin_router.message(F.text == "Сформировать частичный график")
async def create_schedule(message: Message) -> None:
    auto_schedule_create()
    await message.answer('График сформирован. Вы сможете ознакомиться с ним в меню "Расписание на точках"')


@admin_router.message(F.text == "Отправить уведомление сотрудникам")
async def send_notification_tg(message: Message, state: FSMContext) -> None:
    await message.answer('Напишите ваше уведомление:')
    await state.set_state(NotificationText.text)


@admin_router.message(NotificationText.text)
async def message_with_text(message: Message, state: FSMContext) -> None:
    send_notifications(message)
    await message.answer('Ваше уведомление сотрудникам отправлено')
    await state.clear()


@admin_router.message(F.text == "Расписание на точках")
async def check_points(message: Message) -> None:
    text = 'Выберите точку из приведенных ниже:\n\n'
    await message.answer(text, reply_markup=points_list(get_points()))


@admin_router.callback_query(F.data[:13] == 'get_schedule_')
async def get_schedule_point(callback: CallbackQuery) -> None:
    point = callback.data[13:]
    table = f'Расписание {str(point)}\n\n'
    datas = get_schedule(str(point), path_to_database_schedule)
    if datas is None:
        table += f"Расписание отсутствует"
    else:
        for i in range(len(DAYS)):
            if datas[i] is None:
                data = "Отсутствует"
            else:
                data = datas[i]
            table += DAYS[i].capitalize() + ' - ' + data + '\n'
    await callback.message.answer(table)


@admin_router.message(F.text == "Связаться с сотрудником")
async def contact(message: Message, state: FSMContext) -> None:
    await message.answer('Введите ФИО сотрудника, с которым хотите связаться')
    await state.set_state(Contact.contact)


@admin_router.message(Contact.contact)
async def state_contact(message: Message, state: FSMContext) -> None:
    data = get_employee_contact(message.text, path_to_database_users)
    text = f'Информация о "{message.text}"\n\n'
    text += f'Teлефон: {data[0]}\n'
    text += f'Username: @{data[1]}'
    await message.answer(text)
    await state.clear()
