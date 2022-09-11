import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def unban(id, user_id, user):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 3 or int(admin_status) == 3:
		from helpmethod.readdb import is_ban
		ban_status = is_ban(user)
		if ban_status == 1:
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET ban_state = ? WHERE id = ?""", (0, user))
			sqlite_connection.commit()
			cur.close()
			msg(id, '✅[id' + str(user) + '|Пользователь] успешно разбанен.')
			from helpmethod.readdb import get_nick
			nick = get_nick(user_id)
			u_nick = get_nick(user)

			msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду unban на пользователе [id' + str(user) + '|' + str(u_nick) + ']\n#unban')
		elif ban_status != 1:
			msg(id, '[id' + str(user) + '|Пользователь] не имеет бана.')