#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 3
# Filename: RSS_feed.py
"""
This file handles the parsing of an rss feed.
"""
import sqlite3
import feedparser

myfeed = feedparser.parse("https://stackoverflow.com/jobs/feed")

for items in myfeed['items']:
    link = items.link
    title = items.title
    description = items.description

    print(link)
    print(title)
    print(description)

    # get the database ready for data
    c = sqlite3.connect('rss.sqlite')

    # Create the table and place the data in the proper place
    with c:
        cursor_object = c.cursor()
        cursor_object.execute('INSERT INTO RSSentries (link, title, description) VALUES (?, ?, ?)',
                              (items['link'], items['title'], items['description']))

# Commit your changes to the program
c.commit()

# Close the cursor_object
c.close()
