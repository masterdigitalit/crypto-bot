import sqlite3
from datetime import datetime, timedelta
import json
import aiosqlite


con = sqlite3.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES, check_same_thread=False)
cursor = con.cursor()

def createUser(id, name,projects):
    cursor.execute("INSERT INTO Users (telegramId, Name, registeredProjects,dateRegistered, Status) VALUES (?,?,?,?,?)", [id, name,f'{projects}', (datetime.now()).strftime('%d.%m.%Y %H:%M'), 'user'])
    con.commit()

def isUserRegistered(id):
    get = cursor.execute("SELECT Id FROM Users WHERE telegramId = ?", [id])
    return get.fetchone()

async def getUserRegistration(id):
    db = await aiosqlite.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                                                               sqlite3.PARSE_COLNAMES, check_same_thread=False)
    cursor = await db.cursor()
    get = await cursor.execute("SELECT registeredProjects FROM Users WHERE telegramId = ?", [id])
    get = await get.fetchone()
    return json.loads(get[0])


def createTask(code, name, type, userId, time=0):
    if type == 'periodic':
        cursor.execute("INSERT INTO Tasks (uniqueCode, Name, dateCreated,confirmationDate, warningTime,State, Type,nextSendTime, userId) VALUES (?,?,?,?,?,?,?,?,?)", [code, name,datetime.now().strftime('%d.%m.%Y %H:%M'),(datetime.now() + timedelta(minutes=3)).strftime('%d.%m.%Y %H:%M'),(datetime.now() + timedelta(minutes=3)).strftime('%d.%m.%Y %H:%M'),'not-activated', type,(datetime.now() + timedelta(minutes=int(time[0]))).strftime('%d.%m.%Y %H:%M'),userId ])
    else:
        cursor.execute("INSERT INTO Tasks (uniqueCode, Name, dateCreated,confirmationDate, warningTime,State, Type,nextSendTime, userId) VALUES (?,?,?,?,?,?,?,?,?)", [code, name,datetime.now().strftime('%d.%m.%Y %H:%M'),(datetime.now() + timedelta(minutes=3)).strftime('%d.%m.%Y %H:%M'),(datetime.now() + timedelta(minutes=3)).strftime('%d.%m.%Y %H:%M'),'not-activated', type,(datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y %H:%M'),userId ])

    con.commit()
def changeConfirmationState(uniqueCode, state):
    cursor.execute("UPDATE Tasks SET State = ? WHERE uniqueCode = ? ", [state, uniqueCode])
    con.commit()

async def updateUserRegistration(telegramId, name):
    db = await aiosqlite.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                                                    sqlite3.PARSE_COLNAMES, check_same_thread=False)
    cursor = await db.cursor()

    projects = await cursor.execute("SELECT registeredProjects FROM Users WHERE telegramId = ?", [telegramId])
    projects = await projects.fetchone()
    projects =   json.loads(projects[0])


    projects.append(name)
    projects = json.dumps(projects)
    await cursor.execute("UPDATE Users SET registeredProjects = ? WHERE telegramId = ? ", [projects, telegramId])
    await db.commit()








    # get = cursor.execute("SELECT registeredProjects FROM Users WHERE telegramId = ?", [telegramId])
    #
    # projects =  json.loads(get.fetchone()[0])
    # print(projects, name)
    # projects.append(name)
    # projects = json.dumps(projects)
    # cursor.execute("UPDATE Users SET registeredProjects = ? WHERE telegramId = ? ", [projects, telegramId])
    # con.commit()
def getUserStatus(telegramId):
    get = cursor.execute("SELECT Status FROM Users WHERE telegramId = ?", [telegramId])
    return get.fetchone()[0]

def getAllUsers():
    get = cursor.execute("SELECT * FROM Users ", )
    return get.fetchall()