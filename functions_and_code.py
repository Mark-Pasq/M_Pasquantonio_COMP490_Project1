import sqlite3

from sqlite_utils.cli import rows


def delete_an_item_from_table():
    connection = sqlite3.connect('rss.sqlite')
    cursor_object = connection.cursor()
    for row in rows:
        cursor_object.execute('DELETE from RSSentries WHERE rowid=500')
        print(row[500])
    connection.commit()
    connection.close()
