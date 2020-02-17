#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 3
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.  It also populates the table.
"""
import sqlite3
import feedparser

myfeed = feedparser.parse("https://stackoverflow.com/jobs/feed")
for item in myfeed['items']:

    title = item.title
    link = item.link
    description = item.description

    print(title)
    print(link)
    print(description)

    db = sqlite3.connect('rss.sqlite')
    with db:
        cur = db.cursor()
        cur.execute(f'''INSERT INTO main.RSSentries(title, link, description) 
                        VALUES (?, ?, ?);''', (title, link, description))

        print('Succesfull!')
# close the cursor
cur.close()

# close the connection
db.close()
