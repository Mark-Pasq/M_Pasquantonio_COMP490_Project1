import sqlite3
from typing import Tuple
import pandas as pd
import plotly.express as px
import jobs
import geopy.distance as GeoDist


def establishConnection() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect("job_demo.sqlite")  # connects to db or makes new one
    cursor = conn.cursor()
    return conn, cursor


def createDataFrame():
    conn, cursor = establishConnection()
    query = pd.read_sql_query('''SELECT * FROM github_jobs''', conn)
    dataframe_from_table = pd.DataFrame(query, columns=["id", "type", "created_at", "company", "location", "title",
                                                        "latitude", "longitude"])
    return dataframe_from_table


def createMap():
    data_frame = createDataFrame()
    pd.set_option('display.max_columns', None)
    fig = px.scatter_mapbox(data_frame, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["title", "type", "company", "created_at", "location"],
                            color_discrete_sequence=["black"], zoom=3, height=900)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


# creates a new table to make plotting easier.
def makeFiftyMileRadiusTable():
    conn, cursor = establishConnection()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Fifty_Mile_Radius (id, type, created_at, company, location,
                    title, latitude, longitude)''')
    jobs.close_db(conn)


# creates another table for pandas to read easier
def makeDistancedTable():
    conn, cursor = establishConnection()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Distance_Table(id, type, created_at, company, location, title,
                        latitude, longitude);''')
    jobs.close_db(conn)


def insertIntoFiftyMileRadiusTable():
    makeFiftyMileRadiusTable()
    conn, cursor = establishConnection()
    cursor.execute('''DELETE FROM Fifty_Mile_Radius''')
    cursor.execute('''INSERT INTO Fifty_Mile_Radius SELECT * FROM github_jobs''')
    jobs.close_db(conn)


def insertIntoDistance():
    starting_coords = (41.9667679, -70.9661533)
    insertIntoFiftyMileRadiusTable()
    conn, cursor = establishConnection()
    cursor.execute('''DELETE FROM Distance_Table''')
    cursor.execute('''SELECT location, latitude, longitude FROM github_jobs''')
    rows = cursor.fetchall()
    for data in rows:
        comparative_coord = (data[1], data[2])
        distance = GeoDist.distance(comparative_coord, starting_coords).miles
        if distance <= 50:
            print(data[0])
            cursor.execute(
                f'''INSERT OR IGNORE INTO  Distance_Table SELECT * FROM github_jobs where location = "{data[0]}" ''')
                # f'''INSERT INTO github_jobs SELECT * FROM RSS_pull''')
    jobs.close_db(conn)


def plotFiftyMileRadius():
    conn, cursor = establishConnection()
    query = pd.read_sql_query('''SELECT * FROM Distance_Table''', conn)
    cursor.execute('''SELECT * FROM Distance_Table ''')
    rows = cursor.fetchall()
    for columns in rows:
        print(columns)
    print(query)
    dataframe_from_table = pd.DataFrame(query, columns=["id", "type", "created_at", "company", "location", "title",
                                                        "latitude", "longitude"])
    fig = px.scatter_mapbox(dataframe_from_table, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["title", "type", "company", "created_at", "location"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=900)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


createMap()
makeDistancedTable()
insertIntoDistance()
makeFiftyMileRadiusTable()
plotFiftyMileRadius()
