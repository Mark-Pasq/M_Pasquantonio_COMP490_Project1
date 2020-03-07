import sqlite3
import datetime
import jobs


# def row():
#     pass
#
#
# def delete_an_item_from_table():
#     try:
#         connection = sqlite3.connect('rss.sqlite')
#         cursor_object = connection.cursor()
#         print("I am connected to SQLite!")
#
#         sql_delete_query = f'''DELETE FROM main.RSSentries WHERE rowid >= 500'''
#         cursor_object.execute(sql_delete_query)
#         connection.commit()
#         if "rowid <= 500":
#             print("There isn't enough files to do the job")
#         else:
#             print("The record(s) have been successfully deleted!")
#         cursor_object.close()
#
#     except sqlite3.Error as error:
#         print("I have failed to delete the record(s) from the table as you requested", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("The SQLite connection has been closed!")
#
#
# delete_an_item_from_table()
#

############################################################################################
# def del_and_update():
#     conn = sqlite3.connect('rss.sqlite')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM RSSentries;')
#     print('We have deleted', cursor.rowcount, 'records from the table.')
#     conn.commit()
#     conn.close()

##############################################################################################

# def queryDateRange():
#     cxn = sqlite3.connect('job_demo.sqlite')
#     cur = cxn.cursor()
#     cur.execute(
#         "SELECT created_at FROM github_jobs WHERE created_at BETWEEN '2020-01-01' AND '2020-03-06' ORDER BY created_at")
#     rows = cur.fetchall()
#     for items in rows:
#         # time.sleep(.5)
#         print(items)
#
#     cxn.commit()
#     cur.close()
#
#     queryDateRange()

def query_location():
    cxn = sqlite3.connect('job_demo.sqlite')
    cur = cxn.cursor()
    cur.execute("SELECT * FROM lat_long_locations")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cxn.commit()
    cur.close()


query_location()

###################################################################################################################
