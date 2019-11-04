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


def decor(func):
    def wrapper(*args):
        print('----------------------')
        result = func(*args)
        print('----------------------')
        return result
    return wrapper


def login_user(name_surname):
    log = 0
    role = 0
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name_surname, role '
                                   'FROM students '
                                   'INNER JOIN role '
                                   'ON students.id_role=role.id')
        for u in query_response:
            (u_name_surname, u_role) = u
            if name_surname in u:
                log += 1
                if u_role == 'admin':
                    role += 1
                else:
                    role += 0
            else:
                log += 0
        return log, role


@decor
def get_all_students():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name_surname, faculty, num_group '
                                   'FROM students '
                                   'INNER JOIN students_group '
                                   'ON students.id_group=students_group.id '
                                   'INNER JOIN faculty '
                                   'ON students.id_faculty=faculty.id')
        for u in query_response:
            print(*u)


@decor
def found_from_num_student(num_student):
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name_surname, num_student '
                                   'FROM students')
        for u in query_response:
            (u_name_surname, u_num_student) = u
            if num_student in (u_name_surname, u_num_student):
                print(*u)


@decor
def get_full_info_user(name_surname):
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name_surname, num_student, faculty, num_group '
                                   'FROM students '
                                   'INNER JOIN faculty '
                                   'ON students.id_faculty=faculty.id '
                                   'INNER JOIN students_group '
                                   'ON students.id_group=students_group.id')
        for u in query_response:
            (u_name_surname, u_num_student, u_aculty, u_num_group) = u
            if name_surname in (u_name_surname, u_num_student, u_aculty, u_num_group):
                print(*u)


@decor
def found_excellence():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT name_surname, grade_student, subject_student '
                                   'FROM grade_students '
                                   'INNER JOIN subject_students '
                                   'ON grade_students.id_subject=subject_students.id '
                                   'INNER JOIN students '
                                   'ON grade_students.id_students=students.id')
        for u in query_response:
            (u_name_surname, u_grade_student, u_subject_student) = u
            if 5 in (u_name_surname, u_grade_student, u_subject_student):
                print(*u)


@decor
def add_student(name_surname, num_student, id_faculty, id_group):
    sql = 'INSERT INTO students (name_surname,  num_student, id_faculty, id_group, id_role) VALUES (?, ?, ?, ?, ?) '
    with ContextManagerSQLite('students base.db') as s:
        s.execute(sql, [name_surname, num_student, id_faculty, id_group, '2'])
    print('Student added')


def change_name_surname(mutable_user):
    name, surname = input('Enter new student name and surname\n').split()
    mutable_user1 = name.capitalize() + ' ' + surname.capitalize()
    sql = f'UPDATE students SET name_surname = "{mutable_user1}" WHERE name_surname = "{mutable_user}" '
    with ContextManagerSQLite('students base.db') as s:
        s.execute(sql)
    return mutable_user1


def change_student_number(mutable_user):
    new_num_student = input('Enter new student name and surname\n')
    sql = f'UPDATE students SET num_student = "{new_num_student}" WHERE name_surname = "{mutable_user}" '
    with ContextManagerSQLite('students base.db') as s:
        s.execute(sql)


def change_student_group(mutable_user, id_group):
    sql = f'UPDATE students SET id_group = "{id_group}" WHERE name_surname = "{mutable_user}" '
    with ContextManagerSQLite('students base.db') as s:
        s.execute(sql)


@decor
def get_all_id_students():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT id, name_surname FROM students')
        all_id = []
        for u in query_response:
            (u_id, u_name_surname) = u
            all_id += [str(u_id)]
            print(f'{u_id} - {u_name_surname}')
    return all_id


@decor
def get_all_id_subject():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT id, subject_student FROM subject_students')
        all_id = []
        for u in query_response:
            (u_id, u_subject_student) = u
            all_id += [str(u_id)]
            print(f'{u_id} - {u_subject_student}')
    return all_id


@decor
def get_all_id_group():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT id, num_group FROM students_group')
        all_id = []
        for u in query_response:
            (u_id, u_num_group) = u
            all_id += [str(u_id)]
            print(f'{u_id} - {u_num_group}')
    return all_id


@decor
def get_all_id_faculty():
    with ContextManagerSQLite('students base.db') as s:
        query_response = s.execute('SELECT id, faculty FROM faculty')
        all_id = []
        for u in query_response:
            (u_id, u_faculty) = u
            all_id += [str(u_id)]
            print(f'{u_id} - {u_faculty}')
    return all_id


def add_grade_student(grade_student, id_student, id_subject):
    sql = 'INSERT INTO grade_students (grade_student, id_students, id_subject) VALUES (?, ?, ?)'
    with ContextManagerSQLite('students base.db') as s:
        s.execute(sql, [str(grade_student), str(id_student), str(id_subject)])


