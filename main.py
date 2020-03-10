# !/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490 Project 1
# JobsAssignment Sprint 4
# Filename: mapplot.py
"""
This file handles the ability to create an application GUI to view the contents of
a database.  You can input your parameters and click a search button for filtered database
information.  **Note** - This does not work at this time.  Just click the green 'run'
button to launce the GUI.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, Main_Window):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelMainWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelMainWindow.setGeometry(QtCore.QRect(250, 20, 500, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setUnderline(True)
        self.labelMainWindow.setFont(font)
        self.labelMainWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMainWindow.setObjectName("labelMainWindow")
        self.lineEditDateToSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateToSearch.setGeometry(QtCore.QRect(275, 150, 200, 40))
        self.lineEditDateToSearch.setObjectName("lineEditDateToSearch")
        self.lineEditDateFromSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateFromSearch.setGeometry(QtCore.QRect(525, 150, 200, 40))
        self.lineEditDateFromSearch.setObjectName("lineEditDateFromSearch")
        self.labelDateTo = QtWidgets.QLabel(self.centralwidget)
        self.labelDateTo.setGeometry(QtCore.QRect(325, 120, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.labelDateTo.setFont(font)
        self.labelDateTo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDateTo.setObjectName("labelDateTo")
        self.labelDateFrom = QtWidgets.QLabel(self.centralwidget)
        self.labelDateFrom.setGeometry(QtCore.QRect(575, 120, 100, 20))
        self.labelDateFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDateFrom.setObjectName("labelDateFrom")
        self.labelSearchDates = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchDates.setGeometry(QtCore.QRect(50, 150, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSearchDates.setFont(font)
        self.labelSearchDates.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelSearchDates.setObjectName("labelSearchDates")
        self.pushButtonSearchDates = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchDates.setGeometry(QtCore.QRect(800, 150, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchDates.setFont(font)
        self.pushButtonSearchDates.setObjectName("pushButtonSearchDates")
        self.lineEditSearchCompany = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchCompany.setGeometry(QtCore.QRect(275, 250, 450, 40))
        self.lineEditSearchCompany.setObjectName("lineEditSearchCompany")
        self.pushButtonSearchCompany = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchCompany.setGeometry(QtCore.QRect(800, 250, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchCompany.setFont(font)
        self.pushButtonSearchCompany.setObjectName("pushButtonSearchCompany")
        self.labelSearchCompany = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchCompany.setGeometry(QtCore.QRect(50, 250, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSearchCompany.setFont(font)
        self.labelSearchCompany.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelSearchCompany.setObjectName("labelSearchCompany")
        self.lineEditSearchLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchLocation.setGeometry(QtCore.QRect(275, 350, 450, 40))
        self.lineEditSearchLocation.setObjectName("lineEditSearchLocation")
        self.pushButtonSearchLocation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchLocation.setGeometry(QtCore.QRect(800, 350, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchLocation.setFont(font)
        self.pushButtonSearchLocation.setObjectName("pushButtonSearchLocation")
        self.pushButtonSearchTechnology = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchTechnology.setGeometry(QtCore.QRect(800, 450, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchTechnology.setFont(font)
        self.pushButtonSearchTechnology.setObjectName("pushButtonSearchTechnology")
        self.pushButtonSearchTechnology.clicked.connect(self.slot_method)
        self.lineEditSearchTechnology = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchTechnology.setGeometry(QtCore.QRect(275, 450, 450, 40))
        self.lineEditSearchTechnology.setWhatsThis("")
        self.lineEditSearchTechnology.setObjectName("lineEditSearchTechnology")
        self.labelSearchLocation = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchLocation.setGeometry(QtCore.QRect(50, 350, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSearchLocation.setFont(font)
        self.labelSearchLocation.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelSearchLocation.setObjectName("labelSearchLocation")
        self.labelSearchTechnology = QtWidgets.QLabel(self.centralwidget)
        self.labelSearchTechnology.setGeometry(QtCore.QRect(50, 450, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSearchTechnology.setFont(font)
        self.labelSearchTechnology.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelSearchTechnology.setObjectName("labelSearchTechnology")
        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(400, 520, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonExit.clicked.connect(self.show_dialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.pushButtonSearchDates.clicked.connect(self.lineEditDateToSearch.selectAll)
        self.pushButtonSearchDates.clicked.connect(self.lineEditDateFromSearch.selectAll)
        self.pushButtonSearchCompany.clicked.connect(self.lineEditSearchCompany.selectAll)
        self.pushButtonSearchLocation.clicked.connect(self.lineEditSearchLocation.selectAll)
        self.pushButtonSearchTechnology.clicked.connect(self.lineEditSearchTechnology.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self):
        # _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle_translate("MainWindow", "MainWindow")
        MainWindow.setStatusTip_translate("MainWindow", "Enter your date to search here!")
        self.labelMainWindow.setText_translate("MainWindow", "Jobs Posting Search Application")
        self.lineEditDateToSearch.setStatusTip_translate("MainWindow", "Enter your date to search to here!")
        self.lineEditDateFromSearch.setStatusTip_translate("MainWindow", "Enter your date to search from here!")
        self.labelDateTo.setText_translate("MainWindow", "Date To:")
        self.labelDateFrom.setText_translate("MainWindow", "Date From:")
        self.labelSearchDates.setText_translate("MainWindow", "Search Dates:")
        self.pushButtonSearchDates.setStatusTip_translate("MainWindow", "Click to search!")
        self.pushButtonSearchDates.setText_translate("MainWindow", "Search!")
        self.lineEditSearchCompany.setStatusTip_translate("MainWindow", "Enter the company to search for here!")
        self.pushButtonSearchCompany.setStatusTip_translate("MainWindow", "Click to search!")
        self.pushButtonSearchCompany.setText_translate("MainWindow", "Search!")
        self.labelSearchCompany.setText_translate("MainWindow", "Search Company:")
        self.lineEditSearchLocation.setStatusTip_translate("MainWindow", "Enter a geographical location to search for here!")
        self.pushButtonSearchLocation.setStatusTip_translate("MainWindow", "Click to search!")
        self.pushButtonSearchLocation.setText_translate("MainWindow", "Search!")
        self.pushButtonSearchTechnology.setStatusTip_translate("MainWindow", "Click to search!")
        self.pushButtonSearchTechnology.setText_translate("MainWindow", "Search!")
        self.lineEditSearchTechnology.setStatusTip_translate("MainWindow", "Enter a technology, like Python, Java, "
                                                                           "PhP, AI, etc., to search for!")
        self.labelSearchLocation.setText_translate("MainWindow", "Search Location:")
        self.labelSearchTechnology.setText_translate("MainWindow", "Search Technology:")
        self.pushButtonExit.setStatusTip_translate("MainWindow", "Click to exit the application!")
        self.pushButtonExit.setText_translate("MainWindow", "Exit!")

    def show_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("Clicking the 'yes' button will terminate your job search!!!")
        msg_box.setWindowTitle("Sprint4GUI Exit!!!")
        msg_box.setDetailedText("Are you sure???!")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.No)
        msg_box.buttonClicked.connect(self.msg_button_clicked)

        return_value = msg_box.exec()
        if return_value == QMessageBox.Yes:
            print("Yes button is clicked")

        if return_value == QMessageBox.No:
            print("No button is clicked")

        if return_value == QMessageBox.Cancel:
            print("Cancel button is clicked")

    def slot_method(self, msg_box):
        return_value = msg_box.exec()
        if return_value == self.pushButtonSearchTechnology.clicked.connect(self.slot_method):
            print("Search is clicked!")

    @staticmethod
    def msg_button_clicked(i):
        print("Button clicked is :", i.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
