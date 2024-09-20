from aiogram import types, dispatcher
from aiogram.types import CallbackQuery
from create_bot import dp, bot
from database import getUserStatus,addNewProject
from database import changeConfirmationState
from aiogram import Router, F, filters
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboard import markup5
from aiogram.types import ReplyKeyboardRemove
from admin.distribution import distributionFunc
router = Router()

class addNewProjectClass(StatesGroup):
    name = State()
    pereodic = State()
    pereodicTime = State()
    daily = State()
    link = State()
@router.callback_query(F.data[0:17] == 'admin:add_project')
async def adminControls(callback_query: CallbackQuery, state:FSMContext):
    message_id = callback_query.message.message_id

    await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
    user_id = callback_query.from_user.id
    if getUserStatus(user_id) == 'admin':


        data = callback_query.data[6:]
        print(data)
        await state.set_state(addNewProjectClass.name)
        await bot.send_message(callback_query.from_user.id, 'введите название (на английском )', reply_markup=ReplyKeyboardRemove())
@router.message(addNewProjectClass.name)
async def adminAddProjectName(message:Message,  state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(addNewProjectClass.pereodic)


    await bot.send_message(message.from_user.id, 'есть почасовая награда?', reply_markup=markup5)


@router.message(addNewProjectClass.pereodic)
async def adminAddProjectPereodic(message:Message,  state:FSMContext):
    if message.text == 'да':
        await state.update_data(pereodic=1)
    elif message.text == 'нет':
        await state.update_data(pereodic=0)
    await state.set_state(addNewProjectClass.pereodicTime)


    await bot.send_message(message.from_user.id, 'введите промежуток в минутах', reply_markup=ReplyKeyboardRemove())
@router.message(addNewProjectClass.pereodicTime)
async def adminAddProjectPereodicTime(message:Message,  state:FSMContext):
    if message.text.isdigit():

        await state.update_data(pereodicTime=message.text)
        await state.set_state(addNewProjectClass.daily)
        await bot.send_message(message.from_user.id, 'есть ежедневка?', reply_markup=markup5)
    else:
        await bot.send_message(message.from_user.id, 'попробуйте еще раз, введенное число не подходит', reply_markup=ReplyKeyboardRemove())
        await state.set_state(addNewProjectClass.pereodicTime)

@router.message(addNewProjectClass.daily)
async def adminAddProjectDaily(message:Message,  state:FSMContext):
    if message.text == 'да':
        await state.update_data(daily=1)
    elif message.text == 'нет':
        await state.update_data(daily=0)
    await state.set_state(addNewProjectClass.link)
    await bot.send_message(message.from_user.id, 'отправте ссылку', reply_markup=ReplyKeyboardRemove())

@router.message(addNewProjectClass.link)
async def adminAddProjectLink(message:Message,  state:FSMContext):
    await state.update_data(link=message.text)
    data = await state.get_data()
    addNewProject(name=data['name'], periodic=data['pereodic'], pereodic_time=data['pereodicTime'], daily=data['daily'], link=data['link'])
    print(data)

    await bot.send_message(message.from_user.id, 'успешно добавлено', reply_markup=ReplyKeyboardRemove())
    await distributionFunc(bot, name=data['name'])









