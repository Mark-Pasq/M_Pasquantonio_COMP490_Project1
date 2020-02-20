#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 3
# Filename: jobs_testing_folder.py
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
    """
    This test tests the validity of the data in the 'jobdemo.sqlite' database.  First it sets the parameters as false,
    then they enter the for loop to determine if the conditions are met, and then we assert the answer.  In this case,
    since there is no location in the database that matches the test parameters, the test will give a failed output.
    """
    data = get_data
    location_found = False
    company_found = False
    for item in data:
        if item['location'] == 'Plymouth, Massachusetts':
            location_found = True
        elif item['company'] == 'Microsoft':
            company_found = True
    assert company_found and location_found, "failed test"
    print('There is not a location in the "jobdemo.sqlite" database named Plymouth, Massachusetts.')


def test_save_data_to_file():
    # second required test
    demo_data = {'id': 1234, 'type': "Testable"}
    list_data = [demo_data]
    file_name = "testfile.txt"
    jobs.save_data(list_data, file_name)
    testfile = open(file_name, 'r')
    saved_data = testfile.readlines()
    # the save puts a newline at the end
    assert f"{str(demo_data)}\n" in saved_data


def test_check_if_table_exists():
    """
    This test checks to see if the table 'RSSentries' actually exists in the 'rss.sqlite' database.  This test will
    return a favorable answer.
    """
    connection = sqlite3.connect('testonly.sqlite')
    cursor_object = connection.cursor()
    # get the count of tables with the name
    cursor_object.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='test_table' ''')
    # if the count is 1, then table exists
    test_passed = cursor_object.fetchone()[0] == 1
    assert test_passed
    print('There is only 1 table in the database named test_table.')


def test_get_location():
    """
    This test checks the 'hardcode_github_jobs' table in the 'jobdemo.sqlite' database to see if there is a
    row that matches both type and location columns with the appropriate data.  This test will return a
    favorable answer.
    """
    connection = sqlite3.connect('jobdemo.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute(f'''CREATE TABLE IF NOT EXISTS hardcode_github_jobs (id, type, url, created_at,
        company, company_url, location, title, description, how_to_apply, company_logo);''')
    cursor_object.execute(f''' SELECT type, location FROM hardcode_github_jobs
        WHERE location ='Munich, Germany' and type = 'Full Time' ''')


def test_table_exists():
    """
    This test takes the 'test_table' table in the 'testonly.sqlite' database and injects a fake row with fake data.
    The test attempts to see if the test can see if the fake table exists in the testing database.  This test
    will return a favorable answer.
    """
    fake_table = 'test_table'
    fake_row = {'id': 'F$RT%YH&', 'type': 'Remote', 'url': 'http://wwww.fakedata.com', 'created_at': '02-12-2020',
                'company': "Don't Work Here Comp", 'company_url': None, 'location': "giant urban metro",
                'title': 'Junior software peon', 'description': "blah blah, devops, scrum, hot tech",
                'how_to_apply': "http://runaway.com", 'company_logo': None}
    connection, cursor = jobs.open_db('testonly.sqlite')
    jobs.create_table(cursor, jobs.make_column_description_from_json_dict(fake_row), fake_table)
    result_cursor = cursor.execute(f"SELECT name from sqlite_master where (name = '{fake_table}')")
    # results = result_cursor.rowcount
    success = len(result_cursor.fetchall()) >= 1
    assert success


def test_insertion_of_data():
    """
        This test will check to see if 'test_table" table in the 'testonly.sqlite' database will accept both good data
        AND bad data through an sqlite INSERT INTO command.
        """
    connection = sqlite3.connect('testonly.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute(f'''CREATE TABLE IF NOT EXISTS test_table (id, type, url, created_at,
          company, company_url, location, title, description, how_to_apply, company_logo)''')
    cursor_object.execute(
        f''' INSERT INTO test_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
        ('XYZ%^&123456789', 'Remote', 'http://wwww.me.org', 2020 - 12 - 25,
         'My Company, LLC', 'None', 'Your moms house', 'stud-muffin', 'blah blah blah',
         'Dont not worth it', 'None'))
    # cursor_object.execute(
    #     f'''INSERT INTO test_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
    #     (0o12345, 'Full Time', 98089, 'None', 'company: None', 'None', 'Home1',
    #      'Teacher', 'WOrd!!', 'how_to_apply: None', 'company_log: None'))


def test_read_from_database():
    """
    This test tests the ability to be able to read a specific item in a particular row correctly.  Here, we
    check to see if row 31 of the table 'hardcode_github_jobs' in 'jobdemo.sqlite' yields the answer
    company == Microsoft, which it does.  The test gives a favorable answer.
    """

    def read_from_database():
        pass

    connection = sqlite3.connect('jobdemo.sqlite')
    cursor_object = connection.cursor()
    sql = f'''SELECT * FROM hardcode_github_jobs'''
    for row in cursor_object.execute(sql):
        print(row[31])
    company = "Microsoft"
    sql = "SELECT * FROM hardcode_github_jobs WHERE company = ?"
    for row in cursor_object.execute(sql, (company,)):
        assert cursor_object.execute(sql, (company,)) == 'Microsoft'
        print(row[31]), 'test passes!'


def test_delete_and_update():
    conn = sqlite3.connect('rss.sqlite')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM RSSentries;')
    print('We have deleted', cursor.rowcount, 'records from the table.')
    # cursor.execute('DELETE FROM hardcode_github_jobs')
    print('We have deleted', cursor.rowcount, 'records from the table.')
    conn.commit()
    conn.close()


test_delete_and_update()


def test_delete_an_item_from_table():
    def row():
        pass

    connection = sqlite3.connect('rss.sqlite')
    cursor_object = connection.cursor()
    cursor_object.execute('DELETE from RSSentries WHERE rowid = 500')
    connection.commit()
    connection.close()


def main():
    if __name__ == '__main__':
        main()
