import sqlite3

from sqlite_utils.cli import rows

# def row():
#     pass
#
#
# def delete_an_item_from_table():
#     connection = sqlite3.connect('rss.sqlite')
#     cursor_object = connection.cursor()
#     cursor_object.execute('DELETE from RSSentries WHERE rowid = 500')
#     print(row[500])
#     connection.commit()
#     connection.close()

# def del_and_update():
#     conn = sqlite3.connect('rss.sqlite')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM RSSentries;')
#     print('We have deleted', cursor.rowcount, 'records from the table.')
#     conn.commit()
#     conn.close()


# delete_an_item_from_table()
global sqliteConnection


def read_sqlite_table():
    global sqliteConnection
    try:
        sqliteConnection = sqlite3.connect('testonly.sqlite')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # sqlite_select_query = """DROP TABLE IF EXISTS work"""
        sqlite_select_query = """SELECT * from work"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            # print("Email: ", row[2])
            # print("JoiningDate: ", row[3])
            # print("Salary: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


read_sqlite_table()
