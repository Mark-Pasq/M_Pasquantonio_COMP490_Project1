#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.  This function
does not work as expected.  It was supposed to be added to the results of the .JSON download
from Sprint 1.  When the green 'run' button is clicked, the function will print the results
of the query and populate a database table.
"""

import feedparser
import sqlite3
from geopy import Nominatim
import time

geo_locator = Nominatim(user_agent='GoogleMaps')

parsed_feed = feedparser.parse("https://stackoverflow.com/jobs/feed")
cxn = sqlite3.connect('rss.sqlite')
cur = cxn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS RSS_pull(title TEXT, link TEXT, description TEXT, location TEXT,
                    latitude REAL, longitude REAL );''')
cur.execute('DELETE FROM RSS_pull;')  # clears the table before running, error arose on unique id of job links on
# rerun
# # position of opening square bracket
# first_pos = string.rfind("(")
# # position of closing square bracket
# last_pos = string.rfind(")")
# # printing the text between two square brackets
# print(string[first_pos + 1: last_pos])  # Prints output 'How'
for entries in parsed_feed['items']:
    print(entries)
    title = entries.title
    link = entries.link
    description = entries.description
    print(link)
    print(title)
    print(description)
    string = title
    first_pos = string.rfind("(")
    # position of closing square bracket
    last_pos = string.rfind(")")
    # printing the text between two square brackets
    temp_location_holder = geo_locator.geocode(string[first_pos + 1: last_pos])
    time.sleep(.5)
    with cxn:
        try:
            cur.execute('''INSERT INTO main.RSS_pull (title, link, description, location, latitude, longitude) VALUES
                        (?, ?, ?, ?, ?, ?);''', (entries['title'], entries['link'], entries['description'],
                        string[first_pos + 1: last_pos], temp_location_holder.latitude, temp_location_holder.longitude))
        except AttributeError:
            cur.execute('''INSERT INTO main.RSS_pull (title, link, description, location, latitude, longitude) VALUES
                        (?, ?, ?, ?, ?, ?);''', (entries['title'], entries['link'], entries['description'],
                        string[first_pos + 1: last_pos], 0.0, 0.0))
# Commit your changes to the program
cxn.commit()
# Close the cursor_object
cur.close()
