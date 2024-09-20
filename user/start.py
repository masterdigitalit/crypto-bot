from aiogram import types, dispatcher
from create_bot import dp, bot
from keyboard.InlineKeyboard import registration, AdminKb
from database import createUser, getAllProjects,  isUserRegistered, getUserRegistration, getUserStatus
from hooks import checkAllRegIsDone
from aiogram import Router, F, filters
from aiogram.filters import Command

router = Router()
@router.message(Command("start"))
async def startMessage(message: types.Message):
    chat_id = message.chat.id
    message_id = message.message_id
    user_id = message.from_user.id
    if not isUserRegistered(user_id):
        createUser(id=user_id, name=message.from_user.username,projects=[])
    if     getUserStatus(chat_id) == 'user':


        await bot.delete_message(chat_id, message_id=message.message_id)


        reg = checkAllRegIsDone(await getUserRegistration(user_id),getAllProjects(only_titles=True) )
        if reg['done']:
            await bot.send_message(chat_id, 'Вы уже прошли регистрацию, ждите заданий', reply_markup=types.ReplyKeyboardRemove())

        else:
            await bot.send_message(chat_id, 'Привет.\nДля начала пройди регистрацию во всех проектах', reply_markup=( registration(reg['arr']) if len(reg['arr']) > 1 else  registration(reg['arr'],doall=False) ))
    elif     getUserStatus(chat_id) == 'admin':
        await bot.delete_message(chat_id=chat_id, message_id=message.message_id)
        await bot.send_message(chat_id, 'Привет админ, что надо сделать ?',
                              reply_markup=AdminKb())


