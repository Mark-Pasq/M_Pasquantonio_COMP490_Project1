# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: filter.py
"""
This file is used to filter database data.
"""
import sqlite3
import pandas as pd

# cxn = sqlite3.connect('job_demo.sqlite')
# cur = cxn.cursor()
# cur.execute(f"SELECT location FROM github_jobs ORDER BY location ASC;")
# results = cur.fetchall()
# for place in results:
#     print(place)
#     cxn.commit()
#     cur.close()

cxn = sqlite3.connect('job_demo.sqlite')
dataframe = pd.read_sql_query("SELECT * FROM github_jobs", cxn)

print(dataframe.head())
print(dataframe)

cxn.close()
