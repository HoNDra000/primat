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


def sub(id, user_id, id_u, bal):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 4 or int(admin_status) == 4:
		num_ = is_num(id_u)
		if num_ == False:
			msg(id, "айди должен быть числом")
		else:
			aa = is_num(bal)
			if aa == False:
				msg(id, "баланс должен быть числом")
			else:
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (bal, id_u))
				sqlite_connection.commit()
				cur.close()
				from helpmethod.readdb import get_nick
				u_nick = get_nick(id_u)
				msg(id, '[id' + str(user_id) + '|Ты] успешно выдал пользователю [id' + str(id_u) + '|' + str(u_nick) + '] баланс: ' + humanize.intcomma(str(bal)) + '$')
				from helpmethod.readdb import get_nick
				nick = get_nick(user_id)
				u_nick = get_nick(id_u)

				msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду set_user_balance на пользователе [id' + str(id_u) + '|' + str(u_nick) + '] и выдал ему: ' + humanize.intcomma(str(bal)) + '\n#sub')