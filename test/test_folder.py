#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_jobs.py
import sqlite3
import pytest
import jobs

conn = sqlite3.connect('test_project_1.sqlite')
c = conn.cursor()


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
    connection = sqlite3.connect('test_project_1.sqlite')
    cursor_object = connection.cursor()
    # get the count of tables with the name
    cursor_object.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND 
    name='test_github_jobs_table' ''')

    # if the count is 1, then table exists
    if (cursor_object.fetchone()[0]) == 1:
        print('There is only 1 table in the database named github_jobs_table.')


def test_get_locations():
    connection = sqlite3.connect('test_project_1.sqlite')
    cursor_object = connection.cursor()
    for row in cursor_object.execute('''SELECT EXISTS (SELECT location from test_github_jobs_table WHERE id = 
                              '2e67c6a6-eda0-4a6d-87af-548eaa8111d3')'''):
        assert row[0] == 'Munich, Germany'
        print('Munich, Germany is the location of the job in row 0')

        connection.commit()


def test_count_number_of__rows():
    connection = sqlite3.connect('project_1.sqlite')
    cursor_obj = connection.cursor()
    cursor_obj.execute('''SELECT count(*) from github_jobs_table ''')
    rowcount = cursor_obj.fetchall()[0]
    assert rowcount == 249
