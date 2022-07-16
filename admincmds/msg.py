import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

vk = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll_Ls = VkLongPoll(vk)
def send_ls(id, message):
	vk.method('messages.send', {'user_id' : id, 'message' : message, 'random_id': 0})
def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def mess(id, user_id, message):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 1 or int(admin_status) == 1:
		messa = message.replace('сообщение ', '')
		mess = messa.split(']')[1]
		id_u = messa.split(']')[0]
		if "@" in id_u:
			id_uu = id_u.split("|")[0]
			id_u = id_uu.replace('[', '')
			if "id" in id_u:
				id_u = id_u.replace("id", "")
		from helpmethod.readdb import get_nick
		u_nick = get_nick(id_u)
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		send_ls(id_u, mess)
		msg(id, '✅[id' + str(user_id) + '|' + str(nick) + '] ты отправил сообщение пользователю [id' + str(id_u) + '|' + str(u_nick) + ']:\n\n🗡 Сообщение: ' + str(mess))