import sqlite3

def give_case(user_id, id, user):

	from helpmethod.readdb import get_as
	admin_status = get_as(user_id)
	if int(admin_status) > 5 or int(admin_status) == 5:
		sqlite_connection = sqlite3.connect('databases\MDB.db')
		cur = sqlite_connection.cursor()

		from helpmethod.readdb import get_case
		cases = get_case(user)
		if cases == None:
			cases = 0
			result = int(cases) + 1
		else:
			result = int(cases) + 1

		a = """UPDATE users SET cases = ? WHERE id = ?"""
		cur.execute(a, (result, user))
		sqlite_connection.commit()
		cur.close()
		return True
	else:
		return False