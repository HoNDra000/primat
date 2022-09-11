import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
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
def post(text):
	vk.method('wall.post', {'owner_id' : -210219643, 'message' : text, 'from_group': 1})


def set_stat(id, user_id, message):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 4 or int(admin_status) == 4:
		useer = message.replace('setstat ', '')
		user = useer.split(' ')[0]
		stat = useer.split(' ')[1]
		if "@" in user:
			userr = user.split("|")[0]
			user = userr.replace('[', '')
			if "id" in user:
				user = user.replace("id", "")
				old_stat = get_as(user)
				if str(stat) == 'tester' or str(stat) == 'test' or str(stat) == 'тест' or str(stat) == 'тестер':
					stat = 8
					setstat = '[5] Тестер'
				elif str(stat) == '0' or str(stat) == 'user' or str(stat) == 'юзер' or str(stat) == 'пользователь':
					stat = 0
					setstat = '[0] Пользователь'
				elif str(stat) == '1' or str(stat) == 'help' or str(stat) == 'helper' or str(stat) == 'хелп' or str(stat) == 'хелпер':
					stat = 1
					setstat = '[1] Хелпер'
				elif str(stat) == '2' or str(stat) == 'moder' or str(stat) == 'moderator' or str(stat) == 'mod' or str(stat) == 'мод' or str(stat) == 'модер' or str(stat) == 'модератор':
					stat = 2
					setstat = '[2] Модератор'
				elif str(stat) == '3' or str(stat) == 'srmoder' or str(stat) == 'srmoderator' or str(stat) == 'srmod' or str(stat) == 'срмод' or str(stat) == 'срмодер' or str(stat) == 'срмодератор':
					stat = 3
					setstat = '[3] Гл.Модератор'
				elif str(stat) == '4' or str(stat) == 'cur' or str(stat) == 'curator' or str(stat) == 'кур' or str(stat) == 'куратор':
					stat = 4
					setstat = '[4] Куратор'
				elif str(stat) == '5' or str(stat) == 'dev' or str(stat) == 'developer' or str(stat) == 'разраб' or str(stat) == 'разработчик':
					stat = 5
					setstat = '[5] Разработчик'
				elif str(stat) == '6' or str(stat) == 'adm' or str(stat) == 'admin' or str(stat) == 'administrator' or str(stat) == 'адм' or str(stat) == 'админ' or str(stat) == 'администратор':
					stat = 6
					setstat = '[6] Администратор'
				elif str(stat) == '7' or str(stat) == 'own' or str(stat) == 'owner' or str(stat) == 'владелец' or str(stat) == 'овн' or str(stat) == 'овнер':
					stat = 7
					setstat = '[7] Владелец'
				else:
					msg(id, 'Не верно указана группа.')
				if int(admin_status) > 4 or int(admin_status) == 4:
					from helpmethod.readdb import get_as
					user_as = get_as(user)
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET admin_lvl = ? WHERE id = ?""", (stat, user))
					sqlite_connection.commit()
					cur.close()
					msg(id, '✅[id' + str(user_id) + '|Ты] дал [id' + str(user) + '|ему] статус: ' + setstat)
				from helpmethod.readdb import get_nick
				nick = get_nick(user_id)
				u_nick = get_nick(user)

			msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду setstat на пользователе [id' + str(user) + '|' + str(u_nick) + '] со значением: ' + setstat + '\n#setstat')