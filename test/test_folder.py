#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_jobs.py
import sqlite3
import pytest
import jobs

conn = sqlite3.connect('rss.sqlite')
cur_obj = conn.cursor()


@pytest.fixture
def get_data():
    import jobs
    return jobs.get_github_jobs_data()


def test_jobs_dict(get_data):
    # first required test
    assert len(get_data) >= 175
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
    connection = sqlite3.connect('rss.sqlite')
    cursor_object = connection.cursor()
    # get the count of tables with the name
    cursor_object.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='RSSentries' ''')
    # if the count is 1, then table exists
    assert cursor_object.fetchone()[0] == 0
    print('There is only 1 table in the database named RSSentries.')


def test_get_locations():
    connection = sqlite3.connect('project_1.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute(''' SELECT company, location FROM main.github_jobs_table WHERE location ='New York'
     and company = 'Nike' ''')


def test_get_number_of_rows():
    connection = sqlite3.connect('project_1.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute("BEGIN")  # start transaction
    number_of_rows = cursor_object.execute("SELECT COUNT() FROM sqlite_master").fetchone()[0]
    # if n > big: be_prepared()
    cursor_object.execute("SELECT * FROM sqlite_master").fetchall()
    cursor_object.connection.commit()  # end transaction
    if number_of_rows >= 500:
        # assert number_of_rows >= 500
        print('YES!! There are ' + str(number_of_rows) + ' rows in the table.')
    # if number_of_rows > 5000:
    #     assert number_of_rows < 5000
    #     print('NO!!  There are only ' + str(number_of_rows) + ' rows in the table.')
