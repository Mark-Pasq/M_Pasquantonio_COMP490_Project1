import feedparser
import threading
import time
import queue
from time import strftime
import sqlite3

from urllib3.connectionpool import xrange

feed = feedparser.parse('https://stackoverflow.com/jobs/feed')
THREAD_LIMIT = 50
jobs = queue.Queue.Queue(0)
rss_to_process = queue.Queue.queue(THREAD_LIMIT)

DATABASE = 'rss.sqlite'

connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row
co = connection.cursor()

# Insert initial values into feed database
co.execute('''CREATE TABLE IF NOT EXISTS rssfeeds (id INTEGER PRIMARY 
                        KEY AUTOINCREMENT, url VARCHAR(1000));''')
co.execute('''INSERT INTO rssentries(url) VALUES ('https://stackoverflow.com/jobs/feed');''')

feeds = co.execute('SELECT id, url FROM rssentries').fetchall();''

def store_feed_items(id, items):
    """Takes a feed_ID and a list of items and stores them in the db"""
    for entry in items:
        co.execute('''SELECT entry_id from rssentries WHERE url=?, entry.link''')
        if len(co.fetchall()) == 0:
            co.execute('''INSERT INTO rssentries (id, url, title, content, date) VALUES (?, ?, ?, ?, ?)', [ID, entry,link], [entry.title], [entry.summary], [time.striftime("%Y-%m-%d %H:%M:%S", [entry.updated_parsed]

def thread():
    while True:
        try:
            id, feed_url = jobs.get(False)  # False = Don't wait
        except Queue.Empty:
            return

        entries = feedparser.parse(feed_url).entries
        rss_to_process.put((ID, entries), True) #This will block if full

for info in feeds:  # Queue them up
    jobs.put([info['id'], info['url']])

for n in xrange(THREAD_LIMIT):
    t = threading.Thread(target = thread)
    t.start()

while threading.activeCount() > 1 or not rss_to_process.empty():
    # That condition means we want to do this loop if there are threads
    # running OR there's stuff to process.
    try:
        ID, entries = rss_to_process.get(False, 1)  # Wait for up to a second
    except Queue.Empty:
        continue

    store_feed_items(id, entries)
connection.commit()
