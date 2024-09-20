from aiogram import types, dispatcher
from create_bot import dp, bot
from aiogram import Router, F, filters
from aiogram.types import Message
from aiogram.filters import Command


router = Router()
@router.message(Command("problem"))
async def problem(message: types.Message):
    chat_id = message.chat.id
    message_id = message.message_id
    await bot.delete_message(chat_id, message_id=message_id)
    await bot.send_message(chat_id, 'Напишите администратору\n @Invincible_guys')




