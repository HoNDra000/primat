import sqlite3
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from threading import Thread

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text, keyboard):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})

def create_keyboard(num):
	keyboard = VkKeyboard(inline=True)
	if num == 1:
		keyboard.add_callback_button('2x', color=VkKeyboardColor.POSITIVE, payload={"type": "2x", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('3x', color=VkKeyboardColor.POSITIVE, payload={"type": "3x", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('5x', color=VkKeyboardColor.SECONDARY, payload={"type": "5x", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('10x', color=VkKeyboardColor.SECONDARY, payload={"type": "10x", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('25x', color=VkKeyboardColor.PRIMARY, payload={"type": "25x", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('50x', color=VkKeyboardColor.PRIMARY, payload={"type": "50x", "text": "Это исчезающее сообщение"})
		keyboard.add_line()
		keyboard.add_callback_button('75x', color=VkKeyboardColor.NEGATIVE, payload={"type": "75x", "text": "Это исчезающее сообщение"})
		keyboard.add_callback_button('100x', color=VkKeyboardColor.NEGATIVE, payload={"type": "100x", "text": "Это исчезающее сообщение"})

	return keyboard.get_keyboard()

def wait_chat_bet(user):
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			print(event.obj)
			user_id = event.obj['message']['from_id']
			message = str(event.object.message['text'].lower())
			
			if user_id == user:
				msg(45, "sucess " + str(message), None)
				break

def wait_bet():
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_EVENT:
			peer = event.obj['peer_id']
			user = event.obj['user_id']
			if peer == 2000000045:
				msg(45, "[id" + str(user) + "|Пользователь], Введи ставку", None)
				wait_chat_bet(user)




def default():
	msg(45, "Колесо фортуны!\nОставшееся время: {out_time}\n\nВыберите коэффицент: ", create_keyboard(1))
	wait_bet()
	#mess_id = 
	#out_time = get_out_time(60)
	#while int(out_time) > 0: