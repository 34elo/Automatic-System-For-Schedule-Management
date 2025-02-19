from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from telegram.keyboards import admin_keyboards

login_router = Router()


class AuthAdmin(StatesGroup):
    admin_code = State()


class AuthWorker(StatesGroup):
    worker_code = State()


@login_router.message(CommandStart())
async def start(message: Message):
    if already_auth(message.chat.id)[0]:
        if is_admin(message.chat.id)[1]:
            await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
        else:
            await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
    else:
        await message.answer(
            'Вам нужно авторизоваться, выберите вашу роль:',
            reply_markup=login_keyboard.main())


@login_router.message(F.text == 'Сотрудник')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите пароль сотрудника")
    await state.set_state(AuthWorker.worker_code)


@login_router.message(F.text == 'Администратор')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите пароль администратора")
    await state.set_state(AuthAdmin.admin_code)


@login_router.message(AuthWorker.worker_code)
async def message_with_text(message: Message, state: FSMContext):
    if check_worker_code(message.text):
        await state.clear()
        await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
        await put_data(message.from_user.id, 'Сотрудник')
    else:
        await message.answer('Данные неверны, Попробуйте снова')
        await state.set_state(AuthWorker.worker_code)


@login_router.message(AuthAdmin.admin_code)
async def message_with_text(message: Message, state: FSMContext):
    if check_admin_code(message.text):
        await state.clear()
        await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
        await put_data(message.from_user.id, 'Администратор')

    else:
        await message.answer('Данные неверны, Попробуйте снова')
        await state.set_state(AuthAdmin.admin_code)
