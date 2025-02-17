from aiogram import Router
from aiogram.types import Message

admin_router = Router()


@admin_router.message()
def template(message: Message):
    pass
