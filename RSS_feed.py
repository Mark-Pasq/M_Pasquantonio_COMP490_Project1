#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 3
# Filename: RSS_feed.py


import feedparser
import sqlite3
import connection

myfeed = feedparser.parse("https://stackoverflow.com/jobs/feed")

for items in myfeed['items']:
    link = items.link
    category = items.category
    title = items.title
    description = items.description
    pubDate = items.pubDate

    print(link)
    print(category)
    print(title)
    print(description)
    print(pubDate)

    # get the database ready for data
    connection = sqlite3.connect('rss.sqlite')

    # Create the table and place the data in the proper place
    with connection:
        cursor_object = connection.cursor()
        cursor_object.execute('INSERT INTO RSSentries (link, category, title, description, pubDate) '
                              'VALUES (?, ?, ?, ?, ?)', (items['link'], items['category'], items['title'],
                                                         items['description'], items['pubDate']))

# Commit your changes to the program
connection.commit()

# Close the cursor_object
connection.close()
