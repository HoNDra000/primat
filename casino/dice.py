import humanize
import random
import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def is_num(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
            
def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def dice_Method(stavka, id, dice, user_id):
	from helpmethod.readdb import get_balance
	bal = get_balance(user_id)
	from helpmethod.readdb import get_nick
	nick = get_nick(user_id)
	win = int(stavka) * 2
	result = int(bal) + int(win)
	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
	sqlite_connection.commit()
	cur.close()
	msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл!\nТвой баланс: ' + humanize.intcomma(str(result)))
def dice(id, stavka, user_id):
	from helpmethod.readdb import get_balance
	balik = get_balance(user_id)
	from helpmethod.readdb import get_nick
	nick = get_nick(user_id)
	if int(stavka) < int(balik) or int(stavka) == int(balik):
		if stavka == '0':
			msg(id, 'иди нахуй, 0 ты не поставишь.')
		else:
			dice = random.randint(1, 101)
			if dice == 25 or dice == 26 or dice == 27 or dice == 28 or dice == 29 or dice == 30 or dice == 71 or dice == 72 or dice == 73 or dice == 74 or dice == 75:
				dice_Method(stavka, id, dice, user_id)
			elif dice == 31 or dice == 32 or dice == 33 or dice == 34 or dice == 35 or dice == 36 or dice == 37 or dice == 38 or dice == 39 or dice == 40:
				dice_Method(stavka, id, dice, user_id)
			elif dice == 41 or dice == 42 or dice == 43 or dice == 44 or dice == 45 or dice == 46 or dice == 47 or dice == 48 or dice == 49 or dice == 50:
				dice_Method(stavka, id, dice, user_id)
			elif dice == 51 or dice == 52 or dice == 53 or dice == 54 or dice == 55 or dice == 56 or dice == 57 or dice == 58 or dice == 59 or dice == 60:
				dice_Method(stavka, id, dice, user_id)
			elif dice == 61 or dice == 62 or dice == 63 or dice == 64 or dice == 65 or dice == 66 or dice == 67 or dice == 68 or dice == 69 or dice == 70:
				dice_Method(stavka, id, dice, user_id)
			else:
				from helpmethod.readdb import get_balance
				bal = get_balance(user_id)
				result = int(bal) - int(stavka)
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()
				msg(id, '❌[id' + str(user_id) + "|" + str(nick) + '] ты проиграл:\nтвой баланс: ' + str(result))
	else:
		msg(id, 'иди нахуй, у тебя деняк нету\nфууууу бомжара')
def start_dice(id, user_id, message):
	if 'dice ' in message:
		stavka = message.replace("dice ", "")
		num_ = is_num(stavka)
		if num_ == False:
			msg(id, 'ставка должна быть числом сука')
		elif num_ == True:
			tmp = int(stavka)
			dice(id, stavka, user_id)
		else:
			msg(id, 'ERROR: Critical error dice_a01')
	elif 'дайсы ' in message:
		stavka = message.replace("дайсы ", "")
		num_ = is_num(stavka)
		if num_ == False:
			msg(id, 'ставка должна быть числом сука')
		elif num_ == True:
			tmp = int(stavka)
			dice(id, stavka, user_id)
		else:
			msg(id, 'ERROR: Critical error dice_a01')
	elif 'дайс ' in message:
		stavka = message.replace("дайс ", "")
		num_ = is_num(stavka)
		if num_ == False:
			msg(id, 'ставка должна быть числом сука')
		elif num_ == True:
			tmp = int(stavka)
			dice(id, stavka, user_id)
		else:
			msg(id, 'ERROR: Critical error dice_a01')