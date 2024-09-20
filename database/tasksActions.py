import sqlite3
from datetime import datetime, timedelta
import json


con = sqlite3.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES, check_same_thread=False)
cursor = con.cursor()

def getNameByCode(code):
    get = cursor.execute("SELECT Name FROM Tasks WHERE uniqueCode = ?", [code])
    return get.fetchone()[0]


def selectByExecutionTime():
    get = cursor.execute("SELECT* FROM Tasks WHERE nextSendTime = ?", [datetime.now().strftime('%d.%m.%Y %H:%M')])
    return get.fetchall()


def selectByWarningTime():
    get = cursor.execute("SELECT * FROM Tasks WHERE warningTime = ? AND State = 'not-activated' ", [datetime.now().strftime('%d.%m.%Y %H:%M')])
    return get.fetchall()









