import sqlite3
import humanize
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def k_system(message):
	text = message
	stavka = text.replace('автомат ', '')
	if "k" in text or 'к' in text:
		stavka /= 1000
	if "kk" in text or 'кк' in text:
		stavka /= 1000000
	if "kkk" in text or 'ккк' in text:
		stavka /= 1000000000
	if "kkkk" in text or 'кккк' in text:
		stavka /= 1000000000000
	if "kkkkk" in text or 'ккккк' in text:
		stavka /= 1000000000000000
	if "kkkkkk" in text or 'кккккк' in text:
		stavka /= 1000000000000000000
	if "kkkkkkk" in text or 'ккккккк' in text:
		stavka /= 1000000000000000000000
	if "kkkkkkkk" in text or 'кккккккк' in text:
		stavka /= 1000000000000000000000000
	if "kkkkkkkkk" in text or 'ккккккккк' in text:
		stavka /= 1000000000000000000000000000
	if "kkkkkkkkkk" in text or 'кккккккккк' in text:
		stavka /= 1000000000000000000000000000000
	if "kkkkkkkkkkk" in text or 'ккккккккккк' in text:
		stavka /= 1000000000000000000000000000000000
	if "kkkkkkkkkkkk" in text or 'кккккккккккк' in text:
		stavka /= 1000000000000000000000000000000000000
	if "kkkkkkkkkkkkk" in text or 'ккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000
	if "kkkkkkkkkkkkkk" in text or 'кккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkk" in text or 'ккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkk" in text or 'ккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkk" in text or 'кккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkk" in text or 'ккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkk" in text or 'кккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkkk" in text or 'ккккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkkkk" in text or 'кккккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkkkkk" in text or 'ккккккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkkkkkk" in text or 'кккккккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000000000000000
	if "kkkkkkkkkkkkkkkkkkkkkkkk" in text or 'ккккккккккккккккккккккккк' in text:
		stavka /= 100000000000000000000000000000000000000000000000000000000000000000000000

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def start_method(stavka, id, mnoj, text, user_id, balance):
	if id == 16:
		mnojj = mnoj * 2
		result = int(stavka) * int(mnojj)

		from helpmethod.readdb import get_koef
		koef = int(get_koef(user_id))

		result *= koef
		
		new_bal = balance + int(result)

		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()

		cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(new_bal), user_id))
		sqlite_connection.commit()
		cur.close()

		msg(id, text + '\nТы выйграл: ' + humanize.intcomma(str(result)))
	else:
		result = int(stavka) * int(mnoj)

		from helpmethod.readdb import get_koef
		koef = int(get_koef(user_id))

		result *= koef

		new_bal = balance + int(result)

		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()

		cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(new_bal), user_id))
		sqlite_connection.commit()
		cur.close()

		msg(id, text + '\nТы выйграл: ' + humanize.intcomma(str(result)))
		print('avtomat.WIN: ' + str(user_id) + ', ' + str(result))
def start(id, stavka, user_id, balance):
	if stavka == 0:
		msg(id, 'отсоси мой член, 0 ты не поставишь.')
	elif stavka < 0:
		msg(id, 'давай не отрицательную стаку? я понимаю что ты гений, но всё-же')
	else:
		if stavka < balance or stavka == balance:
			a = random.randint(1, 3)
			b = random.randint(1, 192)
			if a == 1 or a == 3:
				
				result = int(balance) - int(stavka)

				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, 'Ты проебал(((\nТвой баланс, лошок: ' + humanize.intcomma(str(result)))
			elif a == 2:
				if (b <101):
					start_method(stavka, id, 2, 'Ты выйграл', user_id, balance)
				elif (b >150) and (b <176):
					start_method(stavka, id, 10, 'Ты ограбил банк(', user_id, balance)
				elif (b > 175) and (b < 186):
					start_method(stavka, id, 25, 'Ты оставил сотрудников без зарплаты((', user_id, balance)
				elif (b > 185) and (b < 191):
					start_method(stavka, id, 50, 'Ты оставил толстых дядек без зарплаты(((', user_id, balance)
				elif (b >190):
					start_method(stavka, id, 100, 'Ты обонкротил казино(((((((', user_id, balance)
		elif stavka > balance:
			msg(id, 'иди нахуй, у тебя деняк нету\nфууууу бомжара')