import sqlite3

with open('elements.sql', 'r', encoding='UTF-8') as _:
    sql = _.read()

database = sqlite3.connect('database.sqlite')
controller = database.cursor()

controller.executescript(sql)

database.commit()
