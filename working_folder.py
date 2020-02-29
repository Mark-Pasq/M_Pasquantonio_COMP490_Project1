# import sqlite3

# from sqlite_utils.cli import rows
#
# # def row():
# #     pass
# #
# #
# # def delete_an_item_from_table():
# #     connection = sqlite3.connect('rss.sqlite')
# #     cursor_object = connection.cursor()
# #     cursor_object.execute('DELETE from RSSentries WHERE rowid = 500')
# #     print(row[500])
# #     connection.commit()
# #     connection.close()


# # def del_and_update():
# #     conn = sqlite3.connect('rss.sqlite')
# #     cursor = conn.cursor()
# #     cursor.execute('DELETE FROM RSSentries;')
# #     print('We have deleted', cursor.rowcount, 'records from the table.')
# #     conn.commit()
# #     conn.close()
#
#
# # delete_an_item_from_table()


# global sqliteConnection
#
#
# def read_sqlite_table():
#     global sqliteConnection
#     # try:
#     sqliteConnection = sqlite3.connect('jobdemo.sqlite[2]')
#     cursor = sqliteConnection.cursor()
#     print("Connected to SQLite")
#
#         # sqlite_select_query = """DROP TABLE IF EXISTS work"""
#     sqlite_select_query = """SELECT * from hardcode_github_jobs"""
#     cursor.execute(sqlite_select_query)
#     records = cursor.fetchall()
#     print("printing each row")
#     for row in records:
#         print("------------------------------------------")
#         print("Id: ", row[0])
#         print("Job Type: ", row[1])
#         print("Job Title: ", row[4])
#         print("Job Location: ", row[6])
#         print("Created Date", row[3])
#         print("Printing each row now!")
#         print("Total rows are:  ", len(records))
#         print("\n")
#
#         cursor.close()
# read_sqlite_table()
#
#

# except sqlite3.Error as error:
#     print("Failed to read data from sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")


#####################################################
# geolocator = Nominatim(user_agent="GoogleMaps")
# location = geolocator.geocode("Munchen")
# print(location.address)
# print((location.latitude, location.longitude))

#####################################################
import sqlite3
import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="GoogleMaps")
cnx = sqlite3.connect('jobdemo.sqlite[2]')
cur = cnx.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS main.latlong_locations(id int primary key, latitude REAL, longitude REAL);''')
cur.execute('''SELECT location FROM main.hardcode_github_jobs''')

rows = cur.fetchall()
counter = 0
for data in rows:
    counter = counter + 1
    time.sleep(.5)
    location = geolocator.geocode(data)
    # if counter > 5:
    # break
    try:
        print(location.latitude, location.longitude)
        cur.execute(''' INSERT INTO main.latlong_locations( latitude, longitude) VALUES (?,?)''',
                    (location.latitude, location.longitude))
    except AttributeError:
        cur.execute(''' INSERT INTO main.latlong_locations( latitude, longitude) VALUES (?,?)''', ("remote", "remote"))

        cnx.commit()
        # cur.close()

####################################################################################################################

# def query_dates():
#     cxn = sqlite3.connect('jobdemo.sqlite[2]')
#     cursor = cxn.cursor()
#
#     cursor.execute(
#         '''SELECT created_at FROM hardcode_github_jobs WHERE created_at >= 'Wed Jan 01 00:00:00 UTC 2020' and created_at <= 'Thu Feb 27 00:00:00 UTC 2020'; ''')
#     table = cursor.fetchall()
#     for items in table:
#         print(items)
#
#     cxn.commit()
#     cursor.close()
#
#
# query_dates()
