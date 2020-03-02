#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: Map.py
"""
This file handles the necessary files to get lat and long from one table
so that the jobs can be placed on an interactive map.
"""

import sqlite3
from geopy.geocoders import Nominatim
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

geo_locator = Nominatim(user_agent='GoogleMaps')
cxn = sqlite3.connect('job_demo.sqlite')
cur = cxn.cursor()
cur.execute('DELETE FROM main.lat_long_locations;')
cur.execute(
    '''CREATE TABLE IF NOT EXISTS main.lat_long_locations(id INTEGER PRIMARY KEY, latitude REAL, longitude REAL);''')
cur.execute('''SELECT location FROM main.github_jobs;''')
# cur.execute("SELECT * FROM github_jobs ORDER BY created_at DESC LIMIT 1;")
rows = cur.fetchall()
counter = 0
for items in rows:
    counter = counter + 1
    time.sleep(.5)
    location = geo_locator.geocode(items)
    if counter > 10:
        break
    try:
        if location is None:
            continue
        print(location.longitude, location.latitude)
        print(counter)
        cur.execute(f'''INSERT INTO main.lat_long_locations(latitude, longitude) VALUES (?, ?);''',
                    (location.longitude, location.latitude))

    except AttributeError:
        cur.execute(f'''INSERT INTO main.lat_long_locations( latitude, longitude) VALUES (?, ?)''',
                    ("remote", "remote"))

cxn.commit()
cur.close()



