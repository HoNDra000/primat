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
            int(string)
            return True
        except ValueError:
            return False
def you1(user_id, id, user):
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 2 or int(admin_status) == 2:
		from helpmethod.readdb import get_as
		status = get_as(user)
		from helpmethod.readdb import get_balance
		mon = get_balance(user)
		ggg = humanize.intcomma(mon)
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		from helpmethod.readdb import get_nick
		nick_u = get_nick(user)
		from helpmethod.readdb import is_ban
		ban_ = is_ban(user)
		from helpmethod.readdb import get_specbal
		gem = get_specbal(user)
		gems = humanize.intcomma(gem)
		from helpmethod.readdb import get_case
		cas = get_case(user)
		cases = humanize.intcomma(cas)
		from helpmethod.readdb import get_lvl, get_koef
		levl = get_lvl(user)
		rebirth = str(int(get_koef(user)) - 1)
		if admin_status == 1:
			pref = 'H |'
		elif admin_status == 2:
			pref = 'M |'
		elif admin_status == 3:
			pref = 'Sr.M |'
		elif admin_status == 4:
			pref = 'Cur |'
		elif admin_status == 5:
			pref = 'Dev |'
		elif admin_status == 8:
			pref = 'T |'
		elif admin_status == 6:
			pref = 'ADM |'
		elif admin_status == 7:
			pref = 'OWN |'
		if ban_ == 0:
			ban = 'Не забанен'
		elif ban_ == 1:
			ban = 'Забанен'
		if int(status) > 1 or int(status) == 1:
			if int(status) == 1:
				n = '[1] Хелпер'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя H |  [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth))
			elif int(status) == 2:
				n = '[2] Модератор'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя M | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 3:
				n = '[3] Гл.Модератор'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Sr.M [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 4:
				n = '[4] Куратор'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Cur | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 5:
				n = '[5] Разработчик'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Dev | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 8:
				n = '[5] Тестер'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя T | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 6:
				n = '[6] Администратор'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя ADM | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			elif int(status) == 7:
				n = '[7] Владелец'
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя OWN | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
		else:
			msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: [0] Пользователь' + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		u_nick = get_nick(user)

		msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду you на пользователе [id' + str(user) + '|' + str(u_nick) + ']\n#you')
def you(user_id, id, message):
	user = message.replace('твоя инфа ', '')
	if "@" in user:
		userr = user.split("|")[0]
		user = userr.replace('[', '')
		if "id" in user:
			user = user.replace("id", "")
	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 2 or int(admin_status) == 2:
		num_ = is_num(user)
		if num_ == False:
			msg(id, "айди должен быть числом")
		else:
			from helpmethod.readdb import get_as
			status = get_as(user)
			from helpmethod.readdb import get_balance
			mon = get_balance(user)
			ggg = humanize.intcomma(mon)
			from helpmethod.readdb import get_nick
			nick = get_nick(user_id)
			from helpmethod.readdb import get_nick
			nick_u = get_nick(user)
			from helpmethod.readdb import is_ban
			ban_ = is_ban(user)
			from helpmethod.readdb import get_specbal
			gem = get_specbal(user)
			gems = humanize.intcomma(gem)
			from helpmethod.readdb import get_case
			cas = get_case(user)
			cases = humanize.intcomma(cas)
			from helpmethod.readdb import get_lvl, get_koef
			levl = get_lvl(user)
			rebirth = str(int(get_koef(user)) - 1)
			if admin_status == 1:
				pref = 'H |'
			elif admin_status == 2:
				pref = 'M |'
			elif admin_status == 3:
				pref = 'Sr.M |'
			elif admin_status == 4:
				pref = 'Cur |'
			elif admin_status == 5:
				pref = 'Dev |'
			elif admin_status == 8:
				pref = 'T |'
			elif admin_status == 6:
				pref = 'ADM |'
			elif admin_status == 7:
				pref = 'OWN |'
			if ban_ == 0:
				ban = 'Не забанен'
			elif ban_ == 1:
				ban = 'Забанен'
			if int(status) > 1 or int(status) == 1:
				if int(status) == 1:
					n = '[1] Хелпер'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя H | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 2:
					n = '[2] Модератор'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя M | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 3:
					n = '[3] Гл.Модератор'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Sr.M | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 4:
					n = '[4] Куратор'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Cur | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 5:
					n = '[5] Разработчик'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя Dev | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 8:
					n = '[5] Тестер'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя T | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 6:
					n = '[6] Администратор'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя ADM | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
				elif int(status) == 7:
					n = '[7] Владелец'
					msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя OWN | [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: ' + n + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth)) 
			else:
				msg(id, '📕 ' + pref + ' [id' + str(user_id) + "|" + str(nick) + '] ты глянул профиль пользователя [id' + str(user) + "|" + str(nick_u) + ']:\n💰 Баланс: ' + str(ggg) + "$" + '\n🗽 Его статус среди администрации: [0] Пользователь' + '\n💎Его гемы: ' + gems + '\n🎁Его кейсики: ' + cases + '\n‼Его бан статус: ' + str(ban) + '\n🏐Его уровень: ' + str(levl) + '\n📊Его перерождения: ' + str(rebirth))
			from helpmethod.readdb import get_nick
			nick = get_nick(user_id)
			u_nick = get_nick(user)

			msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду you на пользователе [id' + str(user) + '|' + str(u_nick) + ']\n#you')