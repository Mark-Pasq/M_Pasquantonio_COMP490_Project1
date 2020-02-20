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
        cur.execute(f'''INSERT INTO main.RSSentries(link, title, description) VALUES (?, ?, ?);''', (item['link'],
                                                                                                     item['title'],
                                                                                                     item[
                                                                                                         'description']))
