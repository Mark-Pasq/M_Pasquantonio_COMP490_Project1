# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: GeoLocation.py
"""
This file handles the ability to get geolocation on the locations of the jobs
in the database.  It will give addresses and latitudinal
"""
import pandas as pd
import jobs
from pprint import pprint
import sqlite3

data = jobs.get_github_jobs_data()

cnx = sqlite3.connect('jobdemo.sqlite[2]')
cur = cnx.cursor()

cur.execute('SELECT * FROM hardcode_github_jobs LIMIT 5;')

results = cur.fetchall()
pprint(results)

cnx.commit()
cur.close()

