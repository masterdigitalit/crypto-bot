from aiogram.types import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
    InlineKeyboardButton, CallbackQuery, )


def confirmationButtonReg(code, last):

    #
    yes = InlineKeyboardButton(
        text=" выполнил ✅",
        callback_data=f'reg:done:{"last:" if last  else ""}{code}'
    )
    no = InlineKeyboardButton(
        text=" провалено ❌",
        callback_data=f'reg:not_done:{"last:" if last  else ""}{code}'
    )
    row = [yes, no]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def confirmationButtonDailyReg(code, last):

    #
    yes = InlineKeyboardButton(
        text=" выполнил ✅",
        callback_data=f'reg:done:{"last:" if last  else ""}{code[0]}:{code[1]}'
    )
    no = InlineKeyboardButton(
        text=" провалено ❌",
        callback_data=f'reg:not_done:{"last:" if last  else ""}{code[0]}:{code[1]}'
    )
    row = [yes, no]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)
def confirmationButton(code):

    #
    yes = InlineKeyboardButton(
        text=" выполнил ✅",
        callback_data=f'user:done:{code}'
    )
    no = InlineKeyboardButton(
        text=" Пропустил ❌",
        callback_data=f'user:not_done:{code}'
    )
    row = [yes, no]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def confirmationButtonDaily(code):

    #
    yes = InlineKeyboardButton(
        text=" выполнил ✅",
        callback_data=f'user:done:{code[0]}:{code[1]}'
    )
    no = InlineKeyboardButton(
        text=" Пропустил ❌",
        callback_data=f'user:not_done:{code[0]}:{code[1]}'
    )
    row = [yes, no]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def menu(items=[]):
    buttons = []
    for el in items:
        buttons.append(InlineKeyboardButton(text='hihihihihihi', callback_data='cc'))
    array_size = 2
    sliced_array = []
    i = 0
    while i < len(buttons):
        sliced_array.append(buttons[i: i + array_size])
        i += array_size
    doAll =  [InlineKeyboardButton(text='Пройти все', callback_data='cc')]
    settings =  [InlineKeyboardButton(text='Настройки', callback_data='cc')]
    rows = [doAll, *sliced_array, settings]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def registration(items=[], doall=True):
    buttons = []
    for el in items:
        buttons.append(InlineKeyboardButton(text=el, callback_data=f'reg:oppr:last:{el}'))
    array_size = 2
    sliced_array = []
    i = 0
    while i < len(buttons):
        sliced_array.append(buttons[i: i + array_size])
        i += array_size
    doAll =  [InlineKeyboardButton(text='Пройти все', callback_data='reg:do_All')]
    update = [InlineKeyboardButton(text='Перепройти', callback_data='reg:update')]

    rows = [filter(lambda x: doall , doAll), *sliced_array, update]
    return InlineKeyboardMarkup(inline_keyboard=rows)

def Start(name, last):
    rows = [InlineKeyboardButton(text='Начать', callback_data=f'reg:oppr:{"last:" if last  else ""}{name}'),
            InlineKeyboardButton(text='Назад' , callback_data=f'reg:back:{"last:" if last  else ""}' )
           ]
    return InlineKeyboardMarkup(inline_keyboard=[rows])

def AdminKb():
    buttons = []
    items = []
    for el in items:
        buttons.append(InlineKeyboardButton(el, callback_data=f'reg:oppr:last:{el}'))
    array_size = 2
    sliced_array = []
    i = 0
    while i < len(buttons):
        sliced_array.append(buttons[i: i + array_size])
        i += array_size
    doAll = [InlineKeyboardButton(text='Статистика', callback_data='admin:show_statistic')]
    update = [InlineKeyboardButton(text='Изменить настройки проектов', callback_data='admin:change_project')]
    add = [InlineKeyboardButton(text='Добавить проект', callback_data='admin:add_project')]

    rows = [doAll, *sliced_array,add, update]
    return InlineKeyboardMarkup(inline_keyboard=rows)


