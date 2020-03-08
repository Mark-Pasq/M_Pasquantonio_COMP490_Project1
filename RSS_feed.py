#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.
"""
import time
import feedparser
import pprint
import sqlite3
import unidecode as unidecode
from geopy import Nominatim

geo_locator = Nominatim(user_agent='GoogleMaps')

rss = "http://stackoverflow.com/jobs/feed"
feed = feedparser.parse(rss)
for key in feed['entries']:
    time.sleep(1)
    try:
        print(unidecode.unidecode(key['title']))
        # print(unidecode.unidecode(key['link']))
        # print(unidecode.unidecode(key['description']))
        temp_location_holder = geo_locator.geocode(key['title'])
        pp = pprint.PrettyPrinter(indent=4)
        print(temp_location_holder)
        cxn = sqlite3.connect('rss.sqlite')
        cur = cxn.cursor()

        cur.execute(f'''CREATE TABLE IF NOT EXISTS rssfeed (link INTEGER NOT NULL PRIMARY KEY ON CONFLICT IGNORE,
                title TEXT, description TEXT, latitude REAL, longitude REAL);''')

        cur.execute(f''' INSERT INTO rssfeed(link, title, description, latitude, longitude) VALUES (?,?,?,?,?);''',
                    (key['link'], key['title'], key['description'], temp_location_holder.latitude,
                     temp_location_holder.longitude))
    except AttributeError:
        cxn = sqlite3.connect('rss.sqlite')
        cur = cxn.cursor()
        cur.execute(f'''INSERT INTO rssfeed(
                        link, title, description, latitude, longitude) 
                        VALUES (?,?,?,?,?)''', (key['link'], key['title'], key['description'], 0.0, 0.0))
