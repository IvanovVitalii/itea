import sqlite3


class ContextManagerSQLite:
    def __init__(self, file):
        self._file = file

    def __enter__(self):
        self._conn = sqlite3.connect(self._file)
        self._conn.row_factory = sqlite3.Row
        return self._conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.commit()
        self._conn.close()


def login(name, surname):
    u = []
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name, surname FROM students')
        for u_id in query_response:
            u += u_id
        if name and surname in u:
            log = 1
        else:
            log = 0
        return log


def get_all_students():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name, surname, faculty, num_group '
                                    'FROM students '
                                    'INNER JOIN students_group '
                                    'ON students.id_group=students_group.id '
                                    'INNER JOIN faculty '
                                    'ON students.id_faculty=faculty.id')
        for u in query_response:
            (u_name) = u
            print(*u)


def found_from_num_student(num_student):
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name, surname, num_student '
                                   'FROM students')
        for u in query_response:
            (u_id) = u
            if num_student in (u_id):
                print(*u)


while True:
    com1 = input('1 - Student\n'
                 '0 - Exit\n')
    if com1 == '1':
        name_user, surname_user = input('Enter you name and surname:').split()
        login = login(name_user, surname_user)
        print(login)

        if login != 0:
            while True:
                com2 = input('1 - Список отличников\n'
                             '2 - Список всех студентов\n'
                             '3 - Найти по номеру студенческого\n'
                             '4 - Полная информация пользователя\n'
                             '0 - Exit\n')
                if com2 == '1':
                    break
                elif com2 == '2':
                    get_all_students()
                elif com2 == '3':
                    found_from_num_student(input('Enter num student'))
                elif com2 == '4':
                    with ContextManagerSQLite('students base.db') as s:
                        u = []
                        query_response = s.execute('SELECT name, surname FROM students')
                        for u_id in query_response:
                            u += u_id
                        if name_user and surname_user in u:
                            print(*u)
                elif com2 == '0':
                    break

            # break
    elif com1 == '0':
        break




# with ContextManagerSQLite('students base.db') as s:
#     name = input('name student:')
#     surname = input('surname student:')
#     faculty = input('faculty student:')
#     student_number = input('student_number:')
#     group = input('group student:')
#     sql = 'INSERT INTO user (name, surname, faculty) VALUES (?, ?, ?, ?, ?)'
#     query_response = s.execute(sql, [name, surname, faculty, student_number, group])



# with ContextManagerSQLite('students base.db') as s:
#     # query_response = s.execute(sql, [login, password])
#     query_response = s.execute('SELECT * FROM students')
#     for s in query_response:
#         (s_id) = s
#         if 'Bob' and 'Jones' in (s_id):
#             print(*s)


# name, surname = input('Enter you name and surname:').split()
# with ContextManagerSQLite('students base.db') as s:
#     query_response = s.execute('SELECT name, surname, student_number, faculty, num_group '
#                                 'FROM students INNER JOIN students_group '
#                                 'ON students.id_group=students_group.id '
#                                 'INNER JOIN faculty '
#                                 'ON students.id_faculty=faculty.id')
#     for u in query_response:
#         (u_id) = u
#         if name and surname in u:
#             print(*u)
#             continue
#         else:
#             break
