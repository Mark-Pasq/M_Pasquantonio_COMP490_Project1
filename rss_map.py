# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: mapplot.py
"""
This file handles the ability to get geolocation information on the locations of the jobs
in the github jobs database only.  When you click the green 'run' button, a map will load
and it will contain a map of the world with black dots on the map, which will signify a location
based on latitude-longitude information gained from the original JSON download of the GitHub
Jobs posting from Sprint 1.
"""
import plotly.express as px
import pandas as pd
import jobs

conn, cursor = jobs.open_db("job_demo.sqlite")
query = pd.read_sql_query('''SELECT * FROM rss_feed''', conn)

df_from_table = pd.DataFrame(query, columns=['id', 'type', 'url', 'created_at', 'company', 'location',
                                             'title', 'longitude', 'latitude'])

pd.set_option('display.max_columns', None)
print(df_from_table)

fig = px.scatter_mapbox(df_from_table, lat='latitude', lon='longitude', hover_name='id', hover_data=['type', 'company',
                                                                                                     'created_at',
                                                                                                     'title'],
                        color_discrete_sequence=["black"], zoom=3, height=900)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
