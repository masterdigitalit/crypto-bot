from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
button1 = KeyboardButton(text='да')
button2 = KeyboardButton(text='нет')


markup5 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[ [button1], [button2]], )




greet_kb = markup5