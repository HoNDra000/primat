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

def costs(id):
	msg(id, '''Ты попал в цены на рабов! Весь доход указывается в минуту
		1 раб - Доход: 10к Цена: 15💎
		2 раба - Доход: 25к Цена: 25💎
		3 раба - Доход: 60к Цена: 45💎
		4 раба - Доход: 140к Цена: 60💎
		5 раба - Доход: 300к Цена: 85💎
		6 раба - Доход: 890к Цена: 105💎
		7 раба - Доход: 1.7 МЛН Цена: 145💎
		8 раба - Доход: 3.9 МЛН Цена: 195💎
		9 раба - Доход: 8.65 МЛН Цена: 245💎
		10 раба - Доход: 18м Цена: 300💎
		11 раба - Доход: 39 МЛН Цена: 380💎
		12 раба - Доход: 90 МЛН Цена: 450💎
		13 раба - Доход: 200 МЛН Цена: 570💎
		14 раба - Доход: 500 МЛН Цена: 710💎
		15 раба - Доход: 1 МЛРД Цена: 890💎
		16 раба - Доход: 3 МЛРД Цена: 1000💎
		17 раба - Доход: 10 МЛРД Цена: 1500💎
		18 раба - Доход: 30 МЛРД Цена: 2300💎
		19 раба - Доход: 100 МЛРД Цена: 3900💎
		20 раба - Доход: 500 МЛРД Цена: 5000💎
		''')

def menu(id, user_id):
	from helpmethod.readdb import get_rabs
	rabs = get_rabs(user_id)
	if rabs == 0:
		dohod = '0$ в минуту'
		cost = '0💎'
		nextt = '15💎'
	if rabs == 1:
		dohod = '10,000$ в минуту'
		cost = '15💎'
		nextt = '25💎'
	if rabs == 2:
		dohod = '25,000$ в минуту'
		cost = '25💎'
		nextt = '45💎'
	if rabs == 3:
		dohod = '60,000$ в минуту'
		cost = '45💎'
		nextt = '60💎'
	if rabs == 4:
		dohod = '140,000$ в минуту'
		cost = '60💎'
		nextt = '85💎'
	if rabs == 5:
		dohod = '300,000$ в минуту'
		cost = '85💎'
		nextt = '105💎'
	if rabs == 6:
		dohod = '890,000$ в минуту'
		cost = '105💎'
		nextt = '145💎'
	if rabs == 7:
		dohod = '1,700,000$ в минуту'
		cost = '145💎'
		nextt = '195💎'
	if rabs == 8:
		dohod = '3,900,000$ в минуту'
		cost = '195💎'
		nextt = '245💎'
	if rabs == 9:
		dohod = '8,650,000$ в минуту'
		cost = '245💎'
		nextt = '300💎'
	if rabs == 10:
		dohod = '18,000,000$ в минуту'
		cost = '300💎'
		nextt = '380💎'
	if rabs == 11:
		dohod = '39,000,000$ в минуту'
		cost = '380💎'
		nextt = '450💎'
	if rabs == 12:
		dohod = '90,000,000$ в минуту'
		cost = '450💎'
		nextt = '570💎'
	if rabs == 13:
		dohod = '200,000,000$ в минуту'
		cost = '570💎'
		nextt = '710💎'
	if rabs == 14:
		dohod = '500,000,000$ в минуту'
		cost = '710💎'
		nextt = '890💎'
	if rabs == 15:
		dohod = '1,000,000,000$ в минуту'
		cost = '890💎'
		nextt = '1000💎'
	if rabs == 16:
		dohod = '3,000,000,000$ в минуту'
		cost = '1000💎'
		nextt = '1500💎'
	if rabs == 17:
		dohod = '10,000,000,000$ в минуту'
		cost = '1500💎'
		nextt = '2300💎'
	if rabs == 18:
		dohod = '30,000,000,000$ в минуту'
		cost = '2300💎'
		nextt = '3900💎'
	if rabs == 19:
		dohod = '100,000,000,000$ в минуту'
		cost = '3900💎'
		nextt = '5000💎'
	if rabs == 20:
		dohod = '500,000,000,000$ в минуту'
		cost = '5000💎'
		nextt = 'Это максимальное кол-во купленных рабов👱🏿'
	msg(id, '📚Ты попал в меню управления рабов.\n👱🏿У тебя рабов: ' + str(rabs) + '\n💸Твой доход: ' + str(dohod) + '\n🏷Следующий раб стоит: ' + str(nextt))
