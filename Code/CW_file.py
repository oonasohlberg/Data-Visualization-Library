
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from OW_instructions_window import InstructionsHist, InstructionsLine, InstructionsPie

class File(QtWidgets.QWidget):
    """Creates widget where user chooses the file"""
    def __init__(self, line, type):
        super().__init__()

        # create main layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.is_line = line                         # true if graph is line diagram
        self.warning_message_exists = False         # no warning message by default
        self.type = type                            # type of diagram

        self.default_error_msg = None               # sets default error message as None
        self.inst_window = None                     # define the instruction window

        # Create two layouts, one for text and one for button
        self.layout_up = QtWidgets.QHBoxLayout()
        self.layout_middle = QtWidgets.QVBoxLayout()
        self.layout_down = QtWidgets.QVBoxLayout()

        self.layout.addLayout(self.layout_up)
        self.layout.addLayout(self.layout_middle)
        self.layout.addLayout(self.layout_down)

        # create head text
        if type == 1:
            head_text = 'line diagram'
        elif type == 2:
            head_text = 'histogram'
        else:
            head_text = 'pie diagram'

        fill_empty_space = QLabel('\n')      # fills some empty space in layout

        # Create text
        self.headline = QLabel(f'\n\n\n\n\t\t Add the data you want to visualize for the {head_text}\n\t\t\t'
                               f'     by typing it or uploading a file\n\n\n\n')

        self.headline.setFont(QFont('Arial', 30))
        self.layout_middle.addWidget(self.headline)

        # sets default error msg
        self.default_error_msg = self.layout_middle.warning_label = QtWidgets.QLabel("\t")
        self.default_error_msg.setFont(QFont('Arial', 20))
        self.layout_middle.addWidget(self.default_error_msg)

        # add input data button
        self.input_data = QPushButton('Write data')
        self.input_data.setStyleSheet('background: lightblue')
        self.input_data.setFont(QFont('Arial', 25))

        self.input_data.setFixedSize(QtCore.QSize(1580, 150))

        self.layout_down.addWidget(fill_empty_space)
        self.layout_down.addWidget(self.input_data)
        self.layout_down.addWidget(fill_empty_space)

        # add the file button
        self.button_file = QPushButton('Select file')
        self.button_file.setStyleSheet('background: lightblue')
        self.button_file.setFont(QFont('Arial', 25))
        self.button_file.setFixedSize(QtCore.QSize(1580, 150))
        self.layout_down.addWidget(fill_empty_space)
        self.layout_down.addWidget(self.button_file)
        self.layout_down.addWidget(fill_empty_space)

        # Go back to menu
        self.button_back = QPushButton('Back to menu')
        self.button_back.setStyleSheet('background-color: antiquewhite')
        self.button_back.setFont(QFont('Arial', 15))
        self.button_back.setFixedSize(QtCore.QSize(150, 70))
        self.layout_up.addWidget(self.button_back)
        self.layout_up.addWidget(fill_empty_space)

        # Adds instructions button in layout_up
        label_instructions = QPushButton('Instructions for input data')
        label_instructions.setStyleSheet('background-color: antiquewhite')
        label_instructions.setFont(QFont('Arial', 15))
        label_instructions.setFixedSize(QtCore.QSize(300, 70))
        self.layout_up.addWidget(label_instructions)

        label_instructions.clicked.connect(lambda: self.instructions_clicked(self.type))


    def change_is_line(self):
        """returns True if chosen visualization is line diagram"""
        self.is_line = True
        return self.is_line

    def add_error_message(self):
        """prints an error message if the file is invalid"""
        if not self.warning_message_exists:
            self.warning_message_exists = True
            self.layout_middle.removeWidget(self.default_error_msg)
            warning_text = self.layout_middle.warning_label = (
                QtWidgets.QLabel("\t\t\t\t\t             Wrong kind of file or data"))
            warning_text.setFont(QFont('Arial', 20))
            warning_text.setStyleSheet('color: red')
            self.layout_middle.addWidget(warning_text)

    def instructions_clicked(self, num):
        """When the instructions button is clicked, it opens an instruction window"""
        if num == 1:
            self.inst_window = InstructionsLine()
        elif num == 2:
            self.inst_window = InstructionsHist()
        else:
            self.inst_window = InstructionsPie()
        self.inst_window.show()

