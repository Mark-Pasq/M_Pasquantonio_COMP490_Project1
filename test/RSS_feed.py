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
import feedparser

# geolocator = Nominatim(user_agent="GoogleMaps")
# cnx = sqlite3.connect('rss.sqlite')
# cur = cnx.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS latlong_locations(latitude TEXT, longitude TEXT);''')
# cur.execute('''SELECT description FROM RSSentries''')
global num_of_rows
myfeed = feedparser.parse("http://stackoverflow.com/jobs/feed")
for item in myfeed['items']:

    link = item.link
    title = item.title
    description = item.description

    # time.sleep(.5)
    # location = geolocator.geocode(data)
    # try:
    db = sqlite3.connect('rss.sqlite')
    with db:
        cur = db.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS RSSentries (link TEXT Primary Key, title TEXT, description TEXT);")
        cur.execute(''' INSERT INTO RSSentries(link, title, description) VALUES (?,?, ?)''',
                    (item["link"], item["title"], item["description"]))
        # except AttributeError:
        #     cur.execute(''' INSERT INTO latlong_locations( latitude, longitude) VALUES (?,?)''', ("remote", "remote"))
        #     print(location.latitude, location.longitude)
        db.commit()
        cur.close()

######################################################################################################################

#
# def find_lat_long_of_locations():
#     geolocator = Nominatim(user_agent="GoogleMaps", timeout=5)
#     cxn = sqlite3.connect('jobdemo.sqlite')
#     cur = cxn.cursor()
#     cur.execute(f"CREATE TABLE IF NOT EXISTS latlong_locations(id TEXT, latitude REAL, longitude REAL);")
#     cur.execute('SELECT location FROM github_jobs')
#
#     rows = cur.fetchall()
#     for data in rows:
#         location = geolocator.geocode(data)
#         cur.execute('INSERT INTO latlong_locations(id, latitude, longitude) VALUES (?, ?, ?)',
#                     (data['id'], data['latitude'], data['longitude']))
#         try:
#
#             print(location.address)
#             print(location.latitude, location.longitude)
#
#         except AttributeError:
#             print('missing entry found')
#     print('=========================================')
#     print("The total rows in the database is:  ", len(rows))
#     print('=========================================')
#
#
# find_lat_long_of_locations()
