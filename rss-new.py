#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.  This function
does not work as expected.  It was supposed to be added to the results of the .JSON download
from Sprint 1.  When the green 'run' button is clicked, the function will print the results
of the query and populate a database table.  It doesn't work for me.
"""

import feedparser
import sqlite3
from geopy import Nominatim
import time

geo_locator = Nominatim(user_agent='GoogleMaps')

parsed_feed = feedparser.parse("https://stackoverflow.com/jobs/feed")
cxn = sqlite3.connect('job_demo.sqlite')
cur = cxn.cursor()


def makeRSSTable():
    cur.execute(
        'DELETE FROM RSS_feed;')  # clears the table before running, error arose on unique id of job links on # rerun
    cur.execute(''' CREATE TABLE IF NOT EXISTS RSS_feed(id, type TEXT, url TEXT, created_at TEXT, company TEXT,
    location TEXT, title TEXT, latitude REAL, longitude REAL);''')

    for entries in parsed_feed['items']:
        print(entries)
        id = entries.id
        title = entries.title
        location = entries.location
        created_at = entries.published
        company = entries.author
        description = entries.description
        print(title)
        print(location)
        print(description)
        # print(type(company))
        string = title
        first_pos = string.rfind("(")
        # position of closing square bracket
        last_pos = string.rfind(")")
        # printing the text between two square brackets
        temp_location_holder = geo_locator.geocode(string[first_pos + 1: last_pos])
        time.sleep(.5)
        with cxn:
            try:
                cur.execute('''INSERT INTO RSS_feed (id, type, url, created_at, company, location, title, latitude,
                                longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (entries['id'], entries['type'],
                                entries['link'], entries['created_at'], entries['company'], string[first_pos + 1: last_pos],
                                entries['title'], temp_location_holder.latitude, temp_location_holder.longitude))

            except AttributeError:
                cur.execute('''INSERT INTO RSS_feed (id, type, url, created_at, company, location, title, latitude,
                                longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (entries['id'], entries['type'],
                                entries['link'], entries['created_at'], entries['company'], string[first_pos + 1: last_pos],
                                entries['title'], title, 0.0, 0.0))


def CopyTables():
    cur.execute('''DELETE FROM RSS_feed''')
    cur.execute(''' CREATE TABLE IF NOT EXISTS RSS_feed(id, type, url , created_at, company, location , title,
    latitude, longitude);''')
    cur.execute('''INSERT INTO github_jobs SELECT * FROM RSS_feed''')


def combineTables():
    cur.execute(''' INSERT INTO github_jobs SELECT * FROM RSS_feed;''')
    cxn.commit()


CopyTables()
combineTables()
# Commit your changes to the program
cxn.commit()
# Close the cursor_object
cxn.close()
