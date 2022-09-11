import vk_api
import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import sqlite3

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def get_name(uid: int) -> str:
	if uid > 0:
		da = bh.method("users.get", {"user_ids": uid})
		dat = str(da)
		dat1 = dat.split("'first_name' : ")[0]
		data = dat1.replace("'", "")
		data_ = data.replace("'", "")
		d = data_.split(',')[1]
		data_f = d.replace(' first_name:', '')
		return data_f

def main_logger():
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_chat:
				message = str(event.object.message['text'].lower())
				user_id = event.obj['message']['from_id']
				chat_id = event.chat_id
				td = datetime.datetime.now()
				log_time = td.strftime("DATE: [%d/%m/%Y %H:%M:%S] ")
				name = get_name(user_id)
				if chat_id != 49 and chat_id != 7:
					msg(12, 'Chat_ID: ' + str(chat_id) + '\n' + str(log_time) + '\n[id' + str(user_id) + '|' + str(name) + ']' + ': ' + str(message))