while True:
    com1 = input('1 - Student\n'
                 '0 - Exit\n')
    if com1 == '1':
        name_user, surname_user = input('Enter you name and surname:').split()
        name_surname_user = name_user.capitalize() + ' ' + surname_user.capitalize()
        login = login_user(name_surname_user)

        if login == (1, 0):
            while True:
                com2 = input('1 - List of Excellence\n'
                             '2 - List of all students\n'
                             '3 - Find by student number\n'
                             '4 - Full user information\n'
                             '0 - Exit\n')

                if com2 == '1': # List of Excellence
                    found_excellence()
                elif com2 == '2': # List of all students
                    get_all_students()
                elif com2 == '3': # Find by student number
                    found_from_num_student(input('Enter num student:'))
                elif com2 == '4': # Full user information
                    get_full_info_user(name_surname_user)
                elif com2 == '0':
                    break
                else:
                    print('Wrong choice\n')

        elif login == (1, 1):
            while True:
                com3 = input('1 - List of Excellence\n'
                             '2 - List of all students\n'
                             '3 - Find by student number\n'
                             '4 - Full user information\n'
                             '5 - Introduce a new student\n'
                             '6 - Change student information\n'
                             '7 - Grade a student\n'
                             '0 - Exit\n')

                if com3 == '1': # List of Excellence
                    found_excellence()

                elif com3 == '2': # List of all students
                    get_all_students()

                elif com3 == '3': # Find by student number
                    found_from_num_student(input('Enter num student:'))

                elif com3 == '4': # Full user information
                    get_full_info_user(name_surname_user)

                elif com3 == '5': # Introduce a new student
                    name_surname = input('Name and surname a new student:')
                    num_student = input('Student number:')

                    while True:
                        id_facultys = get_all_id_faculty()
                        id_faculty = input('Faculty a new student:\n')
                        if id_faculty in id_facultys:
                            break
                        else:
                            print('Wrong choice faculty\n')

                    while True:
                        id_groups = get_all_id_group()
                        id_group = input('Enter group student:\n')
                        if id_group in id_groups:
                            break
                        else:
                            print('Wrong choice group\n')
                    add_student(name_surname, num_student, id_faculty, id_group)
                elif com3 == '6': # Change student information

                    while True:
                        com5 = input('Name and surname of the student to be replaced\n'
                                     '0 - Exit\n')

                        if com5 != '0':
                            name, surname = com5.split()
                            mutable_user = name.capitalize() + ' ' + surname.capitalize()
                            login1 = login_user(mutable_user)

                            if login in (1, 0) or (1, 1):

                                while True:
                                    com4 = input('What are we changing\n'
                                                 '1 - Name and surname student\n'
                                                 '2 - Student number\n'
                                                 '3 - Student group\n'
                                                 '0 - Exit\n')

                                    if com4 == '1': # Name and surname student
                                        mutable_user = change_name_surname(mutable_user)
                                    elif com4 == '2': #Student number
                                        change_student_number()
                                    elif com4 == '3': # Student group

                                        while True:
                                            id_group = input('Enter group student:\n'
                                                             '1 - 901\n'
                                                             '2 - 941\n'
                                                             '3 - 911\n')

                                            if id_group in ('1', '2', '3'):
                                                change_student_group(mutable_user, id_group)
                                                break
                                            else:
                                                print('Wrong choice group\n')

                                    elif com4 == '0':
                                        break
                                    else:
                                        print('Wrong choice group\n')

                            else:
                                print('Student not found\n')

                        elif com5 == '0':
                            break
                        raise ValueError

                elif com3 == '7': # Grade a student
                    id_students = get_all_id_students()
                    while True:
                        com6 = input('Enter id student\n'
                                     '0 - Exit\n')
                        if com6 in id_students:
                            id_student = com6
                            break
                        elif com6 == '0':
                            break
                        else:
                            print('Wrong choice\n')
                    id_subjects = get_all_id_subject()
                    while True:
                        com7 = input('Enter id subject\n'
                                     '0 - Exit\n')
                        if com7 in id_subjects:
                            id_subject = com7
                            break
                        elif com7 == '0':
                            break
                        else:
                            print('Wrong choice\n')
                    while True:
                        grade_student = int(input('Enter grade student\n'
                                                  'min - 0\n'
                                                  'max - 5\n'))
                        if 0 <= grade_student <= 5:
                            add_grade_student(grade_student, id_student, id_subject)
                            break
                        else:
                            print('Wrong choice\n'
                                  'min - 0\n'
                                  'max - 5\n')

                elif com3 == '0':
                    break
                else:
                    print('Wrong choice\n')

        elif login == (0, 0):
            print('Student not found\n')

    elif com1 == '0':
        break
    else:
        print('Wrong choice\n')