import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

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

def staff_info(user_id, id):
	from helpmethod.readdb import get_addchat, get_as, get_nick, get_tasks, get_bans, get_curator, get_warns, get_rebuke
	from helpmethod.curator_test import cur_cycle
	a_s = get_as(user_id)
	nick = get_nick(user_id)
	chats = get_addchat(user_id)
	tasks = get_tasks(user_id)
	bans = get_bans(user_id)
	her_staff = cur_cycle(user_id)
	curator = get_curator(user_id)
	curator_name = get_name(curator)
	warns = get_warns(user_id)
	rebuke = get_rebuke(user_id)

	if a_s == 0:
		msg(id, 'Недостаточно прав.')
	else:
		if a_s == 1:
			stat = '[1] Хелпер'
			s = 'хелпера'
			limit_sb = 'Данная команда тебе не доступна'
			norma = '3 добавленных бесед в месяц'
		elif a_s == 2:
			stat = '[2] Модератор'
			s = 'модератора'
			limit_sb = 'Данная команда тебе не доступна'
			norma = '10 банов в месяц'
		elif a_s == 3:
			stat = '[3] Главный Модератор'
			s = 'модератора'
			limit_sb = '50,000,000$'
			norma = '15 банов в месяц + 1-2 разбанов'
		elif a_s == 4:
			stat = '[4] Куратор'
			s = 'куратора'
			limit_sb = '250,000,000$'
			norma = 'Следить за своим стаффом'
		elif a_s == 5:
			stat = '[5] Разработчик'
			s = 'азработчика'
			limit_sb = '∞$'
			norma =  'пахать как негр'
		elif a_s == 8:
			stat = '[5] Тестер'
			s = 'тестера'
			limit_sb = '∞$'
			norma = 'помогать  разрабу пахать как негру.'
		elif a_s == 6:
			stat = '[6] Администратор'
			s = 'администраторов'
			limit_sb = '∞$'
			if user_id == 419536366:
				norma = 'Следить за всем стаффом'
			elif user_id == 418824109:
				norma = 'Следить за всеми тестерами'
		elif a_s == 7:
			stat = '[7] Владелец'
			s = 'вледельца'
			limit_sb = '∞$'
			norma = 'Следить за неграми (Разрабами и Админами)'
		else:
			msg(id, 'Uknown error')
		if curator == 666:
			msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user_id) + '|' + str(nick) + ']:\n\n📌Твои подчинённые: ' + her_staff + '\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Твой статус стаффа: ' + str(stat) + '\n\n📊Твой лимит в "sb": ' + str(limit_sb) + '\n\n🚬Твоя обязанность в боте: ' + norma)
		else:
			if a_s > 5 or a_s == 5:
				msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user_id) + '|' + str(nick) + ']:\n\n📌Твой куратор: [id' + str(curator) + '|' + str(curator_name) + ']\n\n📌Твои подчинённые: ' + her_staff + '\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Твой статус стаффа: ' + str(stat) + '\n\n📊Твой лимит в "sb": ' + str(limit_sb) + '\n\n🚬Твоя обязанность в боте: ' + norma + '\n\n❗Твои предупреждения: ' + str(warns) + '\n\n🚫Твои выговоры: ' + str(rebuke))
			else:
				msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user_id) + '|' + str(nick) + ']:\n\n📌Твой куратор: [id' + str(curator) + '|' + str(curator_name) + ']\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Твой статус стаффа: ' + str(stat) + '\n\n📊Твой лимит в "sb": ' + str(limit_sb) + '\n\n🚬Твоя обязанность в боте: ' + norma + '\n\n❗Твои предупреждения: ' + str(warns) + '\n\n🚫Твои выговоры: ' + str(rebuke))
