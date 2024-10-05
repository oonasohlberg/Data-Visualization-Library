
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *



class InfoWindowLine(QWidget):
    """Shows information about the line data when clicked"""
    def __init__(self, max_y, min_y, amount, mean, median, correlation):
        super().__init__()

        # create info window geometry and layout
        self.setGeometry(50, 100, 400, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # gets these values as parameters
        self.max_y = max_y
        self.min_y = min_y
        self.len_data = amount
        self.mean = mean
        self.median = median
        self.correlation = correlation

        self.setWindowTitle('Information about the line diagram')

        # amount of data points
        amount_of_data = QLabel('Amount of data points:\n\n'
                                f'{self.len_data}\n')
        amount_of_data.setFont(QFont('Arial', 12))
        self.layout.addWidget(amount_of_data)

        # mean
        mean = QLabel('Mean:\n\n'
                      f'{self.mean}\n')
        mean.setFont(QFont('Arial', 12))
        self.layout.addWidget(mean)

        # median
        median = QLabel('Median:\n\n'
                        f'{self.median}\n')
        median.setFont(QFont('Arial', 12))
        self.layout.addWidget(median)

        # correlation
        cor = QLabel('Linear correlation:\n\n'
                     f'{self.correlation}\n')
        cor.setFont(QFont('Arial', 12))
        self.layout.addWidget(cor)

        # max value
        max_value = QLabel('Maximum value:\n\n'
                           f'{self.max_y}\n')
        max_value.setFont(QFont('Arial', 12))
        self.layout.addWidget(max_value)

        # min value
        min_value = QLabel('Minimum value:\n\n'
                           f'{self.min_y}\n')
        min_value.setFont(QFont('Arial', 12))
        self.layout.addWidget(min_value)
