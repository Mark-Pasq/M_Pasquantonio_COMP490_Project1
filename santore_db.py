import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def create_table(cursor):
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.Jobs_Listing (
           id TEXT PRIMARY KEY,
           type TEXT,
           url TEXT,
           created_at TEXT,
           company TEXT,
           company_url TEXT,
           location TEXT,
           title TEXT,
           description TEXT
           );''')


def populate_table(cursor, data):
    for listing in data:
        # Insert a row of data
        cursor.execute('''INSERT INTO Jobs_Listing (type, url, created_at, company, location, title,
        description) VALUES (?, ?, ?, ?, ?, ?, ?)''', (listing['type'], listing['url'],
                                                       listing['created_at'], listing['company'],
                                                       listing['location'],
                                                       listing['title'],
                                                       listing['description']))


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    conn, cursor = open_db("jobs.sqlite")
    create_table(cursor)
    populate_table(cursor)
    print(type(conn))
    close_db(conn)


if __name__ == '__main__':
    main()
