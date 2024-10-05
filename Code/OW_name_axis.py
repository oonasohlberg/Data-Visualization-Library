
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class NameAxisWindow(QWidget):

    def __init__(self, num):
        """Creates the window to name x- and y-axis"""
        super().__init__()
        if num == 1:            # if its line diagram
            self.setGeometry(100, 100, 300, 200)
        elif num == 2:          # if its histogram
            self.setGeometry(100, 100, 300, 150)
        else:                   # if its pie diagram
            self.setGeometry(100, 100, 300, 100)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        if num == 1 or num == 2:
            self.setWindowTitle('Name headline and axis')
        else:
            self.setWindowTitle('Name headline')

        # name headline
        self.headline = QLabel('Headline:')
        self.headline.setFont(QFont('Arial', 10))
        self.layout.addWidget(self.headline)
        self.headline = QLineEdit()
        self.layout.addWidget(self.headline)

        if num == 1:            # name x-axis
            self.x_label = QLabel('x-axis:')
            self.x_label.setFont(QFont('Arial', 10))
            self.layout.addWidget(self.x_label)
            self.x_edit = QLineEdit()
            self.layout.addWidget(self.x_edit)
        if num == 1 or num == 2:        # name y-axis
            self.y_label = QLabel('y-axis:')
            self.y_label.setFont(QFont('Arial', 10))
            self.layout.addWidget(self.y_label)
            self.y_edit = QLineEdit()
            self.layout.addWidget(self.y_edit)

        # creates ok button
        self.ok_button = QPushButton('OK', self)
        self.ok_button.setFont(QFont('Arial', 10))
        self.ok_button.setStyleSheet('background: lightgreen')
        self.ok_button.setFixedSize(QtCore.QSize(300, 30))
        self.layout.addWidget(self.ok_button)






