# M_Pasquantonio_COMP490_Project1 Agile Sprint 4
# Senior Design and Dev COMP490 Prof. J. Santore
# Filename/s: jobs.py, test_jobs.py, test_database

# This is Project 1 Agile Sprint 3.  It is designed to build on the first two Agile Sprints, where we took
# some data from a Github job board, then saved it to a text file.  For Sprint 2, we had to take the data
# from Sprint 1, and create a SQLite database and subsequent table to display the data.  For Sprint 3, we had to 
# download an RSS feed and store it in a similar manner as the .JSON file in part 1. 

# I started off pretty well.  I was able to get the data and set up a table with the RSS feed, but struggled 
# with the writing od the tests.  It has become very apparent to me it takes a lot of practice to master these.
# I added some testing but was confused about how to make the parameters accept both good and bad data,
# simultaneously.  Also am having difficulties using the Github Actions.

# I was able to create a test table, but had some trouble populating it.  Once I figured out it had to be in the
# test folder, it worked with ease.  The database part of this project has been fun to me.  There is a lot of 
# information on the web, both light and dark, so I was able to use the basic functionality of SQLite.  I can't
# wait to see what Sprint 4 has for me.

# Here is Sprint 4.  Sprint 4 is mostly unfinished.  I have many chunks that work, but was unable to get all the
# components to operate as thet should.

# The good: 
#           * I was able to get my original JSON file to work and it gave me the data that I needed throughout the project.
#           * I had trouble with the RSS feed portion, and in the end, it did work once "on my machine" then I somehow broke it,
#           and couldn't get the desired output.
#           * I was able to create the GUI using QT Designer and created a .py file from a .ui file.  When the file is launched,
#           it opens a nice window with options, but had trouble with the necessary code to get the search inputs working.
#           * The map plotting is working.  I was able to take location information from the JSON download and obtain lat/long
#           for geolocation points to be plotted.  Along with that map, it will also create a map that will show 3 jobs  from
#           the github_jobs feed within the 50 mile radius of BSU.
#           # I have some tests that work, but testing is where I lacked complete understanding.  More work needs to be done
#           on my behalf to unserstand it better.
# The bad:
#           * I am mostly disappointed with the outcome of this project for me.  I struggle a bit with code, but this was an 
#           excellent project to learn from.  This will be something I will finish on my own time.  This was submitted at 2:28am
#           on Thursday 3/12/2020.


