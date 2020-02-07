#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_jobs.py

import pytest
import jobs
import sqlite3


@pytest.fixture
def get_data():
    import jobs
    return jobs.get_github_jobs_data()


def test_my_jobs_dict(get_data):
    # first required test
    assert len(get_data) >= 100
    assert type(get_data[1]) is dict


def test_my_jobs_data(get_data):
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


def test_my_save_data_func():
    # second required test
    demo_data = {'id': 1234, 'type': "Testable"}
    file_name = "testfile.txt"
    jobs.save_data(file_name)
    test_data = open(file_name, 'r')
    saved_data = test_data.readlines()
    # the save puts a newline at the end
    assert f"{str(demo_data)}\n" in saved_data


def test_check_if_db_exists():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM main.sqlite_master WHERE type='table' AND name='Jobs_Listing' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('The table exists.')
    else:
        print('The table does not exist.')

    # commit the changes to db
    conn.commit()
    # close the connection
    conn.close()
