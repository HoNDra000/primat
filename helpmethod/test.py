import sqlite3
import time

def elements_num(list):
    count = 0
    for element in list:
        count += 1
    return count

def business_cycle():
	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT id, rabs FROM users ORDER BY rabs')
	one = cursor.fetchall()
	a = 0
	num = elements_num(one)
	final = ''
	while a < int(num):
		listt = one[int(a)]
		a += 1
		bb = str(listt)
		hh = bb.split(', ')[1]
		k = hh.replace(')', '')
		j = k.replace('(', '')
		idd = bb.split(', ')[0]
		ida = idd.replace('(', '')
		id = ida.replace(')', '')
		if j != '0':
			check_num_rabs(id)
	time.sleep(60)

def check_num_rabs(id):
	from helpmethod.readdb import get_rabs, get_balance
	rabs = get_rabs(id)
	if rabs == 1:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 100

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 2:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 250

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 3:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 600

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 4:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			result = int(old_bal) + 1400
			b = """UPDATE users SET balance = ? WHERE id = ?"""

			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			result *= koef

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 5:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 3000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 6:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 8900

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 7:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 17000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 8:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 39000

			result = int(old_bal) + yj

			b = """UPDATE users SET balance = ? WHERE id = ?"""

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 9:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 86500

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 10:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 180000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""

			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 11:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 390000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 12:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 900000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 13:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 2000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 14:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 5000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 15:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 10000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 16:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 20000000

			result = int(old_bal) + yj

			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 17:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 90000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 18:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 110000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 19:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 175000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()
	elif rabs == 20:
		db = sqlite3.connect('databases\MDB.db', timeout=20)
		cur = db.cursor()
		old_bal = get_balance(id)
		if old_bal != '-∞':
			from helpmethod.readdb import get_koef
			koef = int(get_koef(id))

			yj = koef * 250000000

			result = int(old_bal) + yj
			b = """UPDATE users SET balance = ? WHERE id = ?"""
			cur.execute(b, (str(result), id))
			db.commit()

def start_bis():
	number = 1

	while number == 1:
		business_cycle()