def buy(id, user_id):
	from helpmethod.readdb import get_rabs
	rabs = get_rabs(user_id)
	if rabs == 0:
		dohod = '0$ в минуту'
		cost = '0💎'
		nextt = '15💎'
		cs = 15
	if rabs == 1:
		dohod = '10,000$ в минуту'
		cost = '15💎'
		cs = 25
		nextt = '25💎'
	if rabs == 2:
		dohod = '25,000$ в минуту'
		cost = '25💎'
		cs = 45
		nextt = '45💎'
	if rabs == 3:
		dohod = '60,000$ в минуту'
		cost = '45💎'
		cs = 60
		nextt = '60💎'
	if rabs == 4:
		dohod = '140,000$ в минуту'
		cost = '60💎'
		cs = 85
		nextt = '85💎'
	if rabs == 5:
		dohod = '300,000$ в минуту'
		cost = '85💎'
		cs = 105
		nextt = '105💎'
	if rabs == 6:
		dohod = '890,000$ в минуту'
		cost = '105💎'
		cs = 145
		nextt = '145💎'
	if rabs == 7:
		dohod = '1,700,000$ в минуту'
		cost = '145💎'
		cs = 195
		nextt = '195💎'
	if rabs == 8:
		dohod = '3,900,000$ в минуту'
		cost = '195💎'
		cs = 245
		nextt = '245💎'
	if rabs == 9:
		dohod = '8,650,000$ в минуту'
		cost = '245💎'
		cs = 300
		nextt = '300💎'
	if rabs == 10:
		dohod = '18,000,000$ в минуту'
		cost = '300💎'
		cs = 380
		nextt = '380💎'
	if rabs == 11:
		dohod = '39,000,000$ в минуту'
		cost = '380💎'
		cs = 450
		nextt = '450💎'
	if rabs == 12:
		dohod = '90,000,000$ в минуту'
		cost = '450💎'
		cs = 570
		nextt = '570💎'
	if rabs == 13:
		dohod = '200,000,000$ в минуту'
		cost = '570💎'
		cs = 710
		nextt = '710💎'
	if rabs == 14:
		dohod = '500,000,000$ в минуту'
		cost = '710💎'
		cs = 890
		nextt = '890💎'
	if rabs == 15:
		dohod = '1,000,000,000$ в минуту'
		cost = '890💎'
		cs = 1000
		nextt = '1000💎'
	if rabs == 16:
		dohod = '3,000,000,000$ в минуту'
		cost = '1000💎'
		cs = 1500
		nextt = '1500💎'
	if rabs == 17:
		dohod = '10,000,000,000$ в минуту'
		cost = '1500💎'
		cs = 2300
		nextt = '2300💎'
	if rabs == 18:
		dohod = '30,000,000,000$ в минуту'
		cost = '2300💎'
		cs = 3900
		nextt = '3900💎'
	if rabs == 19:
		dohod = '100,000,000,000$ в минуту'
		cost = '3900💎'
		cs = 5000
		nextt = '5000💎'
	if rabs == 20:
		dohod = '500,000,000,000$ в минуту'
		cost = '5000💎'
		cs = 666666
		nextt = 'Это максимальное кол-во купленных рабов👱🏿'
	from helpmethod.readdb import get_specbal
	gems = get_specbal(user_id)
	if cs == 666666:
		msg(id, 'У тебя уже максимальное кол-во рабов...')
	elif cs > gems:
		msg(id, 'Недостаточно гемов(((')
	else:
		a = rabs + 1
		if a == 1:
			adohod = '10,000$ в минуту'
			acost = '15💎'
			cs = 15
			nextt = '25💎'
		if a == 2:
			adohod = '25,000$ в минуту'
			acost = '25💎'
			cs = 25
			nextt = '45💎'
		if a == 3:
			adohod = '60,000$ в минуту'
			acost = '45💎'
			cs = 45
			nextt = '60💎'
		if a == 4:
			adohod = '140,000$ в минуту'
			acost = '60💎'
			cs = 60
			nextt = '85💎'
		if a == 5:
			adohod = '300,000$ в минуту'
			acost = '85💎'
			cs = 85
			nextt = '105💎'
		if a == 6:
			adohod = '890,000$ в минуту'
			acost = '105💎'
			cs = 105
			nextt = '145💎'
		if a == 7:
			adohod = '1,700,000$ в минуту'
			acost = '145💎'
			cs = 145
			nextt = '195💎'
		if rabs == 8:
			adohod = '3,900,000$ в минуту'
			acost = '195💎'
			cs = 195
			nextt = '245💎'
		if a == 9:
			adohod = '8,650,000$ в минуту'
			acost = '245💎'
			cs = 245
			nextt = '300💎'
		if a == 10:
			adohod = '18,000,000$ в минуту'
			acost = '300💎'
			cs = 300
			nextt = '380💎'
		if a == 11:
			adohod = '39,000,000$ в минуту'
			acost = '380💎'
			cs = 380
			nextt = '450💎'
		if a == 12:
			adohod = '90,000,000$ в минуту'
			acost = '450💎'
			cs = 450
			nextt = '570💎'
		if a == 13:
			adohod = '200,000,000$ в минуту'
			acost = '570💎'
			cs = 570
			nextt = '710💎'
		if a == 14:
			adohod = '500,000,000$ в минуту'
			acost = '710💎'
			cs = 710
			nextt = '890💎'
		if a == 15:
			adohod = '1,000,000,000$ в минуту'
			acost = '890💎'
			cs = 890
			nextt = '1000💎'
		if a == 16:
			adohod = '3,000,000,000$ в минуту'
			acost = '1000💎'
			cs = 1000
			nextt = '1500💎'
		if a == 17:
			adohod = '10,000,000,000$ в минуту'
			acost = '1500💎'
			cs = 1500
			nextt = '2300💎'
		if a == 18:
			adohod = '30,000,000,000$ в минуту'
			acost = '2300💎'
			cs = 2300
			nextt = '3900💎'
		if a == 19:
			adohod = '100,000,000,000$ в минуту'
			acost = '3900💎'
			cs = 3900
			nextt = '5000💎'
		if a == 20:
			adohod = '500,000,000,000$ в минуту'
			acost = '5000💎'
			cs = 5000
			nextt = 'Это максимальное кол-во купленных рабов👱🏿'
		result = int(gems) - int(cs)
		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()
		b = """UPDATE users SET spec_bal = ? WHERE id = ?"""
		cur.execute(b, (result, user_id))
		c = """UPDATE users SET rabs = ? WHERE id = ?"""
		cur.execute(c, (a, user_id))
		sqlite_connection.commit()
		cur.close()
		msg(id, 'Ты купил своего ' + str(a) + '-го раба!\n Теперь твой доход: ' + adohod + '\nСледующий раб стоит: ' + str(nextt))