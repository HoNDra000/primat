import sqlite3

def avtomat(id, user_id, af, stavka):
	if id != 7:
		if af == 1:
			sqlite_connection= sqlite3.connect('databases\MDB.db', timeout=20)
			cursor = sqlite_connection.cursor()
			from helpmethod.readdb import get_balance
			stavka = int(get_balance(user_id))
			balance = stavka
			from .avtomatMethod import start, start_method
			start(id, stavka, user_id, balance)
		elif af == 0:
			from .avtomatMethod import start, start_method
			sqlite_connection= sqlite3.connect('databases\MDB.db', timeout=20)
			cursor = sqlite_connection.cursor()
			from helpmethod.readdb import get_balance
			balance = int(get_balance(user_id))
			start(id, stavka, user_id, balance)