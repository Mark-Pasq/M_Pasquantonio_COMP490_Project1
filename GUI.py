import cmd
import os
import sys
from PyQt5.QtWidgets import QPushButton
import jobs
from PyQt5 import uic, QtWidgets, QtCore


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Sprint4_GUI.ui', self)
        self.show()


def UI(window):
    clear_button = QPushButton("Clear", window)
    search_button = QPushButton("Search", window)
    quit_button = QPushButton("Exit", window)
    quit_button.clicked.connect(window.app.exit)
    window.text.move(160, 50)
    clear_button.move(100, 80)
    search_button.move(150, 80)
    quit_button.move(200, 80)
    clear_button.clicked.connect(window.clear_func)
    search_button.clicked.connect(window.search_func)
    quit_button.clicked.connect(window.quit_func)
    window.show()

    def clear_func(window):
        window.text.setText("You clicked clear!!!")
        window.text.resize(150, 20)
        pass

    def search_func(self):
        window.text.setText("You clicked search!!!")
        window.text.resize(150, 20)
        pass

    def quit_func():  # When quit button is clicked, program quits.
        os.system()
        QtCore.QCoreApplication.instance().quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
