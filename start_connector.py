import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType	
import os
from os import startfile
import sys, traceback
from threading import Thread
import sqlite3

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
dev = '''import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

token = "ENTERTOKEN"
vk = vk_api.VkApi(token = token)
give = vk.get_api()
longpoll = VkLongPoll(vk)

def send(peer, text):
	vk.method('messages.send', {'peer_id' : peer, 'message' : text, 'random_id': 0})
def delete_history(peer):
	vk.method('messages.deleteConversation', {'peer_id' : peer, 'count': 1})
def edit(peer, id, text):
	vk.method('messages.edit', {'peer_id' : peer, 'message_id' : id, 'message' : text})
def delete_for_all(peer, id):
	vk.method('messages.delete', {'peer_id' : peer, 'delete_for_all': 1, 'message_id' : id})
def delete(peer, id):
	vk.method('messages.delete', {'peer_id' : peer, 'delete_for_all': 0, 'message_id' : id})

def main():
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			message = event.text.lower()
			user_id = event.peer_id
			u_id = event.user_id
			peer = event.peer_id
			mess_id = event.message_id
			if event.from_me:
				if message == '.cl':
					delete_history(peer)
				if event.text == '.cbs':
					peer1 = -210219643
					edit(peer, mess_id, 'Checking...')
					send(peer1, 'PQPCHATTESTDEV')
					mess_ida = event.message_id
					for event1 in longpoll.listen():
						if event1.type == VkEventType.MESSAGE_NEW:
							if event1.text == 'pqp_chat stable':
								mess_id1 = event1.message_id
								send(peer1, 'CONNECTORTESTDEV')
								mess_idb = event1.message_id
								for event2 in longpoll.listen():
									if event2.type == VkEventType.MESSAGE_NEW:
										if event2.text == 'Connector stable':
											mess_id2 = event2.message_id
											send(peer1, 'LOGGERTESTDEV')
											mess_idc = event2.message_id
											for event3 in longpoll.listen():
												if event3.type == VkEventType.MESSAGE_NEW:
													if event3.text == 'Logger stable':
														mess_id3 = event3.message_id
														edit(peer, mess_id, 'All servers stable')
														delete_history(peer1)
														main()
				if event.text == '.rab':
					edit(peer, mess_id, 'Выполняется...')
					import os
					from os import startfile
					os.system("taskkill /im cmd.exe")
					os.system("taskkill /im primat.exe")
					tasks1 = os.popen('tasklist').read()
					newtasks1 = tasks1.replace('logger.exe', '')
					if tasks1 == newtasks1:
						h = '"D:\Bot\__start__.bat"'
						startfile(h)
						edit(peer, mess_id, 'Все боты перезагружены')
					else:
						edit(peer, mess_id, 'Все боты перезагружены')
				if '.spm ' in message:
					text = message.replace('.spm ', '')
					send(peer, text)
					send(peer, text)
					send(peer, text)
					edit(peer, mess_id, '[PRIMAT DEV] SUCCES')
				if message == '.info':
					from helpmethod.readdb import get_as
					adm = get_as(id)
					from helpmethod.readdb import get_nick
					nick = get_nick(id)
					if int(adm) == 0:
						n = '[0] Пользователь'
					elif int(adm) == 1:
						n = '[1] Модератор'
					elif int(adm) > 1 and int(adm) < 2:
						n = '[1] Тестер'
					elif int(adm) == 2:
						n = '[2] Гл.Модератор'
					elif int(adm) == 3:
						n = '[3] Администрато'
					elif int(adm) == 4:
						n = '[4] Гл.Администратор'
					elif int(adm) == 5:
						n = '[5] Куратор Модераторов'
					elif int(adm) == 6:
						n = '[6] Куратор Тестеров'
					elif int(adm) == 7:
						n = '[7] Куратор Администраторов'
					elif int(adm) == 8:
						n = '[8] Разработчик'
					elif int(adm) == 9:
						n = '[9] Куратор Разработчиков'
					elif int(adm) == 10:
						n = '[10] Гл.Куратор'
					elif int(adm) == 11:
						n = '[11] Владелец'
					edit(peer, mess_id, '[PRIMAT DEV] Ты [id' + str(u_id) + '|' + str(nick) + ']Твой статус в боте: ' + n + 'Ты используюшь: PRIMAT-DEV_BOT')
				if message == '.help':
					edit(peer, mess_id, """Команды бота:
1) .send adm_cmd - отправить админ команды
2) .info - отправить свою информацию
3) .cbs - посмотреть лаги бота
4) .cl - очистить чат
5) .spm (Сообщение) - отправить 3 сообщения 
6) .help - список команд
7) .rab - перезагрузить всех ботов
8) .reconnect - переподключить бота""")
				if message == '.send adm_cmd':
					edit(peer, mess_id, """[PRIMAT DEV] Команды администрации:
[1] Модератор, [1] Тестер:
balance {user} - узнать баланс пользователя
resbal - сбросить себе баланс
сообщение {user} {сообщение} - отправить пользователю сообщение в лс
[2] Гл.Модератор:
твоя инфа {user} - узнать информацию о пользователе
sb {balance} - установить себе баланс
[3] Администратор:
бан {user} - забанить пользователя
дубль {сообщение} - продублировать сообщение от имени бота
[4] Гл.Администратор:
разбан {user} - разбанить пользователя
рассылка {сообщение} - отправить сообщение во все чаты от имени бота
sub {user} {balance} - установить пользователю баланс
[5] Куратор Модераторов:
setstat {user} 1, 2 - выдать пользователю Модератора/Гл.Модератора
[6] Куратор Тестеров:
setstat {user} 1.5
[7] Куратор Администраторов:
setstat {user} 1, 1.5, 2, 3, 4
[8] Разработчик:
Имеет все команды
[9] Куратор Разработчиков:
Имеет все команды
[10] Гл.Куратор:
Имеет все команды
[11] Владелец:
Имеет все команды

Несколько моментов:
1. Тестеры получают команды на тест индивидуально, чтобы не было крашей бота.
2. Логгер доступен от Гл.Админа
!!! Будет дополняться""")

main()'''

