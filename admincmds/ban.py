import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from threading import Thread

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text, keyboard):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})
def create_keyboard(num):
	keyboard = VkKeyboard(inline=True)
	if num == 1:
		keyboard.add_callback_button('15м', color=VkKeyboardColor.POSITIVE, payload={"type": "15M", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('30м', color=VkKeyboardColor.POSITIVE, payload={"type": "30M", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('1ч', color=VkKeyboardColor.POSITIVE, payload={"type": "1H", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('4ч', color=VkKeyboardColor.POSITIVE, payload={"type": "4H", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('10ч', color=VkKeyboardColor.SECONDARY, payload={"type": "10H", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('1д', color=VkKeyboardColor.SECONDARY, payload={"type": "1D", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('7д', color=VkKeyboardColor.SECONDARY, payload={"type": "7D", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('1мес', color=VkKeyboardColor.SECONDARY, payload={"type": "1ME", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('3мес', color=VkKeyboardColor.NEGATIVE, payload={"type": "3ME", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('НАВСЕГДА', color=VkKeyboardColor.NEGATIVE, payload={"type": "GLOB", "text": "Это исчезающее сообщение"})

	return keyboard.get_keyboard()
def sleep(n):
    import time
    a = 0
    while int(a) < int(n):
        time.sleep(5)
        a += 5

def d(user_id, nick, user, u_nick, realson, ban_time, ban_):
	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	from helpmethod.readdb import get_bans
	old = get_bans(user_id)
	new = int(old) + 1

	cur.execute(f"""UPDATE users SET bans = ? WHERE id = ?""", (new, user_id))
	sqlite_connection.commit()
	cur.close()

	import time
	time.sleep(2)

	Thread(target=setbantime, args=(user, ban_time)).start()
	msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду ban на пользователе [id' + str(user) + '|' + str(u_nick) + '] на ' + ban_ + ' по причине ' + realson + '\n#ban', None)

def find_ban_time(user_id, realson, id, banner_id):
	from helpmethod.readdb import get_forban, get_as
	warns = get_forban(user_id)
	if realson == '1.1':
		default_ban_time = 604800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.2':
		default_ban_time = 3600
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.2.1':
		default_ban_time = 604800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.2.2':
		default_ban_time = 2678400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.2.3':
		default_ban_time = 7776000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.3':
		default_ban_time = 36000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.3.1':
		default_ban_time = 86400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '1.4':
		default_ban_time = 2678400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.1':
		default_ban_time = 1800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.2':
		default_ban_time = 1800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.3':
		default_ban_time = 36000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.4':
		default_ban_time = 14400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.5':
		default_ban_time = 86400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.6':
		default_ban_time = 14400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.7':
		default_ban_time = 900
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.8':
		default_ban_time = 36000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.9':
		default_ban_time = 36000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.9.1':
		default_ban_time = 604800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.9.2':
		default_ban_time = 2678400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.9.3':
		default_ban_time = 7776000
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.10':
		default_ban_time = 14400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.11':
		default_ban_time = 14400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '2.12':
		default_ban_time = 14400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '3.1':
		default_ban_time = 'kk'
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '3.2':
		default_ban_time = 604800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '3.3':
		default_ban_time = 86400
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '3.4':
		default_ban_time = 'kk'
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	elif realson == '3.5':
		default_ban_time = 604800
		Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
		if default_ban_time == 'kk':
			ret = 'навсегда'
			return ret
		else:
			ret = help_ban(warns, default_ban_time)
			return ret
	else:
		admin_status = get_as(banner_id)
		if admin_status == 7:
			default_ban_time = 'kk'
			Thread(target=banning, args=(user_id, realson, default_ban_time, warns)).start()
			if default_ban_time == 'kk':
				ret = 'навсегда'
				return ret
			else:
				ret = help_ban(warns, default_ban_time)
				return ret
		else:
			msg(id, 'Данной причины не существует.', None)
			return False

def full_time(sec):
	if sec == 'навсегда':
		return sec
	else:
		import datetime
		a = str(datetime.timedelta(seconds = sec))
		return 'на ' + a

def help_ban(warns, time):
	warns = int(warns) + 1

	ban_time = int(time) * warns
	return ban_time

def banning(user_id, realson, time, warns):
	if time == 'kk':
		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()
		cur.execute(f"""UPDATE users SET ban_state = ? WHERE id = ?""", (1, user_id))
		sqlite_connection.commit()
		cur.close()
	else:

		ban_time = help_ban(warns, time)

		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()
		cur.execute(f"""UPDATE users SET ban_state = ? WHERE id = ?""", (1, user_id))
		sqlite_connection.commit()
		cur.close()

		sleep(ban_time)

		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()
		cur.execute(f"""UPDATE users SET ban_state = ? WHERE id = ?""", (0, user_id))
		sqlite_connection.commit()
		cur.close()

		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)

		msg(32, '[id' + str(user_id) + '|' + str(nick) + '] разбанен по истечению времени.',None)

def ban1(id, user_id, user, realson, d, ban_chat):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 2 or int(admin_status) == 2:
		from helpmethod.readdb import is_ban
		ban_status = is_ban(user)
		if ban_status == 1:
			msg(id, '✅[id' + str(user) + '|Пользователь] уже забанен.', None)
		elif ban_status != 1:
			u_as = get_as(user)
			if u_as > admin_status or u_as == admin_status:
				msg(id, 'Ты не можешь забанить людей, которые твоего статуса или больше твоего статуса', None)
			else:
				ret = find_ban_time(user, realson, id, user_id)
				if ret != False:
					ff = full_time(ret)
					from helpmethod.readdb import get_nick, get_forban, get_bans
					u_nick = get_nick(user)
					msg(id, '✅[id' + str(user) + '|' + str(u_nick) + '] был забанен ' + ff  + ' по причине ' + str(realson), None)

					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					a = get_forban(user) + 1

					cur.execute(f"""UPDATE users SET forban = ? WHERE id = ?""", (a, user))

					sqlite_connection.commit()
					cur.close()

					new = int(get_bans(user_id)) + 1

					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()
					cur.execute(f"""UPDATE users SET bans = ? WHERE id = ?""", (new, user_id))
					sqlite_connection.commit()
					cur.close()

					nick = get_nick(user_id)

					msg(32, '[id' + str(user_id) + '|' + str(nick) + '] забанил пользователя [id' + str(user) + '|' + str(u_nick) + '] на ' + ff + ' по причине ' + str(realson), None)

					if d == 'logger':
						msg(ban_chat, '[id' + str(user) + '|' + str(u_nick) + '] был забанен ' + ff  + ' по причине ' + str(realson) + '\nУзнать расшифровку кода бана: https://vk.com/@bot_pr1mat-rules', None)

				

								

								