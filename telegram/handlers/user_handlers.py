from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database_functions.constants import POINTS, DAYS_DICT
from database_functions.schedule_functions import get_schedule, get_my_schedule
from database_functions.users_data_functions import get_admin_names, get_admin_contact

# from db_work.admin.get_data_about_point import get_data_about_point
# from db_work.user.functions import get_all_points, get_free_shift, viev_schedule, get_name_from_username, \
#     set_work_points, get_all_admins, get_all_schedule, set_work_schedule
# from handlers.admin_handlers import get_points

router = Router()
path_users_data = '../../data/users_data.sqlite'
path_shedule = '../../data/schedule.sqlite'


# @router.message(F.text == "Посмотреть свободные смены на определенной точке")
# async def get_free_shift_message(message: Message):
#     """При сообщении выдает меню кнопочек выбора точки у которой надо посмотреть смены"""
#     builder = InlineKeyboardBuilder()
#     for i in POINTS:
#         builder.add(InlineKeyboardButton(
#             text=i,
#             callback_data=f"get_free_shift_{i}"
#         ))
#     builder.adjust(2)
#
#     await message.answer(
#         'Выберите точку, у которой хотите посмотреть свободные смены',
#         reply_markup=builder.as_markup()
#     )
#
#
# @router.callback_query(F.data[:15] == 'get_free_shift_')
# async def send_free_shift(callback: CallbackQuery):
#     """Получает сигнал(колбек) от нажатой кнопки.
#     Если это тот сигнал, который нужен, вызывается функция"""
#
#     point = callback.data[15:]
#     answer = get_free_shift(point)
#     await callback.message.answer(f'{answer}')


@router.message(F.text == "Посмотреть график в определенной точке")
async def get_schedule_in_point(message: Message):
    """При сообщении выдает меню кнопок выбора точки у которой надо посмотреть ВСЕ смены"""
    builder = InlineKeyboardBuilder()
    all_points = POINTS
    for i in all_points:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"get_schedule_{i}"
        ))

    # Располагаем все кнопки вертикально (по 2 в ряд)
    builder.adjust(2)

    await message.answer(
        'Выберите точку, у которой хотите посмотреть расписание',
        reply_markup=builder.as_markup()
    )



@router.callback_query(F.data[:13] == 'get_schedule_')
async def send_schedule(callback: CallbackQuery):
    point = callback.data[13:]
    table = f'Расписание {str(point)}\n\n'
    print(point)
    datas = get_schedule(str(point), path_shedule)
    for i in range(len(datas)):
        if datas[i]:
            table += DAYS_DICT[i] + ': ' + datas[i] + '\n'
        else:
            table += DAYS_DICT[i] + ': ' + 'Не занято' + '\n'
    await callback.message.answer(table)


@router.message(F.text == "Посмотреть все свои смены")
async def handle_worker(message: Message):
    name = message.from_user.username
    smens = get_my_schedule(name, path_users_data, path_shedule)
    if smens:
        text = 'Вот ваши смены на эту неделю:\n'
        for day in smens:
            point = smens[day]
            text += f'{day}: {point}\n'
    else:
        text = 'Видимо у вас нет смен на этой неделе. Хорошего отдыха)'

    await message.answer(f"{text}")


@router.message(F.text == "Связь с администратором")
async def handle_worker_buttons(message: Message):
    builder = InlineKeyboardBuilder()
    all_admins = get_admin_names(path_users_data)

    for i in all_admins:
        username = get_admin_contact(i, path_users_data)
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"ss_{username}"
        ))

    # Располагаем все кнопки вертикально (по одной в ряд)
    builder.adjust(1)

    await message.answer(
        'Выберите Админа с которым хотите связаться',
        reply_markup=builder.as_markup()
    )
@router.callback_query(F.data[:3] == 'ss_')
async def send_value(callback: CallbackQuery):
    await callback.message.answer(
        f'Вы можете связаться с этим админом по данному контакту:\n\n @{str(callback.data[3:])}')


# @router.message(F.text == "Установить желаемые точки работы")
# async def set_points(message: Message):
#     builder = InlineKeyboardBuilder()
#     all_points = get_all_points()
#
#     for i in all_points:
#         builder.add(InlineKeyboardButton(
#             text=i,
#             callback_data=f"set_points_{i}"
#         ))
#     builder.add(InlineKeyboardButton(
#         text='Закончить выбор точек',
#         callback_data=f"set_points_break"
#     ))
#     # Располагаем все кнопки вертикально (по 2 в ряд)
#     builder.adjust(2)
#
#     await message.answer(
#         'Выберите точки, у которых хотите посмотреть расписание',
#         reply_markup=builder.as_markup()
#     )
#
#
# @router.callback_query(F.data[:11] == 'set_points_')
# async def add_points(callback: CallbackQuery):
#     point = callback.data[11:]
#     username = callback.from_user.username
#     set_work_points(username, point)
#     await callback.message.answer(f'{str(point)} успешно добавлено в список ваших желаемых точек')
#
#
# @router.message(F.text == "Установить желаемые смены")
# async def go_set_work_schedule(message: Message):
#     builder = InlineKeyboardBuilder()
#     all_schedule = get_all_schedule()
#
#     for i in all_schedule:
#         builder.add(InlineKeyboardButton(
#             text=i,
#             callback_data=f"set_schedule_{i}"
#         ))
#     builder.add(InlineKeyboardButton(
#         text='Закончить выбор смен',
#         callback_data=f"set_schedule_break"
#     ))
#     # Располагаем все кнопки вертикально (по 2 в ряд)
#     builder.adjust(2)
#
#     await message.answer(
#         'Выберите точки, у которых хотите посмотреть расписание',
#         reply_markup=builder.as_markup()
#     )
#
#
# @router.callback_query(F.data[:13] == 'set_schedule_')
# async def add_schedule(callback: CallbackQuery):
#     point = callback.data[13:]
#     username = callback.from_user.username
#     set_work_schedule(username, point)
#     await callback.message.answer(f'{str(point)} успешно добавлено в список ваших желаемых смен')
#
#
# @router.message(lambda message: message.text in get_points())
# async def xyita(message: Message) -> None:
#     table = f'Расписание {message.text}\n\n'
#     datas = get_data_about_point(message.text)
#     for i in datas.keys():
#         if datas[i] != 'None':
#             table += str(i) + ': ' + datas[i] + '\n'
#         else:
#             table += str(i) + ': ' + 'Не занято' + '\n'
#     await message.answer(table)