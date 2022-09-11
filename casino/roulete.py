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
def is_num(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

class Roulete:
	def Check(id, value, stavka, user_id):
		if str(value) == 'красное' or str(value) == 'red' or str(value) == 'black' or str(value) == 'черное' or str(value) == 'чёрное' or str(value) == 'zero' or str(value) == 'green' or str(value) == 'зеро' or str(value) == 'зелёное':
			Roulete.Method_Color(id, value, stavka, user_id)
		elif int(value) == 1 or int(value) == 2 or int(value) == 3 or int(value) == 4 or int(value) == 5 or int(value) == 6 or int(value) == 7 or int(value) == 8 or int(value) == 9 or int(value) == 10:
			Roulete.Method_Num(id, value, stavka, user_id)
		elif int(value) == 11 or int(value) == 12 or int(value) == 13 or int(value) == 14 or int(value) == 15 or int(value) == 16 or int(value) == 17 or int(value) == 18 or int(value) == 19 or int(value) == 20:
			Roulete.Method_Num(id, value, stavka, user_id)
		elif int(value) == 21 or int(value) == 22 or int(value) == 23 or int(value) == 24 or int(value) == 25 or int(value) == 26 or int(value) == 27 or int(value) == 28 or int(value) == 29 or int(value) == 30:
			Roulete.Method_Num(id, value, stavka, user_id)
		elif int(value) == 31 or int(value) == 32 or int(value) == 33 or int(value) == 34 or int(value) == 35 or int(value) == 36 or int(value) == 0:
			Roulete.Method_Num(id, value, stavka, user_id)
		else:
			msg(id, 'Вы указали неверный формат значения. Доступные форматы:\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0, Красное, Зеро, Чёрное.')
	def Method_Num(id, value, stavka, user_id):
		num = random.randint(0, 36)
		from helpmethod.readdb import get_balance
		balance = get_balance(user_id)
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		if int(value) == int(num):
			if id == 16:
				win = int(stavka) * 72
				from helpmethod.readdb import get_koef
				koef = int(get_koef(user_id))

				win *= koef

				result = int(win) + int(balance)

				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x72!\nТвой баланс: ' + humanize.intcomma(str(result)))

			else:
				win = int(stavka) * 36
				from helpmethod.readdb import get_koef
				koef = int(get_koef(user_id))

				win *= koef

				result = int(win) + int(balance)

				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
				sqlite_connection.commit()
				cur.close()

				msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x36!\nТвой баланс: ' + humanize.intcomma(str(result)))
		else:
			result = int(balance) - int(stavka)

			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (result, user_id))
			sqlite_connection.commit()
			cur.close()

			msg(id, '❌[id' + str(user_id) + "|" + str(nick) + '] ты проиграл:(\nТвой баланс: ' +  humanize.intcomma(str(result)))
	def Method_Color(id, value, stavka, user_id):
		num = random.randint(0, 36)
		from helpmethod.readdb import get_balance
		balance = get_balance(user_id)
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		if value == 'красное' or value == 'red':
			if int(num) == 1 or int(num) == 3 or int(num) == 5 or int(num) == 7 or int(num) == 9 or int(num) == 12 or int(num) == 14 or int(num) == 16 or int(num) == 18 or int(num) == 19 or int(num) == 21 or int(num) == 23 or int(num) == 25 or int(num) == 27 or int(num) == 30 or int(num) == 32 or int(num) == 34 or int(num) == 36:
				if id == 16:
					win = int(stavka) * 4
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)

					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()

					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x4!\nТвой баланс: ' + humanize.intcomma(str(result)))
					print('roulete.WIN: ' + str(user_id) + ', ' + str(result) + ', ' + str(num))
				else:
					win = int(stavka) * 2
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)

					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()

					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x2!\nТвой баланс: ' + humanize.intcomma(str(result)))
					print('roulete.WIN: ' + str(user_id) + ', ' + str(result) + ', ' + str(num))
			else:
				result = int(balance) - int(stavka)
				
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
				sqlite_connection.commit()
				cur.close()
				
				msg(id, '❌[id' + str(user_id) + "|" + str(nick) + '] ты проиграл:(\nТвой баланс: ' +  humanize.intcomma(str(result)))
		elif value == 'black' or value == 'черное' or value == 'чёрное':
			if int(num) == 2 or int(num) == 4 or int(num) == 6 or int(num) == 8 or int(num) == 10 or int(num) == 11 or int(num) == 13 or int(num) == 15 or int(num) == 17 or int(num) == 20 or int(num) == 22 or int(num) == 24 or int(num) == 26 or int(num) == 28 or int(num) == 29 or int(num) == 31 or int(num) == 33 or int(num) == 35:
				if id == 16:
					win = int(stavka) * 4
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)
					
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()
					
					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x4!\nТвой баланс: ' + humanize.intcomma(str(result)))
				else:
					win = int(stavka) * 2
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)
					
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()
					
					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x2!\nТвой баланс: ' + humanize.intcomma(str(result)))
			else:
				result = int(balance) - int(stavka)
				
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
				sqlite_connection.commit()
				cur.close()
				
				msg(id, '❌[id' + str(user_id) + "|" + str(nick) + '] ты проиграл:(\nТвой баланс: ' +  humanize.intcomma(str(result)))
		elif value == 'zero' or value == 'green' or value == 'зеро' or value == 'зелёное':
			if int(num) == 0:
				if id == 16:
					win = int(stavka) * 72
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)
					
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()
					
					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x72!\nТвой баланс: ' + humanize.intcomma(str(result)))
				else:
					win = int(stavka) * 36
					from helpmethod.readdb import get_koef
					koef = int(get_koef(user_id))

					win *= koef

					result = int(balance) + int(win)
					
					sqlite_connection = sqlite3.connect('databases\MDB.db')
					cur = sqlite_connection.cursor()

					cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
					sqlite_connection.commit()
					cur.close()
					
					msg(id, '💰[id' + str(user_id) + "|" + str(nick) + '] ты выиграл x36!\nТвой баланс: ' + humanize.intcomma(str(result)))
			else:
				result = int(balance) - int(stavka)
				
				sqlite_connection = sqlite3.connect('databases\MDB.db')
				cur = sqlite_connection.cursor()

				cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user_id))
				sqlite_connection.commit()
				cur.close()
				
				msg(id, '❌[id' + str(user_id) + "|" + str(nick) + '] ты проиграл:(\nТвой баланс: ' +  humanize.intcomma(str(result)))

