from aiogram import dispatcher
from create_bot import dp, bot
from user import start, menu, inlineHandlerReg, problem, inlineHandlerUser
import logging
from admin import adminKeyboard
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from cron.distributor import  distributor
import asyncio

from datetime import datetime
import time

# adminKeyboard.setup(dp)
# inlineHandlerUser.setup(dp)
# problem.setup(dp)
# menu.setup(dp)
# inlineHandlerReg.setup(dp)
# start.setup(dp)
logging.basicConfig(
     format="{asctime} - {levelname} - {message}",
     style="{",
     datefmt="%H:%M",
     level=logging.INFO
)
async def telegram():
    # def tack(job):
    #     print('Tack! The time is: ',job.next_run_time, job.trigger)
    #
    # def listener(event):
    #     if not event.exception:
    #         job = scheduler.get_job(event.job_id)
    #         if job.name == 'timeCheckUp':
    #             print( )
    #             tack(job)
    logging.info('bot started')
    logging.getLogger('apscheduler.executors.default').setLevel(logging.INFO)
    scheduler = AsyncIOScheduler(timizone='Europe/Moscow')
    distributor(scheduler, bot)
    # scheduler.add_listener(listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


    try:
        scheduler.start()

        dp.include_routers(start.router, problem.router, inlineHandlerUser.router, inlineHandlerReg.router, adminKeyboard.router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    finally:
        pass


# schedule.every(1).minutes.do(notification, bot)
if __name__ == "__main__":
    asyncio.run(telegram())

