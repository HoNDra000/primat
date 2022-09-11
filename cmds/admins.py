import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()
def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def online_check(admin_id):
	is_on = bh.method('users.get', {'user_ids' : admin_id, 'fields' : 'online'})[0]
	is_online = is_on['online']
	if is_online == 1:
		return True
	else:
		return False

def get_name(uid: int) -> str:
	if int(uid) > 0:
		da = bh.method("users.get", {"user_ids": uid})
		dat = str(da)
		dat1 = dat.split("'first_name' : ")[0]
		data = dat1.replace("'", "")
		data_ = data.replace("'", "")
		d = data_.split(',')[1]
		data_f = d.replace(' first_name:', '')
		return data_f

def element_num(list):
    count = 0
    for element in list:
        count += 1
    return count

def checking(admin_id, admin_stat, admin_name):
	if admin_stat == 7:
		stat = '[7] Владелец'
	elif admin_stat == 6:
		stat = '[6] Администратор'
	elif admin_stat == 8:
		stat = '[5] Тестер'
	elif admin_stat == 5:
		stat = '[5] Разработчик'
	elif admin_stat == 4:
		stat = '[4] Куратор'
	elif admin_stat == 3:
		stat = '[3] Старший Модератор'
	elif admin_stat == 2:
		stat = '[2] Модератор'
	elif admin_stat == 1:
		stat = '[1] Хелпер'
	from helpmethod.readdb import get_texstat
	texstat = get_texstat(admin_id)
	return_ = texstat + '[id' + str(admin_id) + '|' + str(admin_name) + '] - ' + str(stat) + '\n'
	return return_

def admin_cycle(id):
	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT id, admin_lvl FROM users ORDER BY admin_lvl DESC')
	one = cursor.fetchall()
	a = 0
	num = element_num(one)
	full_list = ''
	while a < int(num):
		listt = one[int(a)]
		a += 1
		bb = str(listt)
		hh = bb.split(', ')[1]
		k = hh.replace(')', '')
		j = k.replace('(', '')
		if j != '0':
			idd = bb.split(', ')[0]
			ida = idd.replace('(', '')
			admin_id = ida.replace(')', '')
			admin_name = get_name(admin_id)
			from helpmethod.readdb import get_as
			admin_stat = get_as(admin_id)
			online = online_check(admin_id)
			if online == True:
				return_ = checking(admin_id, admin_stat, admin_name)
				if return_ == None:
					continue
				else:
					full_list = full_list + return_
	msg(id, 'Администрация бота, которая ответит вам на ваш вопрос:\n📕 - Ответит в течении 8 часов\n📙 - Ответит в течении 2 часов\n📗 - Ответит в течении 30 минут\n\n' + full_list)

def settexstatus(user_id, id, status):
	from helpmethod.readdb import get_as
	admin_stat = get_as(user_id)
	if int(admin_stat) == 1 or int(admin_stat) > 1:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		b = """UPDATE users SET tex_stat = ? WHERE id = ?"""
		cur.execute(b, (status, user_id))
		db.commit()
		if status == '📕':
			staa = '📕 - Ответ в течении 8 часов'
		elif status == '📙':
			staa = '📙 - Ответ в течении 2 часов'
		elif status == '📗':
			staa = '📗 - Ответ в течении 30 минут'
		msg(id, 'Твой статус в тех.поддержке установлен на: ' + str(staa))
