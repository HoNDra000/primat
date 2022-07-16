def reply_check(give, event):
	msg_inf = event.obj['message']
	print(msg_inf)
	msg_id = event.obj['message']['conversation_message_id']
	print(msg_id)
	if 'reply_message' in msg_inf:
		reply_check = msg_inf['reply_message']['from_id']
		print(reply_check)
		return reply_check
	else:
		reply_check = event.obj['message']['from_id']
		return reply_check