import sqlite3
from typing import Tuple
import jobs


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def create_table(cursor):
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.Jobs_Listing (
           id INTEGER PRIMARY KEY,
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
        cursor.execute('''INSERT INTO Jobs_Listing (id, type, url, created_at, company, company_url, location, title, 
        description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (listing['id'], listing['type'], listing['url'],
                                                              listing['created_at'], listing['company'],
                                                              listing['company_URL'], listing['location'],
                                                              listing['title'], listing['description']))


def get_number_of_rows():
    conn = sqlite3.connect('github_jobs.sqlite')
    cursor = conn.cursor()
    cursor.execute("BEGIN")  # start transaction
    n = cursor.execute("SELECT COUNT() FROM Jobs_Listing").fetchone()[0]
    # if n > big: be_prepared()
    cursor.execute("SELECT * FROM Jobs_Listing").fetchall()
    cursor.connection.commit()  # end transaction
    # assert n == len(all_rows)
    print(n)


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    data = jobs.get_github_jobs_data()
    conn, cursor = open_db("github_jobs.sqlite")
    create_table(cursor)
    populate_table(cursor, data)
    get_number_of_rows()
    print(type(conn))
    close_db(conn)

    if __name__ == '__main__':
        main()
