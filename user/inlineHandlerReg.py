from aiogram import types, dispatcher
from aiogram.types import CallbackQuery
from create_bot import dp, bot
from keyboard import registration as registration_kb, Start, confirmationButtonReg, confirmationButtonDailyReg
from database import  getAllProjects, getUserRegistration, isProjectHasDaily, changeConfirmationState, createRegistrationTask, updateUserRegistration, getNameByCode, getProjectLink
from hooks import checkAllRegIsDone
import uuid
async def registration(callback_query: CallbackQuery):
    data = callback_query.data[4:]
    print(data)
    reg = checkAllRegIsDone(await getUserRegistration(callback_query.from_user.id), getAllProjects(only_titles=True))

    if(data[0:5] == 'back:'):
        data = data[5:]
        if data[0:4] == 'last':
            if reg['done']:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id,
                                            text=f'Вы уже прошли регистрацию, ждите заданий')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=registration_kb(items=[], doall=False))

            else:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id,
                                            text=f'Привет.\nДля начала пройди регистрацию во всех проектах')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=(registration_kb(reg['arr']) if len(
                                                        reg['arr']) > 1 else registration_kb(reg['arr'], doall=False)))

        else:

            await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id )



    elif data[0:6] == 'do_All':
        await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
        i = 0
        for el in reg['arr']:
            i += 1


            if i == len(reg['arr']):
                await bot.send_message(callback_query.from_user.id, el, reply_markup=Start(el, True))
            else:
                await bot.send_message(callback_query.from_user.id, el, reply_markup=Start(el, False))

        # await bot.send_message(callback_query.from_user.id, 'это были все задания, ждите заданий ')


    elif data[0:5] == 'oppr:':
        data = data[5:]
        if data[0:5] == 'last:':
            name = data[5:]


            if(isProjectHasDaily(data[5:])[0]):


                codes = [f'{uuid.uuid4()}'[0:20], f'{uuid.uuid4()}'[0:20]]
                createRegistrationTask(code=codes[0], name=data[5:], type='periodic',
                                       userId=callback_query.from_user.id)
                createRegistrationTask(code=codes[1], name=data[5:], type='daily', userId=callback_query.from_user.id)
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id, text=f'{data[5:]}\n{getProjectLink(name)}')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=confirmationButtonDailyReg(codes, True))
            else:
                code = f'{uuid.uuid4()}'
                createRegistrationTask(code=code, name=data[5:], type='periodic', userId=callback_query.from_user.id)
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id, text=f'{data[5:]}\n{getProjectLink(name)}')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=confirmationButtonReg(code, True))
        else:
            name = data
            if (isProjectHasDaily(data)[0]):

                codes = [f'{uuid.uuid4()}'[0:20], f'{uuid.uuid4()}'[0:20]]
                createRegistrationTask(code=codes[0], name=data, type='periodic',
                                       userId=callback_query.from_user.id)
                createRegistrationTask(code=codes[1], name=data, type='daily', userId=callback_query.from_user.id)
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id, text=f'{data}\n{getProjectLink(name)}')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=confirmationButtonDailyReg(codes, False))
            else:
                code = f'{uuid.uuid4()}'
                createRegistrationTask(code=code, name=data, type='periodic', userId=callback_query.from_user.id)
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id, text=f'{data}\n{getProjectLink(name)}')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=confirmationButtonReg(code, False))

    elif data[0:5] == 'done:':

        data = data[5:]
        if data[0:5] == 'last:':
            if(data[25] == ':'):

                tasks = [data[5:25], data[26:]]
                name =  getNameByCode(data[5:25])

                await updateUserRegistration(telegramId=callback_query.from_user.id, name=name)


                for i in tasks:
                    changeConfirmationState(state='done', uniqueCode=i)
            else:
                name =  getNameByCode(data[5:])
                await updateUserRegistration(telegramId=callback_query.from_user.id, name=name)
                changeConfirmationState(state='done', uniqueCode=data[5:])
            reg = checkAllRegIsDone(await getUserRegistration(callback_query.from_user.id),
                                    getAllProjects(only_titles=True))

            if reg['done']:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id, text=f'Вы уже прошли регистрацию, ждите заданий')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=registration_kb(items=[], doall=False))

            else:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id,
                                            text=f'Привет.\nДля начала пройди регистрацию во всех проектах')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=( registration_kb(reg['arr']) if len(reg['arr']) > 1 else  registration_kb(reg['arr'],doall=False) ))


        else:
            if (data[20] == ':'):
                name =  getNameByCode(data[0:20])
                await updateUserRegistration(telegramId=callback_query.from_user.id, name=name)
                tasks = [data[0:20], data[21:]]
                for i in tasks:
                    changeConfirmationState(state='done', uniqueCode=i)
            else:
                name =  getNameByCode(data[5:])
                await updateUserRegistration(telegramId=callback_query.from_user.id, name=name)
                changeConfirmationState(state='done', uniqueCode=data[5:])
            await bot.delete_message(message_id=callback_query.message.message_id, chat_id=callback_query.from_user.id)



    elif data[0:9] == 'not_done:':
        data = data[9:]
        if data[0:5] == 'last:':
            if (data[25] == ':'):

                tasks = [data[5:30], data[31:]]
                for i in tasks:
                    changeConfirmationState(state='failer', uniqueCode=i)
            else:
                changeConfirmationState(state='failer', uniqueCode=data[5:])
            reg = checkAllRegIsDone(await getUserRegistration(callback_query.from_user.id),
                                    getAllProjects(only_titles=True))
            if reg['done']:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id,
                                            text=f'Вы уже прошли регистрацию, ждите заданий')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=registration_kb(items=[], doall=False))

            else:
                await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                            message_id=callback_query.message.message_id,
                                            text=f'Привет.\nДля начала пройди регистрацию во всех проектах')
                await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                                    message_id=callback_query.message.message_id,
                                                    reply_markup=(registration_kb(reg['arr']) if len(
                                                        reg['arr']) > 1 else registration_kb(reg['arr'], doall=False)))

        else:

            if (data[20] == ':'):

                tasks = [data[0:20], data[21:]]
                for i in tasks:
                    changeConfirmationState(state='failer', uniqueCode=i)
            else:
                changeConfirmationState(state='failer', uniqueCode=data[5:])
            await bot.delete_message(message_id=callback_query.message.message_id, chat_id=callback_query.from_user.id)




def callbackQueryHandler(dp: dispatcher):
    dp.register_callback_query_handler(registration, lambda c: c.data[0:3] == 'reg')






