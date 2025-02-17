from aiogram import Router
from aiogram.types import Message

user_router = Router()


@user_router.message()
def template(message: Message):
    pass
