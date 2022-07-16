import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from threading import Thread
import humanize
from LiteVkApi import Client


token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

vk_session = Client.login(token, 210219643)

vk = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll_Ls = VkLongPoll(vk)

sqlite_connection = sqlite3.connect('databases\MDB.db')
cursor = sqlite_connection.cursor()
print("База данных создана и успешно подключена к SQLite")

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
def send_ls(id, message):
	vk.method('messages.send', {'user_id' : id, 'message' : message, 'random_id': 0})
def check_user(id, chat_id, first_name):
	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()

	met = """SELECT * FROM users WHERE id = ?"""
	cursor.execute(met, (id,))
	if cursor.fetchone() is None:
		cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (int(id), str(first_name), 0, 1000000, 0, 0))
		db.commit()
		db.close()
	else:
		db.close()
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
def kick(id, user_id):
	bh.method('messages.removeChatUser', {'chat_id' : id, 'user_id' : user_id, 'member_id' : user_id})

def main():
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.message.text)
			user_id = event.obj['message']['from_id']
			id = event.chat_id
			from start_logger import main_logger
			main_logger(message, user_id, id, event)
			if event.from_chat:
				data = bh.method("users.get", {"user_ids": user_id})
				first_name = get_name(user_id)

				from helpmethod.readdb import is_ban
				ban = is_ban(user_id)

				if ban == 1:
					if user_id > 0:
						continue
				else:
					if user_id > 0:
						db = sqlite3.connect('databases\MDB.db', timeout=20)
						cursor = db.cursor()

						met = """SELECT * FROM users WHERE id = ?"""
						cursor.execute(met, (user_id,))
						if cursor.fetchone() is None:
							cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(user_id), str(first_name), 0, 1000000, 0, 0, 0, 0))
							db.commit()
							db.close()
						else:
							db.close()


						if message == 'автомат все' or message == 'автомат всё':
							from casino.avtomat import avtomat
							from helpmethod.readdb import get_balance
							balik = get_balance(user_id)
							Thread(target=avtomat, args=(id, user_id, 1, balik)).start()
						elif message == 'я' or message == "Я":
							from cmds.ya import ya
							Thread(target=ya, args=(id, user_id,)).start()
						elif 'автомат ' in message:
							from casino.avtomat import avtomat
							stavka = message.replace('автомат ', '')
							num_ = is_num(stavka)
							if num_ == False:
								msg(id, 'ставка должна быть числом сука')
							elif num_ == True:
								tmp = int(stavka)
								Thread(target=avtomat, args=(id, user_id, 0, tmp)).start()
							else:
								msg(id, 'ERROR: Critical error avt_a01')
						elif message == 'bonus' or message == 'бонус':
							from cmds.bonus import bonus
							Thread(target=bonus, args=(id, user_id,)).start()
						elif 'setnick ' in message or 'сетник ' in message:
							from cmds.setnick import setnick
							Thread(target=setnick, args=(id, user_id, message)).start()
						elif message == 'balance' or message == 'bal' or message == 'balik' or message == 'бал' or message == 'балик' or message == 'баланс':
							from cmds.balance import balance
							ggg = Thread(target=balance, args=(user_id)).start()
							msg(id, '💰[id' + str(user_id) + '|На твоём] балансе: ' + humanize.intcomma(ggg) + '$')
						elif 'рулетка ' in message:
							if id != 7:
								from casino.roulete import rouleteStart
								Thread(target=rouleteStart, args=(id, user_id, message)).start()
						elif 'dice ' in message or 'дайс' in message or 'дайсы' in message:
							if id != 7:
								from casino.dice import start_dice
								Thread(target=start_dice, args=(id, user_id, message)).start()
						elif message == 'рулетка хелп':
							if id != 7:
								msg(id, 'Доступные форматы:\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0, Красное, Зеро, Чёрное.')
						elif message == 'help' or message == 'команды':
							from helpmethod.readdb import get_nick
							nick = Thread(target=get_nick, args=(user_id)).start()
							msg(id,
	'🛡[id' + str(user_id) + '|' + str(nick) + '] вот команды бота:\n\n' + '''1 — Я - твой профиль.
	2 — перевести [сумма] [пользователь] - перевести пользователю деньги
	3 — Баланс - Узнать свой баланс.
	4 — Сетник [ник] - Установить себе ник.''')
						elif 'перевод ' in message or 'перевести ' in message:
							if 'перевести ' in message:
								useer = message.replace('перевести ', '')
							elif 'перевод ' in message:
								useer = message.replace('перевод ', '')
							user = useer.split(' ')[0]
							ammout = useer.split(' ')[1]
							if "@" in user:
								userr = user.split("|")[0]
								user = userr.replace('[', '')
								if "id" in user:
									user = user.replace("id", "")
							print('user: ' + str(user))
							print('ammout: ' + str(ammout))
							from cmds.translate_money import perevod
							nick = Thread(target=perevod, args=(message, id, user_id, user, ammout)).start()
						elif message == '.connect admin bot' or message == '.connect dev bot' or message == '.connect' or message == '.reconnect':
							from start_connector import main_connector
							Thread(target=main_connector, args=(message, id, user_id, event)).start() 
						elif 'сообщение ' in message:
							from admincmds.msg import mess
							Thread(target=mess, args=(id, user_id, message)).start()
						elif 'дубль ' in message:
							from admincmds.dubl import dubl
							Thread(target=dubl, args=(id, user_id, message)).start()
						elif 'reset_bal' in message:
							from admincmds.reset_bal import reset_bal
							Thread(target=reset_bal, args=(id, user_id, message)).start()
						elif message == 'resbal':
							from admincmds.resbal import resbal
							Thread(target=resbal, args=(id, user_id)).start()
						elif 'set balance ' in message or 'sb ' in message:
							if 'set balance ' in message:
								from admincmds.sb import setbalance
								balance = message.replace('set balance ', '')
								Thread(target=setbalance, args=(id, user_id, balance)).start()
							elif 'sb ' in message:
								from admincmds.sb import setbalance
								balance = message.replace('sb ', '')
								Thread(target=setbalance, args=(id, user_id, balance)).start()
						elif 'balance ' in message:
							from admincmds.balance import check_bal
							Thread(target=check_bal, args=(user_id, id, message)).start()
						elif 'sub ' in message or 'set user balance ' in message:
							if 'sub ' in message:
								uid = message.replace('sub ', '')
								id_u = uid.split(' ')[0]
								if "@" in id_u:
									id_uu = id_u.split("|")[0]
									id_u = id_uu.replace('[', '')
									if "id" in id_u:
										id_u = id_u.replace("id", "")
								bal = uid.split(' ')[1]
								from admincmds.sub import sub
								Thread(target=sub, args=(id, user_id, id_u, bal)).start()
							elif 'set user balance ' in message:
								uid = message.replace('set user balance ', '')
								id_u = uid.split(' ')[0]
								if "@" in id_u:
									id_uu = id_u.split("|")[0]
									id_u = id_uu.replace('[', '')
									if "id" in id_u:
										id_u = id_u.replace("id", "")
								bal = uid.split(' ')[1]
								from admincmds.sub import sub
								Thread(target=sub, args=(id, user_id, id_u, bal)).start()
						elif 'setstat ' in message:
							from admincmds.statset import set_stat
							Thread(target=set_stat, args=(id, user_id, message)).start()
						elif message == 'case' or message == 'кейс' or message == 'кейсик':
							from cmds.opencase import open_case
							win = open_case(id, user_id)
							if win == 0:
								msg(id, 'У тя нету кейсиков')
							elif win == 1:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n10,000,000,000$')
							elif win == 2:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n5,000,000,000$')
							elif win == 3:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n25,000,000,000$')
							elif win == 4:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n1,000,000,000$')
							elif win == 5:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n50,000,000,000$')
							elif win == 6:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n100,000,000,000$')
							elif win == 7:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n1,500,000,000$')
							elif win == 8:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n1,000,000$')
							elif win == 9:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n100,000,000,000$')
							elif win == 10:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл деняк: \n1$')
							elif win == 11:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n1💎')
							elif win == 12:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n5💎')
							elif win == 13:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n10💎')
							elif win == 14:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n2💎')
							elif win == 15:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n15💎')
							elif win == 16:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n17💎')
							elif win == 17:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n4💎')
							elif win == 18:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл Гемы: \n20💎')
							elif win == 19:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл спец.предложение: \n{skidka1}')
							elif win == 20:
								msg(id, '[id' + str(user_id) + '|Ты] выйграл спец.предложение: \n{skidka2}')
							else:
								msg(id, 'error')

						elif 'unban ' in message or 'разбан ' in message:
							if 'unban ' in message:
								user = message.replace('unban ', '')
							elif 'разбан ' in message:
								user = message.replace('разбан ', '')
							if "@" in user:
								userr = user.split("|")[0]
								user = userr.replace('[', '')
								if "id" in user:
									user = user.replace("id", "")
							from admincmds.unban import unban
							Thread(target=unban, args=(id, user_id, user)).start()
						elif 'ban ' in message or 'бан ' in message:
							if 'ban ' in message:
									user = message.replace('ban ', '')
							elif 'бан ' in message:
								user = message.replace('бан ', '')
							if "@" in user:
								userr = user.split("|")[0]
								user = userr.replace('[', '')
								if "id" in user:
									user = user.replace("id", "")
							from admincmds.ban import ban
							Thread(target=ban, args=(id, user_id, user)).start()
						elif message == 'разбан' or message == 'unban':
							from helpmethod.check_answer import reply_check
							user = reply_check(give, event)
							from admincmds.unban import unban
							Thread(target=unban, args=(id, user_id, user)).start()
						elif message == 'ban' or message == 'бан':
							from helpmethod.check_answer import reply_check
							user = reply_check(give, event)
							from admincmds.ban import ban
							Thread(target=ban, args=(id, user_id, user)).start()
						elif 'твоя инфа ' in message:
							from admincmds.you import you
							Thread(target=you, args=(user_id, id, message)).start()
						elif message == 'chat_id':
							from helpmethod.readdb import get_as
							admin_status = get_as(user_id)
							if int(admin_status) > 8 or int(admin_status) == 8:
								msg(id, id)
						elif message == 'твоя инфа':
							from helpmethod.check_answer import reply_check
							user = reply_check(give, event)
							from admincmds.you import you1
							Thread(target=you1, args=(user_id, id, user)).start()
						elif message == 'givecase':
							from helpmethod.check_answer import reply_check
							user = reply_check(give, event)
							from admincmds.case import give_case
							a = give_case(user_id, id, user)
							if a == True:
								msg(id, 'Кейс был выдан [id' + str(user) + '|ему]')
							else:
								msg(id, 'error')
						elif 'рассылка ' in message:
							from helpmethod.readdb import get_as
							admin_status = get_as(user_id)
							if int(admin_status) > 4 or int(admin_status) == 4:
								mess = message.replace('рассылка ', '')
								mass_ids = vk_session.get_all_open_id()
								vk_session.mailing(mess, mass_ids)
								msg(id, 'Рассылка успешна.')
						elif 'kick ' in message or 'кик ' in message or 'кикнуть ' in message:
							try:  
								from helpmethod.readdb import get_as
								admin_status = get_as(user_id)
								if int(admin_status) > 2 or int(admin_status) == 2:
									if 'kick ' in message:
										id_u = message.replace('kick ', '')
									if 'кик ' in message:
										id_u = message.replace('кик ', '')
									if 'кикнуть ' in message:
										id_u = message.replace('кикнуть ', '')
									if "@" in id_u:
										id_uu = id_u.split("|")[0]
										id_u = id_uu.replace('[', '')
										if "id" in id_u:
											id_u = id_u.replace("id", "")
									if 'https://vk.com/' in id_u:
										id_u = id_u.replace('https://vk.com/', '')
										if 'id' in id_user:
											id_u = id_u.replace('id', '')
									Thread(target=kick, args=(id, id_u)).start()
									msg(id, '[id' + str(user_id) + '|Пользователь] успешно исключен.')
							except vk_api.exceptions.ApiError:
								msg(id, 'Данного пользователя невозможно исключить.')
								continue
						elif message == 'kick' or message == 'кик' or message == 'кикнуть':
							from helpmethod.check_answer import reply_check
							user = reply_check(give, event)
							try:
								from helpmethod.readdb import get_as
								admin_status = get_as(user_id)
								if int(admin_status) > 2 or int(admin_status) == 2:
									if 'kick' in message:
										id_u = message.replace('kick ', '')
									if 'кик' in message:
										id_u = message.replace('кик ', '')
									if 'кикнуть' in message:
										id_u = message.replace('кикнуть ', '')
									if 'https://vk.com/' in id_u:
										id_u = id_u.replace('https://vk.com/', '')
										if 'id' in id_user:
											id_u = id_u.replace('id', '')
									Thread(target=kick, args=(id, id_u)).start()
									msg(id, '[id' + str(user_id) + '|Пользователь] успешно исключен.')
							except vk_api.exceptions.ApiError:
								msg(id, 'Данного пользователя невозможно исключить.')
								continue
						elif message == 'рабы':
							msg(id, 'Команды:\n1. Рабы доходы - все бизнесы и их доходы\n2. управление рабами - управление рабами\n3. купить раба - купить следующего раба')
						elif message == 'рабы доходы' or message == 'Рабы доходы':
							from cmds.busines import costs
							costs(id)
						elif message == 'управление рабами' or message == 'Управление рабами':
							from cmds.busines import menu
							menu(id, user_id)
						elif message == 'Купить раба' or message == 'купить раба':
							from cmds.busines import buy
							buy(id, user_id)



						
import time
import requests
					
try:
    main()
except requests.exceptions.ReadTimeout:
    print("\n Переподключение к серверам ВК \n")
    time.sleep(40)
