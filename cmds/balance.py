def balance(user_id):
	from helpmethod.readdb import get_balance
	ggg = get_balance(user_id)
	return ggg