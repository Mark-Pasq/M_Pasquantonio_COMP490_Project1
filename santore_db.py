import sqlite3
from typing import Tuple
import jobs


def create_table(cursor):
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.Jobs_Listing (
                    id INTEGER PRIMARY KEY, type TEXT, url TEXT, created_at TEXT, company TEXT, company_url TEXT,
                    location TEXT, title TEXT, description TEXT);''')


def populate_table(cursor, data):
    for listing in data:
        # Insert a row of data
        cursor.execute('INSERT INTO github_jobs_table (id, type, url, created_at, company, company_url, '
                       'location, title, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);',
                       (listing['id'], listing['type'], listing['url'], listing['created_at'], listing['company'],
                        listing['company_URL'], listing['location'], listing['title'], listing['description']))


# def test_get_number_of_rows():
#     conn = sqlite3.connect('rss.sqlite')
#     cursor = conn.cursor()
#     cursor.execute("BEGIN")  # start transaction
#     number_of_rows = cursor.execute("SELECT COUNT() FROM RSSentries").fetchone()[0]
#     # if n > big: be_prepared()
#     cursor.execute("SELECT * FROM RSSentries").fetchall()
#     cursor.connection.commit()  # end transaction
#     if number_of_rows >= 500:
#         assert number_of_rows >= 500
#         print('YES!! There are ' + str(number_of_rows) + ' rows in the table.')
#     elif number_of_rows > 5000:
#         assert number_of_rows < 5000
#         print('NO!!  There are only ' + str(number_of_rows) + ' rows in the table.')


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    data = jobs.get_github_jobs_data()
    conn, cursor = open_db("github_jobs.sqlite")
    create_table(cursor)
    populate_table(cursor, data)
    # test_get_number_of_rows()
    print(type(conn))
    close_db(conn)

    if __name__ == '__main__':
        main()
