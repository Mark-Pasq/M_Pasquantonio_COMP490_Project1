#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_jobs.py
"""
This file handles the tests associated with COMP490 Project 1.
"""

import sqlite3
import pytest
import jobs


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


def test_save_data_to_file():
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
    cursor_object.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND 
                            name='RSSentries' ''')
    # if the count is 1, then table exists
    assert cursor_object.fetchone()[0] == 1
    print('There is only 1 table in the database named test_table.')


def test_get_location():
    connection = sqlite3.connect('testonly.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute(''' SELECT company, location FROM main.test_table WHERE 
                            location ='Beaverton, Oregon'and company = 'Nike' ''')


def test_table_exists():
    fake_table = 'test_table'
    fake_row = {'id': 'F$RT%YH&', 'type': 'Full Time', 'url': 'http://wwww.fakedata.com', 'created_at': '02-12-2020',
                'company': "Don't Work Here Comp", 'company_url': None, 'location': "giant urban metro",
                'title': 'Junior software peon', 'description': "blah blah, devops, scrum, hot tech",
                'how_to_apply': "http://runaway.com", 'company_logo': None}
    connection, cursor = jobs.open_db('testonly.sqlite')
    jobs.create_table(cursor, jobs.make_column_description_from_json_dict(fake_row), fake_table)
    result_cursor = cursor.execute(f"SELECT name from sqlite_master where (name = '{fake_table}')")
    """results = result_cursor.rowcount"""
    success = len(result_cursor.fetchall()) >= 1
    assert success


def test_save_data():  # modern sprint2 version of save data
    # this is fake data, but I'm testing the save_to_db function so fake data is fine
    fake_row = {'id': 'F$RT%YH&', 'type': 'Full Time', 'url': 'http://wwww.fakedata.com', 'created_at': '02-12-2020',
                'company': "Don't Work Here Comp", 'company_url': None, 'location': "giant urban metro",
                'title': 'Junior software peon', 'description': "blah blah, devops, scrum, hot tech",
                'how_to_apply': "http://runaway.com", 'company_logo': None}
    fake_table = 'test_table'
    connection, cursor = jobs.open_db('testonly.sqlite')
    jobs.create_table(cursor, jobs.make_column_description_from_json_dict(fake_row), fake_table)
    # might have to blow away db on later runs - first run is fine
    jobs.save_to_db([fake_row], cursor, fake_table)
    test_query = F"SELECT type from {fake_table} WHERE (id = 'F$RT%YH&')"
    result_cursor = cursor.execute(test_query)
    results = result_cursor.rowcount
    success = len(result_cursor.fetchall()) >= 1
    jobs.close_db(connection)
    assert success

# def main():
#     connection = sqlite3.connect('jobs.hardcode_github_jobs.sqlite')
#     py_obj = connection.cursor()
#     py_obj.execute(f'''INSERT INTO 'test_table' (id, type, url, created_at, company, company_url, location, title,
#                         description, how_to_apply, company_logo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
#
#     if __name__ == '__main__':
#         main()
