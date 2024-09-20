from database.tasksActions import selectByWarningTime
from database.projectsActions import getProjectLink
from database import getProjectPeriodicTime
from database import createTask
from aiogram import Bot
from keyboard.InlineKeyboard import confirmationButton, confirmationButtonDaily
import uuid


async def warningCheckUp(bot:Bot):
    tasks = selectByWarningTime()
    print(tasks)
    if tasks:
        for i in tasks:
            name, type, userId, state = i[1], i[6], i[8], i[5]

            if type == 'periodic':
                code = uuid.uuid4()

                await bot.send_message(userId, f'Привет, срочно забери часовую награду в {name}\n{getProjectLink(name)}',
                                       reply_markup=confirmationButton(f'{code}'))
            elif type == 'daily':
                code = uuid.uuid4()

                await bot.send_message(userId,
                                       f'Привет, срочно забери ежедневную награду в {name}\n{getProjectLink(name)}',
                                       reply_markup=confirmationButton(f'{code}'))
