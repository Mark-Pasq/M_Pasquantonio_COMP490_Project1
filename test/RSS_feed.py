#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.
"""
import sqlite3
import feedparser
from geopy import Nominatim

global num_of_rows

myfeed = feedparser.parse("https://stackoverflow.com/jobs/feed")
for item in myfeed['items']:
    link = item.link
    title = item.title
    description = item.description

    print(link)
    print(title)
    print(description)

    db = sqlite3.connect('rss.sqlite')
    with db:
        cur = db.cursor()
        cur.execute(f'''INSERT INTO main.RSSentries(link, title, description)
                        VALUES (?, ?, ?);''', (item['link'], item['title'], item['description']))


def find_lat_long_of_locations():
    geolocator = Nominatim(user_agent="GoogleMaps", timeout=5)
    conn = sqlite3.connect('rss.sqlite')
    c_u = conn.cursor()
    cur.execute('SELECT title FROM RSSentries')

    rows = c_u.fetchall()
    for data in rows:
        location = geolocator.geocode(data)
        # cur.execute('INSERT INTO hardcode_github_jobs(latitude, longitude) VALUES (?, ?)',
        #             data['latitude'], data['longitude'])
        try:

            print(location.address)
            print(location.latitude, location.longitude)

        except AttributeError:
            print('missing entry found')
    print('=========================================')
    print("The total rows in the database is:  ", len(rows))
    print('=========================================')


find_lat_long_of_locations()
