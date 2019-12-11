import telebot
import config
from task_7.ContextManagerSQLite import ContextManagerSQLite

bot = telebot.TeleBot(config.TOKEN)


def check_id(value):
    users_id = []
    user_id = value
    sql = 'SELECT id, id_telegram FROM users '
    with ContextManagerSQLite('people.db') as s:
        query_response = s.execute(sql)
        for i in query_response:
            i_id, i_id_telegram = i
            users_id.append(i_id_telegram)
        if str(user_id) in users_id:
            return False
        else:
            return True


def check_name(value):
    n_name_user = ''
    user_id = str(value)
    sql = 'SELECT id, name FROM users WHERE id_telegram=? '
    with ContextManagerSQLite('people.db') as s:
        query_response = s.execute(sql, [user_id])
        for n in query_response:
            n_id, n_name_user = n
        if n_name_user != '0':
            return False
        else:
            return True


def check_tel(value):
    t_tel_user = ''
    user_id = str(value)
    sql = 'SELECT id, tel FROM users WHERE id_telegram=? '
    with ContextManagerSQLite('people.db') as s:
        query_response = s.execute(sql, [user_id])
        for t in query_response:
            t_id, t_tel_user = t
        if t_tel_user != '0':
            return False
        else:
            return True


def check_email(value):
    e_email_user = ''
    user_id = str(value)
    sql = 'SELECT id, email FROM users WHERE id_telegram=? '
    with ContextManagerSQLite('people.db') as s:
        query_response = s.execute(sql, [user_id])
        for e in query_response:
            e_id, e_email_user = e
        if e_email_user != '0':
            return False
        else:
            return True


def check_wishes(value):
    w_wishes_user = ''
    user_id = str(value)
    sql = 'SELECT id, wishes FROM users WHERE id_telegram=? '
    with ContextManagerSQLite('people.db') as s:
        query_response = s.execute(sql, [user_id])
        for w in query_response:
            w_id, w_wishes_user = w
        if w_wishes_user != '0':
            return False
        else:
            return True


def add_id_telegram(value):
    with ContextManagerSQLite('people.db') as s:
        sql = f'INSERT INTO users (id_telegram) VALUES (?) '
        s.execute(sql, [value])


def add_name(value):
    sql = 'UPDATE users SET name=? WHERE name=? '
    with ContextManagerSQLite('people.db') as s:
        s.execute(sql, [value, str(0)])


def add_tel(value):
    sql = 'UPDATE users SET tel=? WHERE tel=? '
    with ContextManagerSQLite('people.db') as s:
        s.execute(sql, [value, str(0)])


def add_email(value):
    sql = 'UPDATE users SET email=? WHERE email=? '
    with ContextManagerSQLite('people.db') as s:
        s.execute(sql, [value, str(0)])


def add_wishes(value):
    sql = 'UPDATE users SET wishes=? WHERE wishes=? '
    with ContextManagerSQLite('people.db') as s:
        s.execute(sql, [value, str(0)])


@bot.message_handler(commands=['start'], func=lambda message: check_id(message.chat.id))
def start_id(message):
    bot.send_message(message.chat.id, 'Hello. Enter your name.')
    add_id_telegram(message.chat.id)


@bot.message_handler(func=lambda message: check_name(message.chat.id))
def start_name(message):
    bot.send_message(message.chat.id, 'Enter your tel.')
    add_name(message.text)


@bot.message_handler(func=lambda message: check_tel(message.chat.id))
def start_tel(message):
    bot.send_message(message.chat.id, 'Enter your email.')
    add_tel(message.text)


@bot.message_handler(func=lambda message: check_email(message.chat.id))
def start_email(message):
    bot.send_message(message.chat.id, 'Enter your wishes.')
    add_email(message.text)


@bot.message_handler(func=lambda message: check_wishes(message.chat.id))
def start_wishes(message):
    bot.send_message(message.chat.id, 'Thanks.')
    add_wishes(message.text)


@bot.message_handler(func=lambda message: True)
def start_end(message):
    bot.send_message(message.chat.id, 'Hi. Your information is already in the database.')


bot.polling(none_stop=True)
