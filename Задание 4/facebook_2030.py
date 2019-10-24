import re
import shelve
from datetime import datetime


class Users:

    USERSINFO = 'users'
    POSTS = 'posts'

    def __init__(self, login=0, password=0, date_registration=0, born=0, post=0):
        self._login = login
        self._password = password
        self._date_registration = date_registration
        self._born = born
        self._post = post

    def get_user_info(self):
        with shelve.open(Registration.POSTS) as db:
            pos = db.get(self._login)
        return f'Логин: {self._login} \nДата регистрации: {self._date_registration} \nДень рождения:{self._born} \n' \
               f'Ваши посты:{pos}'

    def save_info(self):
        with shelve.open(Registration.USERSINFO) as db:
            db[self._login] = [self._login, self._password, self._date_registration, self._born]
        with shelve.open(Registration.POSTS) as db:
            db[self._login] = []

    def open_info(self):
        with shelve.open(Registration.USERSINFO) as db:
            return db.get(self._login)

    def set_born(self, value):
        with shelve.open(Registration.USERSINFO, writeback=True) as db:
            db[self._login][3] = value
            print(db.get(self._login))

    def add_post(self, post=0):
        self._post = input('Ваш пост:')
        date_post = datetime.today().strftime("%d %m %Y")
        with shelve.open(Registration.POSTS) as db:
            db[self._login] += [self._post + '/' + date_post]
        with shelve.open(Registration.POSTS) as db:
            return (db.get(self._login))[-1:]

    def get_admin_info_users(self):
        with shelve.open(Registration.USERSINFO) as db:
            users = list(db.keys())
        for i in users:
            log = i
            with shelve.open(Registration.USERSINFO) as db:
                dat = db.get(i)[2]
                bor = db.get(i)[3]
            print(f'Логин: {log} \nДата регистрации: {dat} \nДень рождения:{bor}')
            print()

    def get_admin_posts_users(self):
        with shelve.open(Registration.POSTS) as db:
            users = list(db.keys())
        for i in users:
            log = i
            with shelve.open(Registration.POSTS) as db:
                pos = db.get(i)
            print(f'Логин: {log} \nПосты: {pos}')
            print()


class Registration(Users):

    def registration(self, login=0, password=0, date_registration=0, born=0):
        self._login = input('Введите логин:')
        while True:
            with shelve.open(Registration.USERSINFO) as db:
                log = self._login in db
            if log:
                self._login = input('Логин занят, введите другой:')
            else:
                break
        password1 = input('Пароль. минимум 6 символов:')
        while True:
            if len(password1) < 6:
                password1 = input('Ошибка: Минимум 6 символов:')
            elif re.search(r'[A-Z]', password1):
                if re.search(r'[0-9]', password1):
                    self._password = input('Повторите пароль:')
                    if self._password == password1:
                        print('Пароль принят.')
                        break
                    else:
                        print('Ввод неверный.')
                        password1 = self._password
            else:
                password1 = input('Должен содержать верхний регистр и цифры:')
        self._date_registration = datetime.today().strftime("%d %m %Y")
        self._born = input('Дата вашего рождения в формате dd mm yyyy')
        return login, password, date_registration, born


class Authorization(Registration):

    def authorization(self, login=0, password=0, date_registration=0, born=0, post=0):
        while True:
            self._login = input('Введите логин:')
            with shelve.open(Registration.USERSINFO) as db:
                log = self._login in db
            if log:
                self._password = input('Введите пароль:')
                with shelve.open(Registration.USERSINFO) as db:
                    passw = db[self._login][1]
                if self._password == passw:
                    print('Вы вошли')
                    with shelve.open(Registration.USERSINFO) as db:
                        self._date_registration = db[self._login][2]
                        self._born = db[self._login][3]
                    with shelve.open(Registration.POSTS) as db:
                        self._post = db.get(self._login)
                    break
                else:
                    print('Пароль не верный')
            else:
                print('Логин не найден')
        return login, password, date_registration, born, post


while True:
    com = int(input('1 - Регистрация, 2 - Войти 0 - Выход:'))
    if com == 1:
        user = Registration()
        user.registration()
        user.save_info()
        print('Вы зарегестрированны')
        print(user.open_info())
    elif com == 2:
        user = Authorization()
        user.authorization()
        while True:
            com2 = int(input('1 - Просмотр ваших данных, '
                             '2 - Изменить дату рождения, '
                             '3 - Опубликовать пост, '
                             '4 - Админ, '
                             '0 - Выход'))
            if com2 == 1:
                print(user.get_user_info())
            elif com2 == 2:
                user.set_born(input('Введите дату рождения(dd mm yyyy)'))
            elif com2 == 3:
                print(user.add_post())
            elif com2 == 4:
                admin_password = input('Пароль админа:')
                while True:
                    if admin_password == '1111': #админ пароль - 1111
                        com3 = int(input('1 - Инфо пользователей, 2 - Посты пользователей, 0 - Выйти из админки'))
                        if com3 == 1:
                            user.get_admin_info_users()
                        elif com3 == 2:
                            user.get_admin_posts_users()
                        elif com3 == 0:
                            break
                        else:
                            com3 = input('Неверный ввод. Повторите')
                    else:
                        print('В доступе отказано!')
                        break
            elif com2 == 0:
                break
            else:
                com2 = int(input('Неверный ввод. Повторите.'))
    elif com == 0:
        break
    else:
        print('Неверный ввод. Повторите.')