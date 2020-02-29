#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.
"""
#
################################################################################################################
import sqlite3
import time
from geopy.geocoders import Nominatim


# geolocator = Nominatim(user_agent="GoogleMaps")
# cnx = sqlite3.connect('rss.sqlite')
# cur = cnx.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS latlong_locations(latitude TEXT, longitude TEXT);''')
# cur.execute('''SELECT description FROM RSSentries''')
#
# rows = cur.fetchall()
# for data in rows:
#
#     time.sleep(.5)
#     location = geolocator.geocode(data)
#     try:
#         print(location.latitude, location.longitude)
#         cur.execute(''' INSERT INTO latlong_locations( latitude, longitude) VALUES (?,?)''',
#                     (location.latitude, location.longitude))
#     except AttributeError:
#         cur.execute(''' INSERT INTO latlong_locations( latitude, longitude) VALUES (?,?)''', ("remote", "remote"))


######################################################################################################################


def find_lat_long_of_locations():
    geolocator = Nominatim(user_agent="GoogleMaps", timeout=5)
    cxn = sqlite3.connect('jobdemo.sqlite[2]')
    cur = cxn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS latlong_locations(id TEXT, latitude REAL, longitude REAL);")
    cur.execute('SELECT location FROM hardcode_github_jobs')

    rows = cur.fetchall()
    for data in rows:
        location = geolocator.geocode(data)
        cur.execute('INSERT INTO latlong_locations(latitude, longitude) VALUES (?, ?)',
                    (data['latitude'], data['longitude']))
        try:

            print(location.address)
            print(location.latitude, location.longitude)

        except AttributeError:
            print('missing entry found')
    print('=========================================')
    print("The total rows in the database is:  ", len(rows))
    print('=========================================')


find_lat_long_of_locations()
