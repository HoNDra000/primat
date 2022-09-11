import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def plus_chat(chat_id, user_id):
	from helpmethod.readdb import get_as
	adm_s = get_as(user_id)
	if adm_s > 1 or adm_s == 1: 
		from helpmethod.readdb import get_addchat
		chats = get_addchat(user_id)
		with open('chats.txt', 'r') as f:
			block_chats = f.read()
		if str(chat_id) in str(block_chats):
			msg(chat_id, 'ERROR: В чате уже был бот.\nЧат не засчитан.')
		else:
			new_chats = int(chats) + 1
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET chats = ? WHERE id = ?""", (new_chats, user_id))
			sqlite_connection.commit()
			cur.close()
			with open('chats.txt', 'w') as f:
				f.write(str(block_chats) + '\n' + str(chat_id))

			with open('count_of_chats.txt', 'r') as f:
				old_count = f.read()
			new_count = int(old_count) + 1
			with open('count_of_chats.txt', 'w') as f:
				f.write(str(new_count))
			msg(chat_id, 'SUCESS: Чат успешно добавлен. \nЧисло чатов куда именно вы добавили бота: ' + str(new_chats))
			from helpmethod.readdb import get_nick
			nick = get_nick(user_id)

			msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду +chat в чате: ' + str(chat_id) + '\n#plus_chat')
