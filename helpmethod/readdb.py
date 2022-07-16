import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import humanize

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()
def msg(id, text):
    bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def get_balance(id):
    sqlite_connection = sqlite3.connect('databases\MDB.db')
    cursor = sqlite_connection.cursor()

    sql_select_query = """select * from users where id = ?"""
    cursor.execute(sql_select_query, (id,))
    records = cursor.fetchall()
    for row in records:
        balik = row[3]
        print('[READ_DB]: ' + str(balik))
        return balik
def get_all(user_id, id):
    try:
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
        if float(status) > 1 or float(status) == 1:
            if float(status) == 1:
                n = '[1] Модератор'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' +  humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) > 1.1 and float(status) < 2:
                n = '[1] Тестер'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 2:
                n = '[2] Гл.Модератор'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 3:
                n = '[3] Администратор'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 4:
                n = '[4] Гл.Администратор'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 5:
                n = '[5] Куратор Модераторов'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 6:
                n = '[6] Куратор Тестеров'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 7:
                n = '[7] Куратор Администраторов'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 8:
                n = '[8] Разработчик'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 9:
                n = '[9] Куратор Разработчиков'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 10:
                n = '[10] Гл.Куратор'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
            elif float(status) == 11:
                n = '[11] Владелец'
                msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: ' + n + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))
        else:
            msg(id, '📕[id' + str(user_id) + "|" + str(nick) + '] твой профиль:\n💰 Баланс: ' + humanize.intcomma(str(ggg)) + "$" + '\n🗽 Твой статус среди администрации: [0] Пользователь' + '\n💎Твои гемы: ' + humanize.intcomma(gems) + '\n🎁Твои кейсики: ' + humanize.intcomma(cases))

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