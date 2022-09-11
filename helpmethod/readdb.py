import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import humanize

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()
def msg(id, text):
    bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def send(id, text, keyboard):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})
def create_keyboard(message):
    keyboard = VkKeyboard(one_time=True)
 
    if message == 'начать' or message == 'вернуться':
        keyboard.add_button('Моя инфа', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Баланс', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Помощь', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Прокачать уровень', color=VkKeyboardColor.POSITIVE)
    if message == 'прокачать уровень':
        keyboard.add_button('Прокачать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вернуться', color=VkKeyboardColor.SECONDARY)
    keyboard = keyboard.get_keyboard()
    return keyboard
def get_balance(id):
    sqlite_connection = sqlite3.connect('databases\MDB.db')
    cursor = sqlite_connection.cursor()

    sql_select_query = """select * from users where id = ?"""
    cursor.execute(sql_select_query, (id,))
    records = cursor.fetchall()
    for row in records:
        balik = row[3]
        return balik
def get_all(user_id, id):
    try:
        if user_id == id:
            sqlite_connection = sqlite3.connect('databases\MDB.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from users where id = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            record = cursor.fetchone()
            nick = get_nick(user_id)
            status = get_as(user_id)
            ggg = get_balance(user_id)
            gems = get_specbal(user_id)
            cases = get_case(user_id)
            levl = get_lvl(user_id)
            rebirth = str(int(get_koef(user_id)) - 1)
            lvl = '\n🏐Твой уровень: ' + str(levl)
            if float(status) > 1 or float(status) == 1:
                if float(status) == 1:
                    n = '[1] Хелпер'
                    send(id, '📕 H | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 2:
                    n = '[2] Модератор'
                    send(id, '📕 M | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 3:
                    n = '[3] Гл.Модератор'
                    send(id, '📕 Sr.M | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 4:
                    n = '[4] Куратор'
                    send(id, '📕 Cur | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 5:
                    n = '[5] Разработчик'
                    send(id, '📕 Dev | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 8:
                    n = '[5] Тестер'
                    send(id, '📕 T | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 6:
                    n = '[6] Администратор'
                    send(id, '📕 ADM | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
                elif float(status) == 7:
                    n = '[7] Владелец'
                    send(id, '📕 OWN | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))
            else:
                send(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth, create_keyboard('начать'))

        else:
            sqlite_connection = sqlite3.connect('databases\MDB.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from users where id = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            record = cursor.fetchone()
            nick = get_nick(user_id)
            status = get_as(user_id)
            ggg = get_balance(user_id)
            gems = get_specbal(user_id)
            cases = get_case(user_id)
            levl = get_lvl(user_id)
            rebirth = str(int(get_koef(user_id)) - 1)
            lvl = '\n🏐Твой уровень: ' + str(levl)
            if float(status) > 1 or float(status) == 1:
                if int(status) == 1:
                    n = '[1] Хелпер'
                    msg(id,'📕 H | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth) 
                elif int(status) == 2:
                    n = '[2] Модератор'
                    msg(id,'📕 M | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth)  
                elif int(status) == 3:
                    n = '[3] Гл.Модератор'
                    msg(id,'📕 Sr.M | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth)  
                elif int(status) == 4:
                    n = '[4] Куратор'
                    msg(id,'📕 Cur | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth)  
                elif int(status) == 5:
                    n = '[5] Разработчик'
                    msg(id,'📕 Dev | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth)  
                elif int(status) == 8:
                    n = '[5] Тестер'
                    msg(id,'📕 T | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth) 
                elif int(status) == 6:
                    n = '[6] Администратор'
                    msg(id,'📕 ADM | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth) 
                elif int(status) == 7:
                    n = '[7] Владелец'
                    msg(id,'📕 OWN | [id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth) 
            else:
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases) + lvl + '\n📊Твои перерождения: ' + rebirth)

    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при работе с SQLite", error)
def is_ban(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            ban_state = record[4]
            return ban_state
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_bonus(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[5]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_as(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            admin = record[2]
            return admin
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_nick(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            nick = record[1]
            return nick
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_case(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[6]
            if bonus == None:
                return 0
            else:
                return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_specbal(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[7]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_rabs(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[8]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_addchat(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[9]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def get_texstat(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[10]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_lvl(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[11]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_koef(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[12]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_tasks(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[15]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_bans(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[14]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_forban(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[18]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_mute_State(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[19]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def get_curator(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[13]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def get_warns(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[16]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
def get_rebuke(user_id):
    try:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cursor = sqlite_connection.cursor()

        sql_select_query = """select * from users where id = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        for record in records:
            cursor.close()
            bonus = record[17]
            return bonus
    except sqlite3.Error as error:
        print("[READ_DB] Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()