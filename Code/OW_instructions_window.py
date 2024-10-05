
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class InstructionsLine(QWidget):
    def __init__(self):
        """Instructions for line diagram"""
        super().__init__()

        # create instructions window geometry and layout
        self.setGeometry(1050, 100, 500, 420)
        self.setWindowTitle('Instructions')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        decimal_point = str('"."')
        comma = str('","')

        instructions = QLabel('Data point: x-value, y-value\n\n'
                              'General:\n\n'
                              '• Each data point contains two values: x-value, y-value\n'
                              f'   separated by comma: {comma}\n\n'
                              '• Amount of data points: between 2 and 50 (inclusive)\n'
                              '• Values: between -9999999 and 9999999 (inclusive)\n\n'
                              '• The minimum x-value and maximum x-value cannot be the same\n'
                              '• The minimum y-value and maximum y-value cannot be the same\n\n'
                              '• Values can be integers or floating-point numbers\n'
                              '• Decimal places shown at most: 7\n'
                              f'• Decimal point format: {decimal_point}\n\n'
                              'Write data:\n\n'
                              '• Each line should have two numbers in the format: x-value, y-value\n'
                              '   where x-value and y-value are numbers as described above.\n\n'
                              'Select file:\n\n'
                              '• The file should only contain lines in format: x-value, y-value\n'
                              '   where x-value and y-value are numbers as described above.\n')
        instructions.setFont(QFont('Arial', 12))
        self.layout.addWidget(instructions)


class InstructionsHist(QWidget):
    def __init__(self):
        """Instructions for histogram"""
        super().__init__()

        # create instructions window geometry and layout
        self.setGeometry(950, 100, 500, 370)
        self.setWindowTitle('Instructions')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        decimal_point = str('"."')
        empty = str('" "')
        comma = str('","')

        instructions = QLabel('Data point: x-value, y-value\n\n'
                              'General:\n\n'
                              '• Each data point contains two values: x-value, y-value\n'
                              f'   separated by comma: {comma}\n\n'
                              '• Amount of data points: between 1 and 20 (inclusive)\n'
                              '• y-values: between 0 and 10000 (inclusive, positive values only)\n\n'
                              '• Values can be integers or floating-point numbers\n'
                              '• Decimal places shown at most in the graph: 7\n'
                              f'• Decimal point format: {decimal_point}\n\n'
                              f'• x-value should not be empty string: {empty} \n'
                              f'• All x-values should be unique and different from each other\n'
                              '• From x-value, the first 10 characters will be shown in the graph\n\n'
                              'Write data:\n\n'
                              '• Each line should have a value and a number in the format: x-value, y-value\n'
                              '   where "x-value" can be, for example, a word or a number, and "y-value" is a number\n\n'
                              'Select file:\n\n'
                              '• The file should only contain lines in format: x-value, y-value\n'
                              '   where "x-value" can be, for example, a word or a number, and "y-value" is a number')

        instructions.setFont(QFont('Arial', 12))
        self.layout.addWidget(instructions)

class InstructionsPie(QWidget):
    def __init__(self):
        """Instructions for pie diagram"""
        super().__init__()

        # create instructions window geometry and layout
        self.setGeometry(950, 100, 500, 370)
        self.setWindowTitle('Instructions')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        decimal_point = str('"."')
        empty = str('" "')
        comma = str('","')

        instructions = QLabel('Data point: x-value, y-value\n\n'
                              'General:\n\n'
                              '• Each data point contains two values: x-value, y-value\n'
                              f'   separated by comma: {comma}\n\n'
                              '• Amount of data points: between 1 and 20 (inclusive)\n'
                              '• y-values: between 0 and 10000 (inclusive, positive values only)\n\n'
                              '• Values can be integers or floating-point numbers\n'
                              '• Decimal places shown at most in the graph: 7\n'
                              f'• Decimal point format: {decimal_point}\n\n'
                              f'• x-value should not be empty string: {empty} \n'
                              f'• All x-values should be unique and different from each other\n'
                              '• From x-value, the first 15 characters will be shown in the graph\n\n'
                              'Write data:\n\n'
                              '• Each line should have a value and a number in the format: x-value, y-value\n'
                              '   where "x-value" can be, for example, a word or a number, and "y-value" is a number\n\n'
                              'Select file:\n\n'
                              '• The file should only contain lines in format: x-value, y-value\n'
                              '   where "x-value" can be, for example, a word or a number, and "y-value" is a number')

        instructions.setFont(QFont('Arial', 12))
        self.layout.addWidget(instructions)