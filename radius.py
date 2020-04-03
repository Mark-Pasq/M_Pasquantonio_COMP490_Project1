#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Desi default gn and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: radius.py

"""
This file is the main file in the project.  It handles the necessary functions and
methods of the project.  The main operation of this file is to create a database and
populate it with downloaded material, then save it to a text file for later use.
When the green 'run' button is clicked, the function will print the contents of a
.JSON file and populate the table named job_demo.sqlite, which can be found in the
database to the right.------------>
"""
import geopy.distance as geoDist
import plotly.express as px
from typing import Tuple
import pandas as pd
import sqlite3
import jobs


def establishConnection() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect("job_demo.sqlite")  # connects to db or makes new one
    cursor = conn.cursor()
    return conn, cursor


def createDataFrame():
    conn, cursor = establishConnection()
    query = pd.read_sql_query(f'''SELECT * FROM github_jobs;''', conn)
    dataframe_from_table = pd.DataFrame(query, columns=["id", "type", "url", "created_at",
                                                        "company", "location", "title",
                                                        "latitude", "longitude"])
    conn.commit()
    return dataframe_from_table


def createMap():
    data_frame = createDataFrame()
    pd.set_option('display.max_columns', None)
    fig = px.scatter_mapbox(data_frame, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["type", "company", "created_at", "title"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=900)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


# creates a new table to make plotting easier.
def makeFiftyMileRadiusTable():
    conn, cursor = establishConnection()
    cursor.execute(
        f''' CREATE TABLE IF NOT EXISTS Fifty_Mile_Radius(id, type, url, created_at, company, location, title,
                    latitude REAL, longitude REAL);''')
    conn.commit()
    jobs.close_db(conn)


# creates another table for pandas to read easier
def makeDistancedTable():
    conn, cursor = establishConnection()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS Distance_Table (id, type, url, created_at, company, location, title,
                    latitude REAL, longitude REAL);''')
    conn.commit()
    jobs.close_db(conn)


def insertIntoFiftyMileRadiusTable():
    makeFiftyMileRadiusTable()
    conn, cursor = establishConnection()
    cursor.execute(f'''DELETE FROM Fifty_Mile_Radius;''')
    cursor.execute(f'''INSERT INTO Fifty_Mile_Radius SELECT * FROM github_jobs;''')
    conn.commit()
    jobs.close_db(conn)


def insertIntoDistance():
    starting_coords = (41.9667679, -70.9661533)
    insertIntoFiftyMileRadiusTable()
    conn, cursor = establishConnection()
    cursor.execute(f'''DELETE FROM Distance_Table;''')
    cursor.execute(f'''SELECT location, latitude, longitude FROM Fifty_Mile_Radius;''')
    rows = cursor.fetchall()
    for data in rows:
        comparative_coord = (data[1], data[2])
        distance = geoDist.distance(comparative_coord, starting_coords).miles
        if distance <= 50:
            print(data[0])
            cursor.execute(
                f'''INSERT OR IGNORE INTO  Distance_Table SELECT * FROM Fifty_Mile_Radius where location = "{data[0]}"''')
    conn.commit()
    jobs.close_db(conn)


def make_combined_map():
    conn, cursor = establishConnection()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS combined_table (id, type, url, created_at, company, location,
                        title, latitude, longitude);''')
    conn.commit()
    jobs.close_db(conn)


def insert_into_combined_table():
    data_frame = createDataFrame()
    make_combined_map()
    conn, cursor = establishConnection()
    cursor.execute(f'''DELETE FROM combined_table;''')
    cursor.execute(f'''INSERT INTO combined_table SELECT * FROM github_jobs UNION SELECT * FROM rss_feed;''')
    rows = cursor.fetchall()
    for data in rows:
        print(data)
    conn.commit()

    fig = px.scatter_mapbox(data_frame, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["company", "created_at", "type"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=900)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


def plotFiftyMileRadius():
    conn, cursor = establishConnection()
    query = pd.read_sql_query(f'''SELECT * FROM Distance_Table;''', conn)
    cursor.execute(f'''SELECT * FROM Distance_Table;''')
    rows = cursor.fetchall()
    for columns in rows:
        print(columns)
    print(query)
    dataframe_from_table = pd.DataFrame(query, columns=["id", "type", "url", "created_at", "company", "location",
                                                        "title", "latitude", "longitude"])

    fig = px.scatter_mapbox(dataframe_from_table, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["type", "company", "created_at", "title"], color_discrete_sequence=
                            ["fuchsia"], zoom=3, height=900)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


createMap()
makeDistancedTable()
insertIntoDistance()
makeFiftyMileRadiusTable()
make_combined_map()
insert_into_combined_table()
plotFiftyMileRadius()
