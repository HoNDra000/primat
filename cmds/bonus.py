import datetime
import humanize
import random
import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def bonus(id, user_id):
	from helpmethod.readdb import get_bonus
	last_bonus = get_bonus(user_id)
	NowDate = datetime.datetime.now()
	NowTime = NowDate.strftime("%H")
	if int(NowTime) == int(last_bonus):
		msg(id, 'бонус можно получать 1 раз в час. не выёбывайся, раньше ты его не получишь.')
	else:
		from helpmethod.readdb import get_koef
		koef = int(get_koef(user_id))
		x_def = random.randint(1, 100)
		if id == 16:
			if x_def < 50:
				x = 4
				money = 500000 * x
				money *= koef
				from helpmethod.readdb import get_balance
				old_money = get_balance(user_id)
				result = int(old_money) + int(money)

				

				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()
				


				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET bonus = ? WHERE id = ?""", (NowTime, user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, 'ты получил ежечасный бонус: ' + humanize.intcomma(str(money)))
			elif x_def > 50:
				x = random.randint(20, 56)
				money = 250000 * x
				money *= koef
				from helpmethod.readdb import get_balance
				old_money = get_balance(user_id)
				result = int(old_money) + int(money)
				from helpmethod.readdb import get_koef
				koef = int(get_koef(user_id))

				result *= koef
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET bonus = ? WHERE id = ?""", (NowTime, user_id))
				sqlite_connection.commit()
				cur.close()
				msg(id, 'ты получил ежечасный бонус: ' + humanize.intcomma(str(money)))
			else:
				msg(id, 'error: N_BON001')
		else:
			if x_def < 50:
				x = 2
				money = 500000 * x
				money *= koef
				from helpmethod.readdb import get_balance
				old_money = get_balance(user_id)
				result = int(old_money) + int(money)

				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()
				


				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET bonus = ? WHERE id = ?""", (NowTime, user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, 'ты получил ежечасный бонус: ' + humanize.intcomma(str(money)))
			elif x_def > 50:
				x = random.randint(10, 28)
				money = 250000 * x
				money *= koef
				from helpmethod.readdb import get_balance
				old_money = get_balance(user_id)
				result = int(old_money) + int(money)
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET bonus = ? WHERE id = ?""", (NowTime, user_id))
				sqlite_connection.commit()
				cur.close()
				msg(id, 'ты получил ежечасный бонус: ' + humanize.intcomma(str(money)))
			else:
				msg(id, 'error: N_BON001')