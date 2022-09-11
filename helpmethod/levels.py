import sqlite3
import humanize

def Lvl_prices(level):
    x = 10000000 #десять миллионов
    price_lvl = {
        1: x,
        2: x*50,
        3: x*150,
        4: x*450,
        5: x*1500,
        6: x*3500,
        7: x*7000,
        8: x*10000,
        9: x*100000,
        10: x*1000000}
    return price_lvl.get(level)

def next_price(next_level, user):
    from helpmethod.readdb import get_koef
    coef = int(get_koef(user)) * 2
    x = 10000000 #десять миллионов
    price_lvl = {
        1: x*coef,
        2: x*50*coef,
        3: x*150*coef,
        4: x*450*coef,
        5: x*1500*coef,
        6: x*3500*coef,
        7: x*7000*coef,
        8: x*10000*coef,
        9: x*100000*coef,
        10: x*1000000*coef,
        11: 'Это максимальный уровень.'}
    return price_lvl.get(next_level)

def menu_levelup(user):
    from helpmethod.readdb import get_lvl
    level = get_lvl(user)
    next_level = int(level) + 1
    if next_level == 11:
        nl = 'Это максимальный уровень'
    else:
        nl = next_level
    next_cost = next_price(next_level,user)
    ret = '''Ты попал в меню прокачки уровня!
Сейчас твой уровень: {level}
Следующий твой уровень: {next_level}
Стоимость следующего уровня: {next_level_cost}'''.format(level=level,next_level=nl,next_level_cost=next_cost)
    return ret
def get_new_rules(next_level):
    if next_level == 1:
        new_rules = '\n1.Использование команды "бонус"\n2.Использование команды "перевод"\n3.10💎 на счёт.'
    elif next_level == 2:
        new_rules = '\n1.30💎 на счёт.'
    elif next_level == 3:
        new_rules = '\n1.Использование команды "сетник"\n2.100💎 на счёт'
    elif next_level == 4:
        new_rules = '\n1.25 кейсиков\n2.250💎 на счёт'
    elif next_level == 5:
        new_rules = '\n1.15 кейсиков\n2.200💎 на счёт\n3.Использование нового режима казино "рулетка"'
    elif next_level == 6:
        new_rules = '\n1.35 кейсиков\n2.150💎 на счёт'
    elif next_level == 7:
        new_rules = '\n1.Использование команды "ребитх"\n2.50 кейсиков\n3.300💎 на счёт'
    elif next_level == 8:
        new_rules = '\n1.Использование нового режима казино "автомат"\n2.120 кейсиков\n3.600💎 на счёт\nP.s.На Следующих уровнях не будет наград.'
    elif next_level == 9:
        new_rules = '\nНету новых прав.'
    elif next_level == 10:
        new_rules = '\nНету новых прав.'
    elif next_level == 11:
        new_rules = '\nНету новых прав.'
    return new_rules

def level_up(user):
    from helpmethod.readdb import get_lvl, get_balance
    balance = get_balance(user)
    level = get_lvl(user)
    next_level = int(level) + 1
    price = next_price(next_level, user)
    if level < 10:
        if int(balance) < int(price):
            mess = 'У тебя не хватает денег на балансе для прокачки уровня, поиграй в казик чтоле...'
            return mess
        else:

            result = int(balance) - int(price)

            sqlite_connection = sqlite3.connect('databases\MDB.db')
            cur = sqlite_connection.cursor()

            cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (str(result), user))
            sqlite_connection.commit()
            cur.execute(f"""UPDATE users SET level = ? WHERE id = ?""", (next_level, user))
            sqlite_connection.commit()
            

            new_rules = get_new_rules(next_level)

            from helpmethod.readdb import get_specbal, get_case

            if next_level == 1:
                old = get_specbal(user)
                res = old + 10
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
            elif next_level == 2:
                old = get_specbal(user)
                res = old + 30
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
            elif next_level == 3:
                old = get_specbal(user)
                res = old + 100
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
            elif next_level == 4:
                old = get_specbal(user)
                olld = get_case(user)
                rees = olld + 25
                res = old + 250
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
                cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (rees, user))
                sqlite_connection.commit()
            elif next_level == 5:
                old = get_specbal(user)
                olld = get_case(user)
                rees = olld + 15
                res = old + 200
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
                cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (rees, user))
                sqlite_connection.commit()
            elif next_level == 6:
                old = get_specbal(user)
                olld = get_case(user)
                rees = olld + 35
                res = old + 150
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
                cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (rees, user))
                sqlite_connection.commit()
            elif next_level == 7:
                old = get_specbal(user)
                olld = get_case(user)
                rees = olld + 50
                res = old + 300
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
                cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (rees, user))
                sqlite_connection.commit()
            elif next_level == 8:
                old = get_specbal(user)
                olld = get_case(user)
                rees = olld + 120
                res = old + 600
                cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res, user))
                sqlite_connection.commit()
                cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (rees, user))
                sqlite_connection.commit()

            mess = 'Ты улучшил свой уровень до ' + str(next_level) + '\nУ тебя на балансе осталось: ' + humanize.intcomma(str(balance)) + '$\n\nТы получаешь:' + new_rules
            cur.close()
            return mess
    else:
        mess = 'У тебя уже максимальный уровень.'
        return mess

def rebirth(user):
    from helpmethod.readdb import get_koef, get_lvl
    level = get_lvl(user)
    if level > 7 or level == 7:
        sqlite_connection = sqlite3.connect('databases\MDB.db')
        cur = sqlite_connection.cursor()

        old_koef = get_koef(user)
        res_koef = int(old_koef) + 1
        rebirth = int(res_koef) - 1

        cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (1000000, user))
        sqlite_connection.commit()
        cur.execute(f"""UPDATE users SET level = ? WHERE id = ?""", (0, user))
        sqlite_connection.commit()
        cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (0, user))
        sqlite_connection.commit()
        cur.execute(f"""UPDATE users SET koef = ? WHERE id = ?""", (res_koef, user))
        sqlite_connection.commit()
        cur.execute(f"""UPDATE users SET rabs = ? WHERE id = ?""", (0, user))
        sqlite_connection.commit()
        cur.close()
        mess = 'Поздравляю с ребитхом! Теперь у тебя ' + str(rebirth) + ' ребитхов (перерождений)'
    else:
        mess = 'Тебе нужен 7 или более уровень для перерождения.'
    return mess