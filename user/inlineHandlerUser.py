from aiogram import types, dispatcher
from aiogram.types import CallbackQuery
from create_bot import dp, bot
from database import changeConfirmationState
from aiogram import Router, F, filters
from aiogram.filters import Command

router = Router()
@router.callback_query(F.data[0:4] == 'user')
async def userCallback(callback_query: CallbackQuery):
    data = callback_query.data[5:]
    print(data)
    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
    if data[0:5] == 'done:':
        changeConfirmationState(state='done', uniqueCode=data[5:])
    elif data[0:9] == 'not_done:':
        changeConfirmationState(state='failed', uniqueCode=data[9:])





