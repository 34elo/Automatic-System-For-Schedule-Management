from aiogram import Router
from aiogram.types import Message

login_router = Router()


@login_router.message()
def template(message: Message):
    pass
