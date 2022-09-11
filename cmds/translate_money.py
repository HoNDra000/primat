import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import humanize

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

vk = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll_Ls = VkLongPoll(vk)

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

def perevod(message, id, user_id, user, ammout):
	if 'перевод ' in message:
		from helpmethod.readdb import get_balance
		bal = get_balance(user_id)
		if int(ammout) > int(bal):
			msg(id, 'еблан? у тя баланса не хватает')
		else:
			new_balance = int(bal) - int(ammout)

			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (new_balance, user_id))
			sqlite_connection.commit()
			cur.close()

			from helpmethod.readdb import get_balance
			ball = get_balance(user)
			new_bal = int(ball) + int(ammout)
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (new_bal, user))
			sqlite_connection.commit()
			cur.close()

			msg(id, '✅[id' + str(user_id) + '|Ты] перевёл [id' + str(user) + '|пользователю] ' +  humanize.intcomma(str(ammout)) + '$')
			send_ls(user, '[id' + str(user_id) + '|пользователь] перевёл тебе ' + humanize.intcomma(str(ammout)) + '$')
	if 'перевести ' in message:
		
		from helpmethod.readdb import get_balance
		bal = get_balance(user_id)
		if int(ammout) > int(bal):
			msg(id, 'еблан? у тя баланса не хватает')
		else:
			new_balance = int(bal) - int(ammout)

			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (new_balance, user_id))
			sqlite_connection.commit()
			cur.close()

			from helpmethod.readdb import get_balance
			ball = get_balance(user)
			new_bal = int(ball) + int(ammout)

			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (new_bal, user))
			sqlite_connection.commit()
			cur.close()

			msg(id, '✅[id' + str(user_id) + '|Ты] перевёл [id' + str(user) + '|пользователю] ' +  humanize.intcomma(str(ammout)) + '$')
			send_ls(user, '[id' + str(user_id) + '|пользователь] перевёл тебе ' + humanize.intcomma(str(ammout)) + '$')