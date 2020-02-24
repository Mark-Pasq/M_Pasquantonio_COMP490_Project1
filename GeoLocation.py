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

global geolocator


geolocator = Nominatim(user_agent="GoogleMaps")
location = geolocator.geocode("23 Winding Way Plymouth Massachusetts")
print(location.address)
print((location.latitude, location.longitude))


def find_lat_long_of_locations():
    geolocator = Nominatim(user_agent="GoogleMaps", timeout=5)
    conn = sqlite3.connect('jobdemo.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT title FROM hardcode_github_jobs')
    rows = cur.fetchall()
    for data in rows:
        location = geolocator.geocode(data)
        cur.execute('INSERT INTO hardcode_github_jobs (latitude, longitude) VALUES (?, ?)',
                    (data['latitude'], data['longitude']))
        try:
            print(location.address)
            print(location.latitude, location.longitude)  #
        except AttributeError:
            print('missing entry found')
    print('=========================================')
    print("The total rows in the database is:  ", len(rows))
    print('=========================================')


find_lat_long_of_locations()

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
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print('============================')
            print("company = ", row[4])
            print("location  = ", row[6])
            print("description  = ", row[7])
            print("title  = ", row[8])
            cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    # finally:
    #     if sqlite_connection:
    #         sqlite_connection.close()
    #         print("The SQLite connection is closed")


query_job_locations()
