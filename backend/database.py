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

def clear_database():
    #Функция для очистки базы данных parser_db
    c.execute('DELETE FROM text') 
    c.execute('DELETE FROM sqlite_sequence WHERE name="text"')
    db.commit()

clear_database()
