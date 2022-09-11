import sqlite3
import humanize

def top():
	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM users ORDER BY koef DESC')
	one = cursor.fetchall()[0]
	one = str(one)
	non1 = one.replace('(', '')
	nonn1 = non1.replace(')', '')
	uid1 = nonn1.split(',')[0]
	use1 = nonn1.split(',')[1]
	user1 = use1.replace(" ' ", "")
	name1 = user1.replace("'", "")
	balanc1 = nonn1.split(",")[12]
	balance1 = balanc1.replace(" ", "")
	balance1 = int(balance1) - 1
	a1 = '1. [id' + str(uid1) + '|' + str(name1) + '] - ' + humanize.intcomma(balance1)
	db.close()

	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM users ORDER BY koef DESC')
	two = cursor.fetchall()[1]
	two = str(two)
	non2 = two.replace('(', '')
	nonn2 = non2.replace(')', '')
	uid2 = nonn2.split(',')[0]
	use2 = nonn2.split(',')[1]
	user2 = use2.replace(" ' ", "")
	name2 = user2.replace("'", "")
	balanc2 = nonn2.split(",")[12]
	balance2 = balanc2.replace(" ", "")
	balance2 = int(balance2) - 1
	a2 = '2. [id' + str(uid2) + '|' + str(name2) + '] - ' + humanize.intcomma(balance2)
	db.close()

	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM users ORDER BY koef DESC')
	three = cursor.fetchall()[2]
	three = str(three)
	non3 = three.replace('(', '')
	nonn3 = non3.replace(')', '')
	uid3 = nonn3.split(',')[0]
	use3 = nonn3.split(',')[1]
	user3 = use3.replace(" ' ", "")
	name3 = user3.replace("'", "")
	balanc3 = nonn3.split(",")[12]
	balance3 = balanc3.replace(" ", "")
	balance3 = int(balance3) - 1
	a3 = '3. [id' + str(uid3) + '|' + str(name3) + '] - ' + humanize.intcomma(balance3)
	db.close()

	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM users ORDER BY koef DESC')
	four = cursor.fetchall()[3]
	four = str(four)
	non4 = four.replace('(', '')
	nonn4 = non4.replace(')', '')
	uid4 = nonn4.split(',')[0]
	use4 = nonn4.split(',')[1]
	user4 = use4.replace(" ' ", "")
	name4 = user4.replace("'", "")
	balanc4 = nonn4.split(",")[12]
	balance4 = balanc4.replace(" ", "")
	balance4 = int(balance4) - 1
	a4 = '4. [id' + str(uid4) + '|' + str(name4) + '] - ' + humanize.intcomma(balance4)
	db.close()

	db = sqlite3.connect('databases\MDB.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM users ORDER BY koef DESC')
	five = cursor.fetchall()[4]
	five = str(five)
	non5 = five.replace('(', '')
	nonn5 = non5.replace(')', '')
	uid5 = nonn5.split(',')[0]
	use5 = nonn5.split(',')[1]
	user5 = use5.replace(" ' ", "")
	name5 = user5.replace("'", "")
	balanc5 = nonn5.split(",")[12]
	balance5 = balanc5.replace(" ", "")
	balance5 = int(balance5) - 1
	a5 = '5. [id' + str(uid5) + '|' + str(name5) + '] - ' + humanize.intcomma(balance5)
	db.close()
	top = a1 + '\n' + a2 + '\n' + a3 + '\n' + a4 + '\n' + a5
	return top