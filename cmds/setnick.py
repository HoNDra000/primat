import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
	
def setnick(id, user_id, message):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if 'nick ' in message:
		set_nick = message.replace('setnick ', '')
	elif 'ник ' in message:
		set_nick = message.replace('сетник ', '')
	if admin_status > 4 or admin_status == 4:
		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()

		cur.execute(f"""UPDATE users SET nickname = ? WHERE id = ?""", (set_nick, user_id))
		sqlite_connection.commit()
		cur.close()
		msg(id, '✅[id' + str(user_id) + '|Ты] установил себе новый ник, теперь ты : ' + str(set_nick))
	else:
		leight = len(str(set_nick))
		if leight < 15:
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET nickname = ? WHERE id = ?""", (set_nick, user_id))
			sqlite_connection.commit()
			cur.close()
			msg(id, '✅[id' + str(user_id) + '|Ты] установил себе новый ник, теперь ты : ' + str(set_nick))
		else:
			msg(id, 'ник не может содержать более 15 символов')