def rouleteStart(id, user_id, message):
	stavk = message.replace('рулетка ', '')
	stavk_count = len(str(stavk))
	if stavk_count < 0:
		msg(id, 'ставка слишком маленькая.')
	else:
		stavka = stavk.split(' ')[0]
		val = stavk.split(' ')[1]
		valu = str(val)
		a = is_num(val)
		if a == False:
			from helpmethod.readdb import get_balance
			balance = get_balance(user_id)
			valu = str(val)
			num_ = is_num(stavka)
			if valu == 'red' or valu == 'black' or valu == 'zero' or valu == 'красное' or valu == 'черное' or valu == 'чёрное' or valu == 'зеро' or valu == 'зелёное':
				if num_ == False:
					msg(id, 'то, на что ты ставишь должно соответствовать параметрам из команды "рулетка хелп"')
				elif num_ == True:
					if int(balance) > int(stavka) or int(balance) == int(stavka):
						Roulete.Check(id, val, stavka, user_id)
					elif stavka == 'все' or stavka == 'всё':
						stavk = int(balance)
						Roulete.Check(id, val, stavk, user_id)
					elif int(stavka) > int(balance):
						msg(id, 'у тя не хватает деняк, еблан')
					else:
						msg(id, 'Отправьте это сообщение в тех.поддержку.\nROLL_ERR')
				else:
					msg(id, 'ERROR: Critical error rul_a01')
			else:
				msg(id, 'то, на что ты ставишь должно соответствовать параметрам из команды "рулетка хелп"')
		elif a == True:
			from helpmethod.readdb import get_balance
			balance = get_balance(user_id)
			value = int(val)
			num_ = is_num(stavka)
			if value == 1 or value == 2 or value == 3 or value == 4 or value == 5 or value == 6 or value == 7 or value == 8 or value == 9 or value == 10 or value == 11 or value == 12 or value == 13 or value == 14 or value == 15 or value == 16 or value == 17 or value == 18 or value == 19 or value == 20 or value == 21 or value == 22 or value == 23 or value == 24 or value == 25 or value == 26 or value == 27 or value == 28 or value == 29 or value == 30 or value == 31 or value == 32 or value == 33 or value == 34 or value == 35 or value == 36 or value == 0:
				if num_ == False:
					if stavka == 'все' or stavka == 'всё':
						stavk == int(balance)
						Roulete.Check(id, val, stavk, user_id)
					else:
						msg(id, 'ставка должна быть числом сука')
				elif num_ == True:
					if int(balance) > int(stavka) or int(balance) == int(stavka):
						Roulete.Check(id, val, stavka, user_id)
					elif int(stavka) > int(balance):
						msg(id, 'у тя не хватает деняк, еблан')
					else:
						msg(id, 'Отправьте это сообщение в тех.поддержку.\nROLL_ERR')
				else:
					msg(id, 'ERROR: Critical error rul_a01')
			else:
				msg(id, 'то, на что ты ставишь должно соответствовать параметрам из команды "рулетка хелп"')
		else:
			msg(id, 'not fixed error')