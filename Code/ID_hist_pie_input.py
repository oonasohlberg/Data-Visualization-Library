
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class HistPieInput(QWidget):
    def __init__(self):
        """creates window for histogram and pie diagram input"""
        super().__init__()

        # sets geometry of the window and layout
        self.setGeometry(100, 100, 270, 450)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.data = []          # initialize list for input QLineEdits

        example = QLabel('Example: Finland, 21.7')
        example.setFont(QFont('Arial', 10))
        self.main_layout.addWidget(example)

        # Adds 20 QLineEdits for data points
        for i in range(20):
            data_line_edit = QLineEdit()
            data_line_edit.setFixedWidth(250)
            self.main_layout.addWidget(data_line_edit)
            self.data.append(data_line_edit)

        # creates ok button
        self.ok_button = QPushButton('OK', self)
        self.ok_button.setFixedSize(QtCore.QSize(250, 30))
        self.ok_button.setStyleSheet('background: lime')
        self.ok_button.setFont(QFont('Arial', 8))
        self.main_layout.addWidget(self.ok_button)

    def get_data_list(self):
        """returns list containing the input data"""
        return self.data
