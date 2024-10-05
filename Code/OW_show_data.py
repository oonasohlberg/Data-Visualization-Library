
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class ShowData(QWidget):
    def __init__(self, data):
        """Shows input data when the button is clicked"""
        super().__init__()

        self.data = data            # data of the diagram
        self.setWindowTitle('Input data')

        if isinstance(data, list):
            # is line diagram
            len_data = len(self.data)
            self.main_layout = QHBoxLayout()
            self.setLayout(self.main_layout)
            self.left_layout = QVBoxLayout()
            self.right_layout = QVBoxLayout()
            self.main_layout.addLayout(self.left_layout)
            self.main_layout.addLayout(self.right_layout)

            if len_data <= 25:
                self.setGeometry(100, 100, 200, len_data * 10)
                for i in range(len_data):
                    data_point = QLabel(f'{self.data[i][0]}, {self.data[i][1]}')
                    data_point.setFont(QFont('Arial', 10))
                    self.left_layout.addWidget(data_point)
            else:
                self.setGeometry(100, 100, 400, len_data * 5)
                for i in range(int(len_data/2)+1):
                    data_point = QLabel(f'{self.data[i][0]}, {self.data[i][1]}')
                    data_point.setFont(QFont('Arial', 10))
                    self.left_layout.addWidget(data_point)

                for j in range(int(len_data/2)+1, len_data):
                    data_point = QLabel(f'{self.data[j][0]}, {self.data[j][1]}')
                    data_point.setFont(QFont('Arial', 10))
                    self.right_layout.addWidget(data_point)


        else:
            # is histogram or pie diagram
            len_data = len(self.data)
            self.main_layout = QVBoxLayout()
            self.setLayout(self.main_layout)
            self.setGeometry(100, 100, 300, len_data * 10)
            keys = list(self.data.keys())
            values = list(self.data.values())

            for i in range(len_data):
                data_point = QLabel(f'{keys[i]}, {values[i]}')
                data_point.setFont(QFont('Arial', 10))
                self.main_layout.addWidget(data_point)




