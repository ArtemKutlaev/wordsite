import sqlite3


db = sqlite3.connect('text.db')
c = db.cursor()


#Создаем базу данных
c.execute('''
    CREATE TABLE IF NOT EXISTS text(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT 
    )
''')
db.commit()
