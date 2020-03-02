#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 4
# Filename: project_gui.py
"""
This file is the PyQt5 GUI file of COMP490 Project 1.  It contains all the necessary functions and methods
to display a interactive GUI to search the job listings.
"""

import os
import sqlite3
import sys
import jobs
from PyQt5.uic.properties import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 275, 800, 600)  # First two parameters places window in screen, second two window size.
        self.setStyleSheet('background-color: gray')
        self.setWindowTitle('Sprint4_GUI')
        self.ui()

    def ui(self):
        #######################Button Set-Up###########################
        self.text = QLabel('Search the Job Postings', self)
        self.text.setStyleSheet('font-size: 24pt; font-family: Arial')
        self.text.move(180, 40)  # Places the position of label.
        self.searchButton = QPushButton('Search', self)
        self.searchButton.setStyleSheet('background-color: orange')
        self.searchButton.move(200, 500)  # Placement of button in window.
        self.searchButton.clicked.connect(self.on_click)
        self.exitButton = QPushButton('Exit', self)
        self.exitButton.setStyleSheet('background-color: orange')
        self.exitButton.move(350, 500)  # Placement of button in window.
        self.exitButton.clicked.connect(self.close)  # Closes the actively running window.
        self.clearButton = QPushButton('Clear', self)
        self.clearButton.setStyleSheet('background-color: orange')
        self.clearButton.move(500, 500)  # Placement of button in window.

        ####################Search Dates Set-Up###################################
        self.searchDatesLabel = QLabel("Search Dates :", self)
        self.searchDatesLabel.setStyleSheet('font-size: 14pt; font-family: Tahoma')
        self.searchDatesLabel.move(50, 150)  # Places the position of label.
        self.searchDatesFromEntryTextBox = QLineEdit(self)
        self.searchDatesFromEntryTextBox.setPlaceholderText("Enter Start Date Here.")
        self.searchDatesFromEntryTextBox.setStyleSheet('background-color: orange')
        self.searchDatesFromEntryTextBox.move(280, 155)  # Places the position of TextBox.
        self.searchDatesFromEntryTextBox.resize(220, 25)  # Size of the TextBox.
        self.searchDatesToEntryTextBox = QLineEdit(self)
        self.searchDatesToEntryTextBox.setPlaceholderText("Enter End Date Here.")
        self.searchDatesToEntryTextBox.setStyleSheet('background-color: orange')
        self.searchDatesToEntryTextBox.move(510, 155)  # Places the position of TextBox.
        self.searchDatesToEntryTextBox.resize(220, 25)  # Size of the TextBox.

        ################################Search Company Set-Up##################################
        self.searchCompanyLabel = QLabel("Company Search: ", self)
        self.searchCompanyLabel.setStyleSheet('font-size: 14pt; font-family: Tahoma')
        self.searchCompanyLabel.move(50, 223)  # Places the position of label.
        self.searchCompanyEntryTextBox = QLineEdit(self)
        self.searchCompanyEntryTextBox.setPlaceholderText("Enter a Company you'd like to work for.")
        self.searchCompanyEntryTextBox.setStyleSheet('background-color: orange')
        self.searchCompanyEntryTextBox.move(280, 225)  # Places the position of TextBox.
        self.searchCompanyEntryTextBox.resize(450, 25)  # Size of the TextBox.

        ##############################Search Location Set-Up######################################
        self.searchLocationLabel = QLabel("Location Search: ", self)
        self.searchLocationLabel.setStyleSheet('font-size: 14pt; font-family: Tahoma')
        self.searchLocationLabel.move(50, 293)  # Places the position of label.
        self.searchLocationEntryTextBox = QLineEdit(self)
        self.searchLocationEntryTextBox.setPlaceholderText("Enter a Location in the world you'd like to live in.")
        self.searchLocationEntryTextBox.setStyleSheet('background-color: orange')
        self.searchLocationEntryTextBox.move(280, 295)  # Places the position of TextBox.
        self.searchLocationEntryTextBox.resize(450, 25)  # Size of the TextBox.

        ######################################Search Technology Set-Up##################################
        self.searchTechnologyLabel = QLabel("Technology Search: ", self)
        self.searchTechnologyLabel.setStyleSheet('font-size: 14pt; font-family: Tahoma')
        self.searchTechnologyLabel.move(50, 363)  # Places the position of label.
        self.searchTechnologyEntryTextBox = QLineEdit(self)
        self.searchTechnologyEntryTextBox.setPlaceholderText("Enter a Technology (Python, Java, PHP, etc.) that "
                                                             "interests you.")
        self.searchTechnologyEntryTextBox.setStyleSheet('background-color: orange')
        self.searchTechnologyEntryTextBox.move(280, 365)  # Places the position of TextBox.
        self.searchTechnologyEntryTextBox.resize(450, 25)  # Size of the TextBox.
        self.show()

    def on_click(self):
        sender = self.sender()
        if sender.text() == "Search":
            entry = self.mod_num.text()
            cxn = sqlite3.connect("job_demo.sqlite")
            cur = cxn.cursor()
            cur.execute("SELECT * FROM github_jobs WHERE location=?", [entry])
            results = cur.fetchone()
            print(results)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
