import sqlite3

try:
    db = sqlite3.connect('MDB.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE users (
                id BIGINT,
                nickname TEXT,
                admin_lvl INT,
                balance BIGINT,
                ban_state INT,
                bonus datetime)''')
    print("База данных подключена к SQLite")

    db.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (db):
        db.close()
        print("Соединение с SQLite закрыто")
input()