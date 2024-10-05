
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class LineInput(QWidget):
    """Creates a window for adding data for line diagram"""
    def __init__(self):
        super().__init__()

        # create geometry and layout for line input window
        self.setGeometry(100, 100, 500, 750)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        # create layouts
        self.layout_left = QVBoxLayout()
        self.layout_right = QVBoxLayout()
        self.main_layout.addLayout(self.layout_left)
        self.main_layout.addLayout(self.layout_right)

        self.data = []          # initialize list for QLineEdits

        example = QLabel('Example: 3, 7.55')
        example.setFont(QFont('Arial', 10))
        self.layout_left.addWidget(example)

        # Adds 50 QLineEdits for data points
        for i in range(50):
            data_line_edit = QLineEdit()
            data_line_edit.setFixedWidth(200)
            if i <= 26:
                self.layout_left.addWidget(data_line_edit)
            else:
                self.layout_right.addWidget(data_line_edit)
            self.data.append(data_line_edit)

        # Creates ok button that is clicked, when the data is added
        self.ok_button = QPushButton('OK', self)
        self.ok_button.setFixedSize(QtCore.QSize(200, 30))
        self.ok_button.setStyleSheet('background: lime')
        self.ok_button.setFont(QFont('Arial', 8))
        self.layout_right.addWidget(self.ok_button)

    def get_data_list(self):
        """returns created data list"""
        return self.data
