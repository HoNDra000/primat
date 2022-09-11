import sqlite3
import random

def open_case(id, user_id):
	win = random.randint(1, 20)

	from helpmethod.readdb import get_case

	cas = get_case(user_id)

	if cas < 0 or cas == 0:
		win = 0
		return win
	else:
		if win == 1:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 100000000 #10 миллиардов

			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 2:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 5000000 #5 миллиардов
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 3:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 25000000 #25 миллиардов
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 4:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 100000000 #1 миллиард
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 5:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 50000000 #50 миллиард
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 6:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 10000000 #100 миллиард
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 7:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 1500000000 #1.5 миллиард
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 8:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 1000000 #1 лям
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 9:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 100 #100 миллиард
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 10:
			from helpmethod.readdb import get_balance
			old = get_balance(user_id)
			res = int(old) + 1 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 11:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 1 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 12:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 5 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 13:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 10 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 14:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 2 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 15:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 15 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 16:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 17 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 17:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 4 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		elif win == 18:
			from helpmethod.readdb import get_specbal
			old = get_specbal(user_id)
			res = int(old) + 20 #1
			
			sqlite_connection = sqlite3.connect('databases\MDB.db')
			cur = sqlite_connection.cursor()
			cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user_id))
			cass = int(cas) - 1
			cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (cass, user_id))
			sqlite_connection.commit()
			cur.close()
		return win