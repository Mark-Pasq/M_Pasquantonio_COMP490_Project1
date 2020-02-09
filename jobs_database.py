#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: jobs_database.py

import sqlite3


def create_a_table():
    connection = sqlite3.connect('jobs.db')
    cursor_obj = connection.cursor()

    # Create table
    cursor_obj.execute('''CREATE TABLE IF NOT EXISTS main.Jobs_Listing (
        id INTEGER PRIMARY KEY,
        type TEXT NOT NULL,
        url TEXT NOT NULL,
        created_at TEXT NOT NULL,
        company TEXT NOT NULL,
        company_url TEXT NOT NULL,
        location TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL
        );''')

    return connection()



def populate_table(cursor_obj):
    # Insert a row of data
    cursor_obj.execute('''INSERT INTO Jobs_Listing (id, type, url, created_at, company, company_url, location, title,
    description) VALUES ('1001', 'FullTime', 'http://www.google.com', '02-07-2020', 'Microsoft',
    'http://www.google.com', 'Seattle', 'Engineer', 'A job at a great place!')''')

    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def main():
    create_a_table()
    populate_table()

    if __name__ == '__main__':
        main()
