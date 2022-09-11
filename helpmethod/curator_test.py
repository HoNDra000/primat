import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def element_num(list):
    count = 0
    for element in list:
        count += 1
    return count

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

def cur_cycle(user_id):
	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT id, curator_id FROM users ORDER BY curator_id DESC')
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

		if str(j) == str(user_id):
			idd = bb.split(', ')[0]
			ida = idd.replace('(', '')
			admin_id = ida.replace(')', '')
			admin_name = get_name(admin_id)
			full_list += '\n[id' + str(admin_id) + '|' + str(admin_name) + ']'
	return full_list