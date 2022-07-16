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
def is_num(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def set_stat(id, user_id, message):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 5 or int(admin_status) == 5:
		useer = message.replace('setstat ', '')
		user = useer.split(' ')[0]
		stat = useer.split(' ')[1]
		if "@" in user:
			userr = user.split("|")[0]
			user = userr.replace('[', '')
			if "id" in user:
				user = user.replace("id", "")
				if int(stat) == 0:
					setstat = '[0] Пользователь'
				elif int(stat) == 1:
					setstat = '[1] Модератор'
				elif int(stat) > 1 and int(stat) < 2:
					setstat = '[1] Тестер'
				elif int(stat) == 2:
					setstat = '[2] Гл.Модератор'
				elif int(stat) == 3:
					setstat = '[3] Администрато'
				elif int(stat) == 4:
					setstat = '[4] Гл.Администратор'
				elif int(stat) == 5:
					setstat = '[5] Куратор Модераторов'
				elif int(stat) == 6:
					setstat = '[6] Куратор Тестеров'
				elif int(stat) == 7:
					setstat = '[7] Куратор Администраторов'
				elif int(stat) == 8:
					setstat = '[8] Разработчик'
				elif int(stat) == 9:
					setstat = '[9] Куратор Разработчиков'
				elif int(stat) == 10:
					setstat = '[10] Гл.Куратор'
				elif int(stat) == 11:
					setstat = '[11] Владелец'
			if int(admin_status) == 5:
				if int(stat) < 3 and int(stat) != 1.1 and int(stat) != 1.2 and int(stat) != 1.3 and int(stat) != 1.4 and int(stat) != 1.5 and int(stat) != 1.6 and int(stat) != 1.7 and int(stat) != 1.8 and int(stat) != 1.9:
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET admin_lvl = ? WHERE id = ?""", (stat, user))
					sqlite_connection.commit()
					cur.close()
					msg(id, '✅[id' + str(user_id) + '|Ты] дал [id' + str(user) + '|ему] статус: ' + setstat)
			elif int(admin_status) == 6:
				if int(stat) == 1.1 or int(stat) == 1.2 or int(stat) == 1.3 or int(stat) == 1.4 or int(stat) == 1.5 or int(stat) == 1.6 or int(stat) == 1.7 or int(stat) == 1.8 or int(stat) == 1.9:
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET admin_lvl = ? WHERE id = ?""", (stat, user))
					sqlite_connection.commit()
					cur.close()
					msg(id, '✅[id' + str(user_id) + '|Ты] дал [id' + str(user) + '|ему] статус: ' + setstat)
			elif int(admin_status) == 7:
				if int(stat) < 5:
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET admin_lvl = ? WHERE id = ?""", (stat, user))
					sqlite_connection.commit()
					cur.close()
					msg(id, '✅[id' + str(user_id) + '|Ты] дал [id' + str(user) + '|ему] статус: ' + setstat)
			elif int(admin_status) > 8 or int(admin_status) == 8:
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET admin_lvl = ? WHERE id = ?""", (stat, user))
				sqlite_connection.commit()
				cur.close()
				msg(id, '✅[id' + str(user_id) + '|Ты] дал [id' + str(user) + '|ему] статус: ' + setstat)
		else:
			msg(id, '[id' + user + '|Пользователь] не зарегистрирован в базе данных.')