adm = '''import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

token = ENTERTOKEN
vk = vk_api.VkApi(token = token)
give = vk.get_api()
longpoll = VkLongPoll(vk)

def send(id, text):
	vk.method('messages.send', {'peer_id' : id, 'message' : text, 'random_id': 0})
def delete_history():
	vk.method('messages.deleteConversation', {'peer_id' : event.peer_id, 'count': 1})
def edit(text):
	vk.method('messages.edit', {'peer_id' : event.peer_id, 'message_id' : event.message_id, 'message' : text})


for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		message = event.text.lower()
		chat_id = event.peer_id
		id = event.user_id
		if event.from_me:
			if message == '.cl':
				delete_history()
			if message == '.cbs':
				edit('[PRIMAT ADM] No lags')
			if '.spm ' in message:
				text = message.replace('.spm ', '')
				send(chat_id, text)
				send(chat_id, text)
				send(chat_id, text)
				edit('[PRIMAT ADM] SUCCES')
			if message == '.info':
				from helpmethod.readdb import get_as
				adm = get_as(id)
				from helpmethod.readdb import get_nick
				nick = get_nick(id)
				if int(adm) == 0:
					n = '[0] Пользователь'
				elif int(adm) == 1:
					n = '[1] Модератор'
				elif int(adm) > 1 and int(adm) < 2:
					n = '[1] Тестер'
				elif int(adm) == 2:
					n = '[2] Гл.Модератор'
				elif int(adm) == 3:
					n = '[3] Администрато'
				elif int(adm) == 4:
					n = '[4] Гл.Администратор'
				elif int(adm) == 5:
					n = '[5] Куратор Модераторов'
				elif int(adm) == 6:
					n = '[6] Куратор Тестеров'
				elif int(adm) == 7:
					n = '[7] Куратор Администраторов'
				elif int(adm) == 8:
					n = '[8] Разработчик'
				elif int(adm) == 9:
					n = '[9] Куратор Разработчиков'
				elif int(adm) == 10:
					n = '[10] Гл.Куратор'
				elif int(adm) == 11:
					n = '[11] Владелец'
				edit('[PRIMAT ADM] Ты [id' + str(id) + '|' + str(nick) + ']Твой статус в боте: ' + n + 'Ты используюшь: PRIMAT-ADM_BOT')
			if message == '.help':
				edit("""[PRIMAT ADM] Команды бота:\n1) .send adm_cmd - отправить админ команды\n2) .info - отправить свою информацию\n3) .cbs - посмотреть лаги бота\n4) .cl - очистить чат\n5) .spm (Сообщение) - отправить 3 сообщения \n6) .help - список команд\n7) .reconnect - переподключить бота""")
			if message == '.send adm_cmd':
				edit("""[PRIMAT ADM] Команды администрации:
[1] Модератор, [1] Тестер:
balance {user} - узнать баланс пользователя
resbal - сбросить себе баланс
сообщение {user} {сообщение} - отправить пользователю сообщение в лс
[2] Гл.Модератор:
твоя инфа {user} - узнать информацию о пользователе
sb {balance} - установить себе баланс
[3] Администратор:
бан {user} - забанить пользователя
дубль {сообщение} - продублировать сообщение от имени бота
[4] Гл.Администратор:
разбан {user} - разбанить пользователя
рассылка {сообщение} - отправить сообщение во все чаты от имени бота
sub {user} {balance} - установить пользователю баланс
[5] Куратор Модераторов:
setstat {user} 1, 2 - выдать пользователю Модератора/Гл.Модератора
[6] Куратор Тестеров:
setstat {user} 1.5
[7] Куратор Администраторов:
setstat {user} 1, 1.5, 2, 3, 4
[8] Разработчик:
Имеет все команды
[9] Куратор Разработчиков:
Имеет все команды
[10] Гл.Куратор:
Имеет все команды
[11] Владелец:
Имеет все команды

Несколько моментов:
1. Тестеры получают команды на тест индивидуально, чтобы не было крашей бота.
2. Логгер доступен от Гл.Админа
!!! Будет дополняться""")'''

