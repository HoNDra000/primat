import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import sqlite3

token = "vk1.a.zOkbeKjvIF4sOUBpjRGpxzVxls54g0JprB41XvKBgcU0OotuiW33hnLVUs8NEF7Mzdxx1oecpf3gnwE0No0tG7YJXgNxoRHfJo5elf9kQ00RagEa8kZ2Ck7RkjhbhlU0Oxe3GVSeVlSOPi_JlvqQV4C-IFQfEBP-rWJ8Lscq4a8I5RE8i3ckDoJbf7zlZ-Ky"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 210219643)
give = bh.get_api()

def msg(id, text):
    bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})

def start_gems(win, old_gem, user_id, id):
    if win == 11:
        old_gem += 1
        return old_gem
    elif win == 12:
        old_gem += 5
        return old_gem
    elif win == 13:
        old_gem += 10
        return old_gem
    elif win == 14:
        old_gem += 2
        return old_gem
    elif win == 15:
        old_gem += 15
        return old_gem
    elif win == 16:
        old_gem += 17
        return old_gem
    elif win == 17:
        old_gem += 4
        return old_gem
    elif win == 18:
        old_gem += 20
        return old_gem
    elif win == 19 or win == 20:
        return old_gem

def start_money(win, old_money):
    if win == 1:
        old_money += 100000000
    elif win == 2:
        old_money += 100000000
    elif win == 3:
        old_money += 100000000
    elif win == 4:
        old_money += 100000000
    elif win == 5:
        old_money += 100000000
    elif win == 6:
        old_money += 100000000
    elif win == 7:
        old_money += 100000000
    elif win == 8:
        old_money += 100000000
    elif win == 9:
        old_money += 100000000
    elif win == 10:
        old_money += 100000000
    return old_money
    
def start_allcase(user_id, id):
    from helpmethod.readdb import get_case
    AllCase = get_case(user_id)
    total_case = get_case(user_id)
    msg(id, 'Генерирую дроп...')
    old_money = 0
    old_gem = 0
    for i in range(0, AllCase):
        from cmds.opencase import open_case
        win = open_case(id, user_id)
        if win == 0:
            msg(id, 'У тя нету кейсиков')
        elif win > 0 and win < 11:
            old_money = start_money(win, old_money)
        elif win > 10:
            old_gem = start_gems(win, old_gem, user_id, id)
        else:
            msg(id, 'error')
        AllCase -= 1
    win_money = old_money
    win_gems = old_gem

    from helpmethod.readdb import get_balance
    from helpmethod.readdb import get_specbal

    old_bal = get_balance(user_id)
    old_gems = get_specbal(user_id)

    res_money = int(old_bal) + int(win_money)
    res_gems = int(old_gems) + int(win_gems)

    sqlite_connection = sqlite3.connect('databases\MDB.db')
    cur = sqlite_connection.cursor()
    cur.execute(f"""UPDATE users SET balance = ? WHERE id = ?""", (res_money, user_id))
    cur.execute(f"""UPDATE users SET spec_bal = ? WHERE id = ?""", (res_gems, user_id))
    cur.execute(f"""UPDATE users SET cases = ? WHERE id = ?""", (0, user_id))
    sqlite_connection.commit()
    cur.close()

    msg(id, "[id" + str(user_id) + '|Ты] открыл ' + str(total_case) + ' кейсиков, и получил с них:\nДеняк: ' + str(win_money) + '\nГемов: ' + str(win_gems))