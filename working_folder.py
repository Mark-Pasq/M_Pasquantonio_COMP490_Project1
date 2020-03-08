
# def queryDateRange():
#     cxn = sqlite3.connect('job_demo.sqlite')
#     cur = cxn.cursor()
#     cur.execute(
#         "SELECT created_at FROM github_jobs WHERE created_at BETWEEN '2020-01-01' AND '2020-03-06' ORDER BY created_at")
#     rows = cur.fetchall()
#     for items in rows:
#         # time.sleep(.5)
#         print(items)
#
#     cxn.commit()
#     cur.close()
#
#     queryDateRange()

# def query_location():
#     cxn = sqlite3.connect('job_demo.sqlite')
#     cur = cxn.cursor()
#     cur.execute("SELECT * FROM lat_long_locations")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#
#     cxn.commit()
#     cur.close()
#
#
# query_location()

###################################################################################################################


