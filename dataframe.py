# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: GeoLocation.py
"""
This file handles the ability to get geolocation on the locations of the jobs
in the database.  It will give addresses and latitudinal
"""
import matplotlib
import pandas as pd
import plotly.express as px

from geopy.extra.rate_limiter import RateLimiter
import jobs
from map import geo_locator

data = jobs.get_github_jobs_data()


framed_data = pd.DataFrame(data, columns=["id", "title", "type", "company", "location", "latitude", "longitude"])

pd.set_option('display.max_columns', None)

geocode = RateLimiter(geo_locator.geocode, min_delay_seconds=1)

framed_data["address"] = framed_data["location"].apply(geocode)

fig = px.scatter_mapbox(framed_data, lat="latitude", lon="longitude", hover_name="id",
                        hover_data=["title", "type", "company"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

# cnx = sqlite3.connect('job_demo.sqlite')
# cur = cnx.cursor()
#
# cur.execute('SELECT * FROM github_jobs LIMIT 5;')
#
# results = cur.fetchall()
# pprint(results)
#
# cnx.commit()
# cur.close()

