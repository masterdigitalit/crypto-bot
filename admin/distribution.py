from database import getAllUsers
from aiogram import Bot
from aiogram import Bot

from database import getAllUsers


async def distributionFunc(bot:Bot, name):
    users = getAllUsers()
    print(users)
    for i in users:
        await bot.send_message(i[1], name)

