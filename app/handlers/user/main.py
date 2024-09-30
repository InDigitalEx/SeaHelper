from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils import time_until_summer

user_router = Router()


@user_router.message(Command('until'))
async def __until_command(message: Message) -> None:
    await message.answer(time_until_summer('Asia/Dubai'))

