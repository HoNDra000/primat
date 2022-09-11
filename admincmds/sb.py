import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import humanize

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

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

def sb(id, user_id, bal):
	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (bal, user_id))
	sqlite_connection.commit()
	cur.close()

	msg(id, '✅[id' + str(user_id) + '|Ты] выдал себе ' + humanize.intcomma(bal) + '$')
	from helpmethod.readdb import get_nick
	nick = get_nick(user_id)

	msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду sb со значением: ' + str(bal) + '\n#reset_bal')
def setbalance_check(id, user_id, bal):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	num_ = is_num(bal)
	if num_ == False:
		msg(id, "баланс должен быть числом")
	else:
		if int(admin_status) == 0:
			print(' ')
		elif int(admin_status) == 1:
			msg(id, 'Не достаточно прав. Для совершения этого действия вам нужен: [3] Гл.Модератор')
		elif int(admin_status) == 2:
			msg(id, 'Не достаточно прав. Для совершения этого действия вам нужен: [3] Гл.Модератор')
		elif int(admin_status) == 3:
			if int(bal) > 500000000:
				msg(id, 'Не превышай своего лимита. Твой лимит: 500,000,000$')
			else:
				sb(id, user_id, bal)
		elif int(admin_status) == 4:
			if int(bal) > 250000000000:
				msg(id, 'Не превышай своего лимита. Твой лимит: 250,000,000,000$')
			else:
				sb(id, user_id, bal)
		else:
			sb(id, user_id, bal)
