
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *



class InfoWindowHistPie(QWidget):
    """Shows information about the line data when clicked"""
    def __init__(self, num, data_len, max_values, min_values, max_y, min_y, mean, median, data_sum):
        super().__init__()

        # gets these values as parameters
        self.type = num
        self.data_len = data_len
        self.max_values = max_values
        self.min_values = min_values
        self.max_y = max_y
        self.min_y = min_y
        self.mean = mean
        self.median = median
        self.data_sum = data_sum

        # setting the window size based on the amount of data to be printed
        self.setGeometry(50, 100, 400, 200 + (len(self.max_values) + len(self.min_values)) * 50)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        if num == 2:
            self.setWindowTitle('Information about the histogram')
        else:
            self.setWindowTitle('Information about the pie diagram')

        # amount of data points
        amount_of_data = QLabel('Amount of data points:  \n\n'
                                f'{self.data_len}\n')
        amount_of_data.setFont(QFont('Arial', 12))
        self.layout.addWidget(amount_of_data)

        # mean and median for histogram
        if self.mean is not None and self.median is not None:
            mean_text = QLabel('Mean: \n\n'
                               f'{self.mean}\n')
            mean_text.setFont(QFont('Arial', 12))
            self.layout.addWidget(mean_text)

            median_text = QLabel('Median: \n\n'
                                 f'{self.median}\n')
            median_text.setFont(QFont('Arial', 12))
            self.layout.addWidget(median_text)

        # set value sum for pie
        if self.data_sum is not None:
            sum_text = QLabel('Value sum: \n\n'
                              f'{self.data_sum}\n\n')
            sum_text.setFont(QFont('Arial', 12))
            self.layout.addWidget(sum_text)

        # max values
        if len(self.max_values) > 1:
            max_y = QLabel('Have maximum value:\n')
        else:
            max_y = QLabel('Has maximum value:\n')
        max_y.setFont(QFont('Arial', 12))
        self.layout.addWidget(max_y)
        for item in self.max_values:
            max_value = QLabel(f'{item}\n')
            max_value.setFont(QFont('Arial', 11))
            self.layout.addWidget(max_value)
        freq_max = QLabel(f'Maximum value:  \n\n'
                          f'{self.max_y}\n\n')
        freq_max.setFont(QFont('Arial', 12))
        self.layout.addWidget(freq_max)

        # min values
        if len(self.min_values) > 1:
            min_y = QLabel('Have minimum value:\n')
        else:
            min_y = QLabel('Has minimum value:\n')
        min_y.setFont(QFont('Arial', 12))
        self.layout.addWidget(min_y)
        for item in self.min_values:
            min_value = QLabel(f'{item}\n')
            min_value.setFont(QFont('Arial', 11))
            self.layout.addWidget(min_value)
        freq_min = QLabel(f'Minimum value: \n\n '
                          f'{self.min_y}\n\n')
        freq_min.setFont(QFont('Arial', 12))
        self.layout.addWidget(freq_min)
