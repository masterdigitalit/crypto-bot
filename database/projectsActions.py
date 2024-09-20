import sqlite3
from datetime import datetime, timedelta
import json


con = sqlite3.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES, check_same_thread=False)
cursor = con.cursor()


def getAllProjects(only_titles):
    if only_titles:
        get = cursor.execute("SELECT Name FROM Projects" )
        return get.fetchall()
def isProjectHasDaily(name):
    get = cursor.execute("SELECT daily FROM Projects WHERE Name = ?", [name])
    return get.fetchone()
def getProjectLink(name):
    get = cursor.execute("SELECT link FROM Projects WHERE Name = ?", [name])
    return get.fetchone()[0]
def getProjectPeriodicTime(name):
    get = cursor.execute("SELECT pereodicTime FROM Projects WHERE Name = ?", [name])
    return get.fetchone()
def addNewProject(name, periodic,pereodic_time, daily, link):
    cursor.execute(
        "INSERT INTO Projects ( Name, pereodic,pereodicTime, daily,link) VALUES (?,?,?,?,?)",
        [name, periodic,pereodic_time, daily, link])
    con.commit()