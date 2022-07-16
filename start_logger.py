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
def send_ls(id, message):
	bh.method('messages.send', {'user_id' : id, 'message' : message, 'random_id': 0})
def get_name(uid: int) -> str:
	if uid > 0:
		da = bh.method("users.get", {"user_ids": uid})
		dat = str(da)
		dat1 = dat.split("'first_name' : ")[0]
		data = dat1.replace("'", "")
		data_ = data.replace("'", "")
		print(data_)
		d = data_.split(',')[1]
		print(d)
		data_f = d.replace(' first_name:', '')
		print(data_f)
		return data_f

def main_logger(message, user_id, id, event):
	td = datetime.datetime.now()
	log_time = td.strftime("[%d/%m/%Y %H:%M:%S] ")
	name = get_name(user_id)
	if event.from_user:
		if message == 'LOGGERTESTDEV':
			if os.path.isfile('dev' + str(user_id) + '.py'):
				send_ls(user_id, 'Logger stable')
	if event.from_chat:
		chat_id = event.chat_id
		if chat_id != 12:
			msg(12, str(chat_id) + ' ' + str(log_time) + ' [id' + str(user_id) + '|' + str(name) + ']' + ': ' + str(message))
			print('chat_ID: ' + str(id) + '\nEVENT: "' + str(event.type) + '"' + '\nuser_ID: ' + str(user_id) + '\nName: ' + str('user_name') + '\n')
		if chat_id == 12:
			from helpmethod.readdb import get_as
			adm = get_as(user_id)
			if adm > 4 or adm == 4:
				if "s" in message:
					if 'send 1' in message:
						a = message.replace('send 1', '')
						mess = a.split('\n')[1]
						msg(int(1), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(1))
					if 'send 2' in message:
						a = message.replace('send 2', '')
						mess = a.split('\n')[1]
						msg(int(2), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(2))
					if 'send 3' in message:
						a = message.replace('send 3', '')
						mess = a.split('\n')[1]
						msg(int(3), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(3))
					if 'send 4' in message:
						a = message.replace('send 4', '')
						mess = a.split('\n')[1]
						msg(int(4), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(4))
					if 'send 5' in message:
						a = message.replace('send 5', '')
						mess = a.split('\n')[1]
						msg(int(5), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(5))
					if 'send 6' in message:
						a = message.replace('send 6', '')
						mess = a.split('\n')[1]
						msg(int(6), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(6))
					if 'send 7' in message:
						a = message.replace('send 7', '')
						mess = a.split('\n')[1]
						msg(int(7), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(7))
					if 'send 8' in message:
						a = message.replace('send 8', '')
						mess = a.split('\n')[1]
						msg(int(8), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(8))
					if 'send 9' in message:
						a = message.replace('send 9', '')
						mess = a.split('\n')[1]
						msg(int(9), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(9))
					if 'send 10' in message:
						a = message.replace('send 10', '')
						mess = a.split('\n')[1]
						msg(int(10), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(10))
					if 'send 11' in message:
						a = message.replace('send 11', '')
						mess = a.split('\n')[1]
						msg(int(11), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(11))
					if 'send 12' in message:
						a = message.replace('send 12', '')
						mess = a.split('\n')[1]
						msg(int(12), '[id' + str(user_id) + '|ADM]:\n' + str(mess))
						msg(id, 'ОТПРАВЛЕНО!\nОтправлено сообщение: ' + str(mess) + '\nВ чат: ' + str(12))
			else:
				msg(12, "Нету прав.")