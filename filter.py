# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: filter.py
"""
This file is used to filter database data.
"""

# cxn = sqlite3.connect('job_demo.sqlite')
# cur = cxn.cursor()
# cur.execute(f"SELECT location FROM github_jobs ORDER BY location ASC;")
# results = cur.fetchall()
# for place in results:
#     print(place)
#     cxn.commit()
#     cur.close()

# cxn = sqlite3.connect('job_demo.sqlite')
# dataframe = pd.read_sql_query("SELECT * FROM github_jobs", cxn)
#
# print(dataframe.head())
# print(dataframe)
#
# cxn.close()


#########################################################################################
# import sqlite3
#
# cxn = sqlite3.connect("rss.sqlite")
# cur = cxn.cursor()
# cur.execute(f'SELECT title FROM rssfeed')
#
# rows = cur.fetchall()
# for row in rows:
#     # print(type(row))
#     # print(row[0])
#     string = row[0]
#
#     # position of opening square bracket
#     first_pos = string.rfind("(")
#     # position of closing square bracket
#     last_pos = string.rfind(")")
#     # printing the text between two square brackets
#     print(string[first_pos + 1: last_pos])  # Prints output 'How'
#
#     var = string[first_pos + 1: last_pos]
#     locs = ""
#     for x in var:
#         locs += x
#
#     # print(type(locs))
#     # print(row[0])
#
#     cxn = sqlite3.connect("rss.sqlite")
#     cur = cxn.cursor()
#     cur.execute('CREATE TABLE IF NOT EXISTS rss_loc (location TEXT)')
#     cur.execute('INSERT INTO rss_loc (location) VALUES (?);', (locs,))

#########################################################################

# def queryDateRange():
#     cxn = sqlite3.connect('job_demo.sqlite')
#     cur = cxn.cursor()
#     cur.execute(''' SELECT * FROM github_jobs ORDER BY created_at ''')
#     rows = cur.fetchall()
#     for items in rows:
#         print(items)
#
#     cxn.commit()
#     cur.close()
#
#
# queryDateRange()

################################################################################
import sqlite3

conn = sqlite3.connect('job_demo.sqlite')
c = conn.cursor()


def merged():
    c.execute(f'''DELETE FROM combined_table;''')
    c.execute(f'''INSERT INTO combined_table SELECT * FROM github_jobs UNION SELECT * FROM rss_feed;''')
    for line in c.fetchall():
        print(line)


merged()

conn.commit()
c.close()
