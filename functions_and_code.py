import sqlite3


# def delete_an_item_from_table():
#     connection = sqlite3.connect('rss.sqlite')
#     cursor_object = connection.cursor()
#     for row in rows:
#         cursor_object.execute('DELETE rowid from RSSentries WHERE rowid=500')
#         print(row[500])
#     connection.commit()
#     connection.close()

def del_and_update():
    conn = sqlite3.connect('rss.sqlite')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM RSSentries;')
    print('We have deleted', cursor.rowcount, 'records from the table.')

    conn.commit()
    conn.close()
    # sqlite = 'DELETE FROM RSSentries'
    # cur = conn.cursor()
    # cur.execute(sqlite)
    # conn.commit()


del_and_update()
