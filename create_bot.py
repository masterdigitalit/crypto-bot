from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
from pythonEnv import getKeyFromEnv

bot = Bot(token=getKeyFromEnv('TOKEN'))
dp = Dispatcher(bot)