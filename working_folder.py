import sqlite3

from sqlite_utils.cli import rows


def row():
    pass


def delete_an_item_from_table():
    connection = sqlite3.connect('rss.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute('DELETE from RSSentries WHERE rowid = 500')
    print(row[500])
    connection.commit()
    connection.close()

# def del_and_update():
#     conn = sqlite3.connect('rss.sqlite')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM RSSentries;')
#     print('We have deleted', cursor.rowcount, 'records from the table.')
#     conn.commit()
#     conn.close()


delete_an_item_from_table()
