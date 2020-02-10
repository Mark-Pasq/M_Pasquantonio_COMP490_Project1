#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_jobs.py
import sqlite3
import pytest
import jobs
import santore_db


@pytest.fixture
def get_data():
    import jobs
    return jobs.get_github_jobs_data()


def test_jobs_dict(get_data):
    # first required test
    assert len(get_data) >= 100
    assert type(get_data[1]) is dict


def test_jobs_data(get_data):
    # any real data should have both full time and Contract
    # jobs in the list, assert this
    data = get_data
    full_time_found = False
    contract_found = False
    for item in data:
        if item['type'] == 'Contract':
            contract_found = True
        elif item['type'] == 'Full Time':
            full_time_found = True
    assert contract_found and full_time_found


def test_save_data():
    # second required test
    demo_data = {'id': 1234, 'type': "Testable"}
    list_data = []
    list_data.append(demo_data)
    file_name = "testfile.txt"
    jobs.save_data(list_data, file_name)
    testfile = open(file_name, 'r')
    saved_data = testfile.readlines()
    # the save puts a newline at the end
    assert f"{str(demo_data)}\n" in saved_data


def test_check_if_table_exists():
    conn = sqlite3.connect('test_github_jobs.sqlite')
    c = conn.cursor()

    # santore_db.create_table(c)

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Jobs_Listing' ''')

    # if the count is 1, then table exists
    assert (c.fetchone()[0] == 1)
    print('There is only 1 table in the database named Jobs_Listing.')

    # commit the changes to db
    conn.commit()
    # close the connection
    conn.close()


# def test_fetch_data():
#     conn = sqlite3.connect('github_jobs.sqlite')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT location FROM main.Jobs_Listing WHERE location = Chicago''')
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)
#
#     conn.commit()
#     conn.close()
def test_get_locations():

    conn = sqlite3.connect('test_github_jobs.sqlite')
    cursor = conn.cursor()

    for row in cursor.execute("SELECT EXISTS (SELECT 7 from Jobs_Listing WHERE id = "
                              "'7b7d433d-caf3-4b1b-9cf1-e4c25d560a53')"):
        assert 'location', row[0] == 'New York'
        print('New York is the location of the job in row 0')

#     # commit the changes to db
#     conn.commit()
#     # close the connection
#     conn.close()
#
#
# test_get_locations()
