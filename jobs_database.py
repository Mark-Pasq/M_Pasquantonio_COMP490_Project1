#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: jobs_database.py

import sqlite3
from sqlite3 import Error
global connection


def create_connection(db):
    # global connection
    db_file = "test/jobs.db"
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn:
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    project_db = r'C:\Mark Pasquantonio\PycharmProjects\M_Pasquantonio_COMP490_Project1\test\job.db'
    sql_create_jobs_table = """CREATE TABLE IF NOT EXISTS Jobs_Listing (
                                    id integer NOT NULL,
                                    type text NOT NULL,
                                    url text NOT NULL,
                                    created_at integer NOT NULL,
                                    company integer NOT NULL,
                                    company_url text NOT NULL,
                                    title text NOT NULL,
                                    location text NOT NULL,
                                    description text NOT NULL
                                    );"""

    # create a database connection
    connect = create_connection(project_db)

    # create tables
    if connect is not None:
        # create projects table
        create_table(connect, sql_create_jobs_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
