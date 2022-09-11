import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from threading import Thread
import humanize
from LiteVkApi import Client

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

vk_session = Client.login(token, 210219643)

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def send(id, text, keyboard):
	bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})
def is_num(string):
	if string.isdigit():
		return True
	else:
		try:
			float(string)
			return True
		except ValueError:
			return False
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
def create_VkKeyboard(message):
    keyboard = VkKeyboard(one_time=True)
 
    if message == 'начать' or message == 'вернуться' or message == 'кто еблан?':
        keyboard.add_button('Моя инфа', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Баланс', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Помощь', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Прокачать уровень', color=VkKeyboardColor.POSITIVE)
        keyboard = keyboard.get_keyboard()
        return keyboard
    elif message == 'прокачать уровень' or message == 'levelup':
        keyboard.add_button('Прокачать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вернуться', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('Перерождение/ребитх', color=VkKeyboardColor.NEGATIVE)
        keyboard = keyboard.get_keyboard()
        return keyboard
    else:
        return None

from helpmethod.test import *
from helpmethod.readdb import *
from start_logger import *
from casino.avtomat import *
from helpmethod.check_answer import *
from admincmds.rebukewarns import *
from admincmds.p_task import *
from cmds.bonus import *
from cmds.ya import *
from cmds.setnick import *
from cmds.balance import *
from casino.roulete import *
from casino.dice import *
from cmds.admins import *
from cmds.translate_money import *
from admincmds.all_admins import *
from start_connector import *
from admincmds.msg import *
from admincmds.p_chat import *
from admincmds.staffinfo import *
from admincmds.dubl import *
from cmds.admins import *
from admincmds.reset_bal import *
from admincmds.resbal import *
from admincmds.sb import *
from admincmds.balance import *
from admincmds.sub import *
from admincmds.statset import *
from cmds.opencase import *
from admincmds.unban import *
from admincmds.you import *
from cmds.top import *
from admincmds.case import *
from admincmds.mailling import *
from admincmds.ban import *
from cmds.busines import *
from cmds.open_all import *
from helpmethod.levels import *


Thread(target=start_bis, args=()).start()
Thread(target=main_logger, args=()).start()

def main():
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_chat:
				message = str(event.object.message['text'].lower())
				user_id = event.obj['message']['from_id']
				id = event.chat_id
				data = bh.method("users.get", {"user_ids": user_id})
				lvl = get_lvl(user_id)
				from helpmethod.readdb import is_ban
				ban_stat = is_ban(user_id)

				db = sqlite3.connect('databases\MDB.db', timeout=20)
				cursor = db.cursor()

				met = """SELECT * FROM users WHERE id = ?"""
				cursor.execute(met, (user_id,))
				if cursor.fetchone() is None:
					first_name = get_name(user_id)
					cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(user_id), str(first_name), 0, 1000000, 0, 0, 0, 0, 0, 0, '📙', 0, 1, 0, 0, 0, 0, 0, 0, 0))
					db.commit()
					db.close()
				else:
					db.close()

				if ban_stat == 1:
					if user_id > 0:
						continue
				else:
					if user_id > 0:

						if message == 'автомат все' or message == 'автомат всё':
							if lvl > 7 or lvl == 7:
								try:

									balik = get_balance(user_id)
									Thread(target=avtomat, args=(id, user_id, 1, balik)).start()
									msg(47, "автомат все\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "автомат все\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'кто еблан?':
							msg(id, 'еблан -> [id0|тык]')
						elif message == '+пред' or message == '+warn' or message == '+rebuke' or message == '+выговор':
							admin_status = get_as(user_id)
							if int(admin_status) == 4 or int(admin_status) > 4:
								if message == '+warn' or message == '+пред':
									try:
										user = reply_check(give, event)
										Thread(target=give_warn, args=(user,)).start()
										msg(id, '✅[id' + str(user) + '|Администратору] было выдано предупреждение')
										msg(47, "+warn\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
									except:
										msg(47, "+warn\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
								else:
									try:
										user = reply_check(give, event)
										Thread(target=give_rebuke, args=(user,)).start()
										msg(id, '✅[id' + str(user) + '|Администратору] был выдан выговор')
										msg(47, "+rebuke\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
									except:
										msg(47, "+rebuke\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == '+task':
							try:
								user = reply_check(give, event)
								Thread(target=plus_task, args=(user_id, id, user,)).start()
								msg(47, "+task\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "+task\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'рулетка хелп':
							if id != 7:
								if lvl > 5 or lvl == 5:
									try:
										
										msg(id, 'Доступные форматы:\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0, Красное, Зеро, Чёрное.')
										msg(47, "roulete help\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
									except:
										msg(47, "roulete help\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'я' or message == "Я":
							try:
								Thread(target=ya, args=(id, user_id,)).start()
								msg(47, "ya\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "ya\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'автомат ' in message:
							if lvl > 7 or lvl == 7:
								try:
									stavka = message.replace('автомат ', '')
									num_ = is_num(stavka)
									if num_ == False:
										msg(id, 'ставка должна быть числом сука')
									elif num_ == True:
										tmp = int(stavka)
										Thread(target=avtomat, args=(id, user_id, 0, tmp)).start()
									else:
										msg(id, 'ERROR: Critical error avt_a01')
									msg(47, "автомат\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "автомат\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'bonus' or message == 'бонус':
							try:
								if lvl > 1 or lvl == 1:
									Thread(target=bonus, args=(id, user_id,)).start()
									msg(47, "бонус\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "бонус\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'setnick ' in message or 'сетник ' in message:
							try:
								if lvl > 3 or lvl == 3:
									Thread(target=setnick, args=(id, user_id, message)).start()
									msg(47, "setnick\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "setnick\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'balance' or message == 'bal' or message == 'balik' or message == 'бал' or message == 'балик' or message == 'баланс':
							try:
								ggg = balance(user_id)
								msg(id, '💰[id' + str(user_id) + '|На твоём] балансе: ' + humanize.intcomma(ggg) + '$')
								msg(47, "bal\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "bal\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'рулетка ' in message:
							if id != 7:
								if lvl > 5 or lvl == 5:
									try:
										Thread(target=rouleteStart, args=(id, user_id, message)).start()
										msg(47, "roulete\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
									except:
										msg(47, "roulete\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'dice ' in message or 'дайс' in message or 'дайсы' in message:
							if id != 7:
								try:
									Thread(target=start_dice, args=(id, user_id, message)).start()
									msg(47, "dice\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "dice\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'settex ' in message:
							admin_status = get_as(user_id)
							if int(admin_status) == 1 or int(admin_status) > 1:
								try:
									setting = message.replace('settex ', '')
									if setting == '📕' or setting == '📙' or setting == '📗':
										Thread(target=settexstatus, args=(user_id, id, setting)).start()
									else:
										msg(id, 'ERROR: Статус может быть только: 📗, 📙, 📕')
									msg(47, "settex\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "settex\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'help' or message == 'команды':
							try:
								nick = get_nick(user_id)
								msg(id,
		'🛡[id' + str(user_id) + '|' + str(nick) + '] вот команды бота:\n\n' + '''1 — Я - твой профиль.
		2 — перевести [сумма] [пользователь] - перевести пользователю деньги
		3 — Баланс - Узнать свой баланс.
		4 — Сетник [ник] - Установить себе ник.''')
								msg(47, "help\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "help\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'перевод ' in message or 'перевести ' in message:
							if lvl > 1 or lvl == 1:
								try:
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
										Thread(target=perevod, args=(message, id, user_id, user, ammout,)).start()
									msg(47, "perevod\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "perevod\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'admin list' or message == 'админ лист':
							try:
								Thread(target=admins_cycle, args=(id,)).start()
								msg(47, "admin_list\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "admin_list\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == '.connect admin bot' or message == '.connect dev bot' or message == '.connect' or message == '.reconnect':
							try:
								Thread(target=main_connector, args=(message, id, user_id, event)).start() 
								msg(47, "connector\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "connector\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'сообщение ' in message:
							try:
								Thread(target=mess_ls, args=(id, user_id, message)).start()
								msg(47, "mess\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "mess\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == '+chat':
							try:
								Thread(target=plus_chat, args=(id, user_id)).start()
								msg(47, "+chat\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "+chat\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'staff-info':
							try:
								Thread(target=staff_info, args=(user_id, id,)).start()
								msg(47, "staff-info\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "staff-info\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'you staff-info' or message == 'you si':
							try:
								msg_inf = event.obj['message']
								if 'reply_message' in msg_inf:
									user = reply_check(give, event)
									Thread(target=you_staff_info, args=(user_id, user, id,)).start()
								else:
									msg(id, 'Ты должен ответить на сообщение человека, которого staff-info хочешь увидить.')
								msg(47, "you_si\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "you_si\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'дубль ' in message:
							try:
								Thread(target=dubl, args=(id, user_id, message)).start()
								msg(47, "дубль\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "дубль\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'админы' or message == 'Админы':
							try:
								Thread(target=admin_cycle, args=(id,)).start()
								msg(47, "admins\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "admins\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'reset_bal' in message:
							try:
								Thread(target=reset_bal, args=(id, user_id, message)).start()
								msg(47, "reset_bal\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "reset_bal\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'resbal':
							try:
								Thread(target=resbal, args=(id, user_id)).start()
								msg(47, "resbal\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "resbal\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'set balance ' in message or 'sb ' in message:
							try:
								if 'set balance ' in message:
									balance = message.replace('set balance ', '')
									Thread(target=setbalance_check, args=(id, user_id, balance)).start()
								elif 'sb ' in message:
									balance = message.replace('sb ', '')
									Thread(target=setbalance_check, args=(id, user_id, balance)).start()
								msg(47, "sb\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "sb\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'balance ' in message:
							try:
								Thread(target=check_bal, args=(user_id, id, message)).start()
								msg(47, "check balance\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "check balance\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'sub ' in message or 'set user balance ' in message:
							try:
								if 'sub ' in message:
									uid = message.replace('sub ', '')
									id_u = uid.split(' ')[0]
									if "@" in id_u:
										id_uu = id_u.split("|")[0]
										id_u = id_uu.replace('[', '')
										if "id" in id_u:
											id_u = id_u.replace("id", "")
									bal = uid.split(' ')[1]
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
									Thread(target=sub, args=(id, user_id, id_u, bal)).start()
								msg(47, "sub\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "sub\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'setstat ' in message:
							try:
								Thread(target=set_stat, args=(id, user_id, message)).start()
								msg(47, "setstat\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "setstat\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'case' or message == 'кейс' or message == 'кейсик':
							try:
								win = open_case(id, user_id)
								if win == 0:
									msg(id, 'У тя нету кейсиков')
								elif win == 1:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n100,000,000$ 💸💸💸')
								elif win == 2:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n5,000,000$ 💸💸💸')
								elif win == 3:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n25,000,000$ 💸💸💸')
								elif win == 4:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n100,000,000$ 💸💸💸')
								elif win == 5:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n50,000,000$ 💸💸💸')
								elif win == 6:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n10,000,000$ 💸💸💸')
								elif win == 7:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n1,500,000,000$ 💸💸💸')
								elif win == 8:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n1,000,000$ 💸💸💸')
								elif win == 9:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n100$ 💸💸💸')
								elif win == 10:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n1$ 💸💸💸')
								elif win == 11:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n1💎')
								elif win == 12:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n5💎')
								elif win == 13:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n10💎')
								elif win == 14:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n2💎')
								elif win == 15:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n15💎')
								elif win == 16:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n17💎')
								elif win == 17:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n4💎')
								elif win == 18:
									msg(id, '[id' + str(user_id) + '|Ты] получил: \n20💎')
								elif win == 19:
									msg(id, '💲[id' + str(user_id) + '|Тебе] выпала скидка на донат💲 \n{skidka1}')
								elif win == 20:
									msg(id, '💲[id' + str(user_id) + '|Тебе] выпала скидка на донат💲 \n{skidka2}')
								else:
									msg(id, 'error')
								msg(47, "open_case\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "open_case\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'unban ' in message or 'разбан ' in message:
							try:
								if 'unban ' in message:
									user = message.replace('unban ', '')
								elif 'разбан ' in message:
									user = message.replace('разбан ', '')
								if "@" in user:
									userr = user.split("|")[0]
									user = userr.replace('[', '')
									if "id" in user:
										user = user.replace("id", "")
								Thread(target=unban, args=(id, user_id, user)).start()
								msg(47, "unban\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "unban\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'разбан' or message == 'unban':
							try:
								user = reply_check(give, event)
								Thread(target=unban, args=(id, user_id, user)).start()
								msg(47, "unban\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "unban\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'lban ' in message or 'лбан ' in message:
							try:
								if id == 12:
									user = reply_check_logger_user(give, event)
									chat = reply_check_logger_chat(give, event)
									if user == False:
										msg(id, 'ОШИБКА! Пользователь или является ботом или вы не ответили на сообщение логгера.')
									else:
										if 'lban ' in message:
											realson = message.replace('lban ', '')
											Thread(target=ban1, args=(id, user_id, user, realson, 'logger', chat)).start()	
										elif 'лбан ' in message:
											realson = message.replace('лбан ', '')
											Thread(target=ban1, args=(id, user_id, user, realson, 'logger', chat)).start()							
								else:
									msg(id, 'Данная команда доступна только в логгере.')
								msg(47, "lban\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "lban\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'ban ' in message or 'бан ' in message:
							try:
								if id != 12:
									user = reply_check(give, event)
									if 'ban ' in message:
										realson = message.replace('ban ', '')
										Thread(target=ban1, args=(id, user_id, user, realson, None, None)).start()
									elif 'бан ' in message:
										realson = message.replace('бан ', '')
										Thread(target=ban1, args=(id, user_id, user, realson, None, None)).start()
								else:
									msg(12, 'команда не доступна в логгере')
								msg(47, "ban\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "ban\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'твоя инфа ' in message:
							try:
								Thread(target=you, args=(user_id, id, message)).start()
								msg(47, "you info\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "you info\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'chat_id':
							try:
								admin_status = get_as(user_id)
								if int(admin_status) > 5 or int(admin_status) == 5:
									msg(id, id)
								msg(47, "chat_id\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "chat_id\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'твоя инфа':
							try:
								user = reply_check(give, event)
								Thread(target=you1, args=(user_id, id, user)).start()
								msg(47, "you info\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "you info\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'топ':
							try:
								tp = top()
								msg(id, 'топ 5 по ребитхам: \n' + tp)
								msg(47, "top\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "top\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'givecase':
							try:
								user = reply_check(give, event)
								a = give_case(user_id, id, user)
								if a == True:
									msg(id, 'Кейс был выдан [id' + str(user) + '|ему]')

									nick = get_nick(user_id)
									u_nick = get_nick(user)

									msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду givecase на пользователе [id' + str(id_u) + '|' + str(u_nick) + ']\n#givecase')
								else:
									msg(id, 'error')
								msg(47, "givecase\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "givecase\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif 'рассылка ' in message:
							admin_status = get_as(user_id)
							if int(admin_status) > 4 or int(admin_status) == 4:
								try:
									text = message.replace('рассылка ', '')
									mass_ids = vk_session.get_all_open_id()
									vk_session.mailing(text, mass_ids)
									Thread(target=mail, args=(id, text)).start()
									msg(47, "mailling\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
								except:
									msg(47, "mailling\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'рабы':
							try:
								msg(id, 'Команды:\n💰Рабы доходы - все бизнесы и их доходы💰\n📊Управление рабами - управление\n🛒Купить раба - купить еще рабов')
								msg(47, "rabs\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "rabs\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'рабы доходы' or message == 'Рабы доходы':
							try:
								Thread(target=costs, args=(id)).start()
								msg(47, "rabs list\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "rabs list\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'управление рабами' or message == 'Управление рабами':
							try:
								Thread(target=menu, args=(id, user_id)).start()
								msg(47, "rabs manage\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "rabs manage\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'Купить раба' or message == 'купить раба':
							try:
								Thread(target=buy, args=(id, user_id)).start()
								msg(47, "rabs buy\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "rabs buy\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
						elif message == 'кейсик всё' or message == 'кейсик все':
							try:
								Thread(target=start_allcase, args=(user_id, id)).start()
								msg(47, "case all\nUSER: @id" + str(user_id) + '\nSTATUS: SUCCESS\n#' + str(user_id))
							except:
								msg(47, "case all\nUSER: @id" + str(user_id) + '\nSTATUS: ERROR\nMESSAGE_TEXT: ' + message + '\n#' + str(user_id) + '\n@online')
			elif event.from_user:
				message = str(event.object.message['text'].lower())
				id = event.obj['message']['from_id']

				from helpmethod.readdb import get_nick
				nick = get_nick(id)

				data = bh.method("users.get", {"user_ids": id})
				first_name = get_name(id)

				from helpmethod.readdb import is_ban
				ban = is_ban(id)

				if ban == 1:
					if id > 0:
						send(id, 'Ты не можешь использовать команды((.\nТы был забанен одним из модераторов.', None)
				else:
					if id > 0:
						db = sqlite3.connect('databases\MDB.db', timeout=20)
						cursor = db.cursor()

						met = """SELECT * FROM users WHERE id = ?"""
						cursor.execute(met, (id,))
						if cursor.fetchone() is None:
							cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(id), str(first_name), 0, 1000000, 0, 0, 0, 0, 0, 0, '📙', 0, 1, 0, 0, 0, 0, 0, 0, 0))
							db.commit()
							db.close()
						else:
							db.close()

						if message == 'начать':
							send(id, 'Чтобы начать играть в нашего бота, используй команду "я" и команду "help".', create_VkKeyboard(message))
						elif message == 'кто еблан?':
							send(id, 'еблан -> [id0|тык]', create_VkKeyboard(message))
						elif message == 'я' or message == 'моя инфа':
							Thread(target=ya, args=(id, id,)).start()
						elif message == 'help' or message == 'помощь' or message == 'хелп':
							send(id,
	'🛡[id' + str(id) + '|' + str(nick) + '] вот команды бота:\n\n' + '''1 — Я - твой профиль.
	2 — перевести [сумма] [пользователь] - перевести пользователю деньги
	3 — Баланс - Узнать свой баланс.
	4 — Сетник [ник] - Установить себе ник.''', create_VkKeyboard('начать'))
						elif message == 'levelup' or message == 'прокачать уровень':
							send(id, menu_levelup(id), create_VkKeyboard(message))
						elif message == 'вернуться':
							send(id, 'Ты вернулся в главное меню.', create_VkKeyboard(message))
						elif message == 'баланс':
							ggg = get_balance(id)
							send(id, '💰[id' + str(id) + '|На твоём] балансе: ' + humanize.intcomma(ggg) + '$', create_VkKeyboard('вернуться'))
						elif message == 'прокачать':
							mess = level_up(id)
							send(id, mess, create_VkKeyboard('levelup'))
						elif message == 'rebirth' or message == 'ребитх' or message == 'перерождение' or message == 'перерождение/ребитх':
							mess = rebirth(id)
							send(id, mess, create_VkKeyboard('levelup'))
						elif message == 'тест':
							send(id, '1', None)



import time
import requests
					
try:
	try:
		try:
			main()
		except requests.exceptions.ReadTimeout:
			print('\n Переподключение к серверам ВК x2 \n')
			time.sleep(30)
			main()
	except requests.exceptions.ReadTimeout:
		print('\n Переподключение к серверам ВК x2 \n')
		time.sleep(20)
		main()
except requests.exceptions.ReadTimeout:
	print("\n Переподключение к серверам ВК \n")
	time.sleep(10)
	main()
