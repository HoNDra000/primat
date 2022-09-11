import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def mail_continue(id, text, a):
	try:
		with open('count_of_chats.txt', 'r') as f:
			count = f.read()
		while int(a) < int(count):
			a += 1
			msg(a, text)
		msg(id, 'Рассылка завершена.')
	except vk_api.exceptions.ApiError:
		mail_continue(id, text, a)

def mail(id, text):
	try:
		with open('count_of_chats.txt', 'r') as f:
			count = f.read()
		a = 0

		while int(a) < int(count):
			if a == 8 or a == 9 or a == 10:
				continue
			else:
				a += 1
				msg(a, text)
	except vk_api.exceptions.ApiError:
		mail_continue(id, text, a)