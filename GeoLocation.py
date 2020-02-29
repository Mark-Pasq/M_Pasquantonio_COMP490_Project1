# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: GeoLocation.py
"""
This file handles the ability to get geolocation on the locations of the jobs
in the database.  It will give addresses and latitudinal
"""

import sqlite3
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="GoogleMaps")
location = geolocator.geocode("23 Winding Way Plymouth Massachusetts")
print(location.address)
print((location.latitude, location.longitude))


global sqlite_connection


def query_job_locations():
    try:
        global sqlite_connection
        sqlite_connection = sqlite3.connect('jobdemo.sqlite')
        cursor = sqlite_connection.cursor()
        print("Connected to SQLite")
        sql_select_query = """select * from hardcode_github_jobs"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        for row in records:
            print('============================')
            print("company = ", row[4])
            print("location  = ", row[6])
            print("description  = ", row[7])
            print("title  = ", row[8])

            sqlite_connection.commit()
            cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


query_job_locations()


# def find_lat_long_of_locations():
#     global hardcore_github_jobs
#     geolocator = Nominatim(user_agent="GoogleMaps", timeout=5)
#     conn = sqlite3.connect('jobdemo.sqlite[2]')
#     cur = conn.cursor()
#     # cur.execute('SELECT title FROM hardcode_github_jobs')
#     print('The system is up and running')
#     try:
#         cur.execute("ALTER TABLE hardcode_github_jobs ADD COLUMN latitude DECIMAL(9,6)")
#         cur.execute("ALTER TABLE hardcode_github_jobs ADD COLUMN longitude DECIMAL(9,6)")
#     except:
#         rows = cur.fetchall()
#         for data in rows:
#             location = geolocator.geocode(data)
#
#             print("Already added columns, skipping that part")
#             hardcore_github_jobs = hardcore_github_jobs.select()
#
#             for hardcore_github_jobs in hardcore_github_jobs:
#                 print(hardcore_github_jobs.full_address())
#
#             print(location.address)
#             print(location.latitude, location.longitude)  #
#
#             print('missing entry found')
#             print('=========================================')
#             print("The total rows in the database is:  ", len(rows))
#             print('=========================================')
#
#
# find_lat_long_of_locations()
