from database.tasksActions import selectByExecutionTime
from database.projectsActions import getProjectLink
from database import getProjectPeriodicTime
from database import createTask
from aiogram import Bot
from keyboard.InlineKeyboard import confirmationButton, confirmationButtonDaily
import uuid


async def timeCheckUp(bot:Bot):
    tasks = selectByExecutionTime()
    if tasks:
        for i in tasks:
            name,  type, userId, state = i[1], i[6], i[8], i[5]
            if state == 'done':
                if type == 'periodic':
                    code = uuid.uuid4()
                    createTask(userId=userId, name=name, type='periodic',code=f'{code}', time=getProjectPeriodicTime(name))
                    await bot.send_message(userId, f'Привет, забери часовую награду в {name}\n{getProjectLink(name)}', reply_markup=confirmationButton(f'{code}'))
                elif type == 'daily':
                    code = uuid.uuid4()
                    createTask(userId=userId, name=name, type='daily', code=f'{code}')
                    await bot.send_message(userId, f'Привет, забери ежедневную награду в {name}\n{getProjectLink(name)}', reply_markup=confirmationButton(f'{code}'))
