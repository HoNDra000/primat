def reply_check(give, event):
	msg_inf = event.obj['message']
	if 'reply_message' in msg_inf:
		reply_check = msg_inf['reply_message']['from_id']
		return reply_check
	else:
		reply_check = event.obj['message']['from_id']
		return reply_check
def reply_check_logger_user(give, event):
	msg_inf = event.obj['message']
	if 'reply_message' in msg_inf:
		reply_check = msg_inf['reply_message']['text']
		reply_check = reply_check.split('[id')[1]
		reply_check = reply_check.split('|')[0]
		if int(reply_check) < 0:
			return False
		else:
			return reply_check
	else:
		return False
def reply_check_logger_chat(give, event):
	msg_inf = event.obj['message']
	if 'reply_message' in msg_inf:
		reply_check = msg_inf['reply_message']['text']
		reply_check = reply_check.replace('Chat_ID: ', '')
		reply_check = reply_check.split('\n')[0]
		if int(reply_check) < 0:
			return False
		else:
			return reply_check
	else:
		return False