def you_staff_info(user_id, user, id):
	from helpmethod.readdb import get_addchat, get_as, get_nick, get_tasks, get_bans, get_curator, get_warns, get_rebuke
	from helpmethod.curator_test import cur_cycle
	a_s = get_as(user)
	nick = get_nick(user)
	chats = get_addchat(user)
	tasks = get_tasks(user)
	bans = get_bans(user)
	her_staff = cur_cycle(user)
	admin_status = get_as(user)
	curator = get_curator(user)
	curator_name = get_name(curator)
	warns = get_warns(user)
	rebuke = get_rebuke(user)


	if admin_status > 4 or admin_status == 4:
		if a_s == 1:
			stat = '[1] Хелпер'
			s = 'хелпера'
			limit_sb = 'Данная команда тебе не доступна'
			norma = '3 добавленных бесед в месяц'
		elif a_s == 2:
			stat = '[2] Модератор'
			s = 'модератора'
			limit_sb = 'Данная команда тебе не доступна'
			norma = '10 банов в месяц'
		elif a_s == 3:
			stat = '[3] Главный Модератор'
			s = 'модератора'
			limit_sb = '50,000,000$'
			norma = '15 банов в месяц + 1-2 разбанов'
		elif a_s == 4:
			stat = '[4] Куратор'
			s = 'куратора'
			limit_sb = '250,000,000$'
			norma = 'Следить за своим стаффом'
		elif a_s == 5:
			stat = '[5] Разработчик'
			s = 'азработчика'
			limit_sb = '∞$'
			norma =  'пахать как негр'
		elif a_s == 8:
			stat = '[5] Тестер'
			s = 'тестера'
			limit_sb = '∞$'
			norma = 'помогать  разрабу пахать как негру.'
		elif a_s == 6:
			stat = '[6] Администратор'
			s = 'администраторов'
			limit_sb = '∞$'
			if user == 419536366:
				norma = 'Следить за всем стаффом'
			elif user == 418824109:
				norma = 'Следить за всеми тестерами'
		elif a_s == 7:
			stat = '[7] Владелец'
			s = 'вледельца'
			limit_sb = '∞$'
			norma = 'Следить за неграми (Разрабами и Админами)'
		else:
			msg(id, 'Uknown error')
		if curator == 666:
			msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user) + '|' + str(nick) + ']:\n\n📌Его подчинённые: ' + her_staff + '\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Его статус стаффа: ' + str(stat) + '\n\n📊Его лимит в "sb": ' + str(limit_sb) + '\n\n🚬Его обязанность в боте: ' + norma)
		else:
			if a_s > 5 or a_s == 5:
				msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user) + '|' + str(nick) + ']:\n\n📌Его куратор: [id' + str(curator) + '|' + str(curator_name) + ']\n\n📌Его подчинённые: ' + her_staff + '\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Его статус стаффа: ' + str(stat) + '\n\n📊Его лимит в "sb": ' + str(limit_sb) + '\n\n🚬Его обязанность в боте: ' + norma + '\n\n❗Его предупреждения: ' + str(warns) + '\n\n🚫Его выговоры: ' + str(rebuke))
			else:
				msg(id, '📋 STAFF-INFO 📋\n📘Информация  ' + s + ' [id' + str(user) + '|' + str(nick) + ']:\n\n📌Его куратор: [id' + str(curator) + '|' + str(curator_name) + ']\n\n⛔Количество банов: ' + str(bans) + '\n\n📖Количество выполненных заданий: ' + str(tasks) + '\n\n📱Количество чатов куда он добавил бота: ' + str(chats) + '\n\n🎓Его статус стаффа: ' + str(stat) + '\n\n📊Его лимит в "sb": ' + str(limit_sb) + '\n\n🚬Его обязанность в боте: ' + norma + '\n\n❗Его предупреждения: ' + str(warns) + '\n\n🚫Его выговоры: ' + str(rebuke))
		from helpmethod.readdb import get_nick
		nick = get_nick(user_id)
		u_nick = get_nick(user)

		msg(32, '[id' + str(user_id) + '|' + str(nick) + '] использовал команду you_staff_info на пользователе [id' + str(user) + '|' + str(u_nick) + ']\n#check_staff-info')


