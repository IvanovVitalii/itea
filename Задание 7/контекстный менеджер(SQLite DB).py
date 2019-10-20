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


# login = input('enter the login')
# password = input('enter the pass')
# sql = 'INSERT INTO user (login, password) VALUES (?, ?)'

with ContextManagerSQLite('people123.db') as s:
    # query_response = s.execute(sql, [login, password])
    query_response1 = s.execute('SELECT * FROM user')
    for u in query_response1:
        (u_id, u_login, u_password) = u
        print(*u)

