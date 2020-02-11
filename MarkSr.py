import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('mark_sr.sqlite')
        return conn
    except Error:
        print(Error)


def sql_table():
    conn = sqlite3.connect('mark_sr.sqlite')
    cursor_obj = conn.cursor()
    cursor_obj.execute(
        'CREATE TABLE IF NOT EXISTS ringo(id integer PRIMARY KEY, name text, salary real, '
        'department text, position text, hireDate text)')

    conn.commit()


def count_number_of_rows():
    pass


def count_number_of__rows():
    conn = sqlite3.connect('mark_sr.sqlite')
    cursor_obj = conn.cursor()
    cursor_obj.execute('''SELECT count(*) from ringo''')
    rowcount = cursor_obj.fetchall()[0]
    print(rowcount)

    def main():
        sql_connection()
        sql_table()
        count_number_of_rows()

        if __name__ == '__main__':
            main()
