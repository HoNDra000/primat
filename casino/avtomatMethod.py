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

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def start_method(stavka, id, mnoj, text, user_id, balance):
	result = int(stavka) * int(mnoj)
	new_bal = balance + int(result)

	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (new_bal, user_id))
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

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, 'Ты проебал(((\nТвой баланс, лошок: ' + humanize.intcomma(str(result)))
				print('avtomat.LOSE: ' + str(user_id) + ', ' + str(result))
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