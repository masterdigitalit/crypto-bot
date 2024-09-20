from aiogram import types, dispatcher
from create_bot import dp, bot


async def menuMessage(message: types.Message):


    chat_id = message.chat.id
    await bot.send_message(chat_id, 'меню')




def registerClientHandler(dp: dispatcher):
    dp.register_message_handler(menuMessage, commands=['menu'])
