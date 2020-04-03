#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_jobs.py
"""
This file handles the parsing of an rss feed.  It also populates the table.  This function
does not work as expected.  It was supposed to be added to the results of the .JSON download
from Sprint 1.  When the green 'run' button is clicked, the function will print the results
of the query and populate a database table.  It doesn't work for me.
"""
from geopy import Nominatim
import feedparser
import sqlite3
import time

geo_locator = Nominatim(user_agent='GoogleMaps')

my_rss_feed = feedparser.parse("https://stackoverflow.com/jobs/feed")
cxn = sqlite3.connect('job_demo.sqlite')
cur = cxn.cursor()
cur.execute(f'''DELETE FROM rss_feed;''')  # clears the table before running.
cur.execute(f''' CREATE TABLE IF NOT EXISTS rss_feed(id TEXT, type TEXT, link TEXT, company TEXT, location TEXT,
                title TEXT, description TEXT, latitude REAL, longitude REAL);''')
cxn.commit()

for entries in my_rss_feed['items']:
    print(entries)
    title = entries.title
    link = entries.link
    description = entries.description
    print(link)
    print(title)
    print(description)
    string = title

    # This extracts the location from the job title so a lat/long can be generated for the map.
    first_pos = string.rfind("(")
    last_pos = string.rfind(")")
    # This is the place the location is stored and the lat/long is generated.
    temp_location_holder = geo_locator.geocode(string[first_pos + 1: last_pos])
    time.sleep(.5)

    with cxn:
        try:
            cur.execute(f'''INSERT INTO rss_feed (id, type, link, company, title, location, description, latitude,
                            longitude) VALUES (?,?,?,?,?,?,?,?,?);''', ('not in use', 'not in use', entries['link'],
                            'not in use', string[first_pos + 1: last_pos], entries['title'], entries['description'],
                            temp_location_holder.latitude, temp_location_holder.longitude))
        except AttributeError:
            cur.execute(f'''INSERT INTO rss_feed (id, type, link, company, title, location, description, latitude,
                            longitude) VALUES (?,?,?,?,?,?,?,?,?);''', ('not in use', 'not in use', entries['link'],
                            'not in use', string[first_pos + 1: last_pos], entries['title'], entries['description'],
                            0.0, 0.0))
# Commit your changes to the program
cxn.commit()
# Close the cursor_object
cur.close()