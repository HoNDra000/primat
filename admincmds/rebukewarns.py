import sqlite3

from helpmethod.readdb import get_rebuke, get_warns

def give_rebuke(user):
	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	new = int(get_rebuke(user)) + 1

	cur.execute(f"""UPDATE users SET rebuke = ? WHERE id = ?""", (new, user))
	sqlite_connection.commit()
	cur.close()

def give_warn(user):
	sqlite_connection = sqlite3.connect('databases\MDB.db')
	cur = sqlite_connection.cursor()

	new = int(get_warns(user)) + 1

	cur.execute(f"""UPDATE users SET warns = ? WHERE id = ?""", (new, user))
	sqlite_connection.commit()
	cur.close()