def main_connector(message, id, user_id, event):
	if message == '.reconnect':
		if os.path.isfile('dev' + str(user_id) + '.py'):
			h = '"D:\Bot\dev' + str(user_id) + '.py"'
			startfile(h)
			msg(id, '[DEV BOT] Бот был подключен.')
		elif os.path.isfile('dAdm' + str(user_id) + '.py'):
			h = '"D:\Bot\dAdm' + str(user_id) + '.py"'
			startfile(h)
			msg(id, '[ADM BOT] Бот был подключен.')
		else:
			msg(id, 'Ты не зареган, используй: .connect')
	if message == '.connect':
		msg(id, '''Чтобы подключить бота пиши:
			.connect dev bot - бот для разработчиков
			.connect admin bot - бот для персонал
			.reconnect - если уже подключал бота, но он выключился''')
	if message == '.connect dev bot':
		th = Thread(args=())
		th.start()
		from helpmethod.readdb import get_as
		admin_status = get_as(user_id)
		if int(admin_status) > 8 or int(admin_status) == 8:
			link = 'https://vk.cc/ceSMvM'
			msg(id, 'WELCOME!\nВы попали в мастер установки PRIMAT-DEV_BOT\nЧтобы установить бота: \n1. Перейдите по ссылке: ' + link + '\n2. Дайте разрешения\n3. Скопируйте ссылку и вставьте её сюда.')
			for event in longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					mess = str(event.message.text)
					if 'https://oauth.vk.com/' in mess:
						toke = mess.replace('https://oauth.vk.com/blank.html#access_token=', '')
						tok = toke.split('&')[0]
						msg(id, 'Регистрирую...')
						print('[' + str(user_id) + '] Подключаю...')
						tokenn = '"' + str(tok) + '"'
						code_dev = dev.replace('ENTERTOKEN', tokenn)
						with open('dev' + str(user_id) + '.py', 'w+', encoding="utf-8") as f:
							f.write(str(code_dev))
						h = '"D:\Bot\dev' + str(user_id) + '.py"'
						print(h)
						print('Пользователь запущен успешно...')

						msg(id, 'SUCESS!')
						startfile(h)
						
						print('reload...')
						main_connector()
	elif message == '.connect admin bot':
		th = Thread(args=())
		th.start()
		from helpmethod.readdb import get_as
		admin_status = get_as(user_id)
		if int(admin_status) > 1 or int(admin_status) == 1:
			link = 'https://vk.cc/ceSMvM'
			msg(id, 'WELCOME!\nВы попали в мастер установки PRIMAT-ADM_BOT\nЧтобы установить бота: \n1. Перейдите по ссылке: ' + link + '\n2. Дайте разрешения\n3. Скопируйте ссылку и вставьте её сюда.')
			for event in longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					mess = str(event.message.text)
					if 'https://oauth.vk.com/' in mess:
						toke = mess.replace('https://oauth.vk.com/blank.html#access_token=', '')
						tok = toke.split('&')[0]
						msg(id, 'Регистрирую...')
						print('[' + str(user_id) + '] Подключаю...')
						tokenn = '"' + str(tok) + '"'
						code_adm = adm.replace('ENTERTOKEN', tokenn)
						with open('dAdm' + str(user_id) + '.py', 'w+', encoding="utf-8") as f:
							f.write(str(code_adm))
						h = '"D:\Bot\dAdm' + str(user_id) + '.py"'
						print(h)
						print('Пользователь запущен успешно...')

						msg(id, 'SUCESS!')
						startfile(h)
						print('reload...')

						main_connector()