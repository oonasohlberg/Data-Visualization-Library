from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import *
from CW_menu import Menu
from CW_file import File
from IC_check_file import GoThroughFile
from CW_graph import Graph
from OW_name_axis import NameAxisWindow
from ID_line_input import LineInput
from ID_hist_pie_input import HistPieInput
from IC_check_input_line import CheckInputLine
from IC_check_input_hist_pie import CheckInputHistPie

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Creates main window"""
        super().__init__()

        # initializes some variables
        self.its_histogram = None
        self.menu_widget = None
        self.file_diagram = None
        self.graph_widget = None
        self.add_data = None
        self.open_axis_window = None

        self.init_ui()          # opens menu window

    def init_ui(self):
        """Creates the menu widget"""
        self.its_histogram = False
        self.menu_widget = Menu()
        self.setCentralWidget(self.menu_widget)
        self.setWindowTitle(f'Oona`s data visualization library')
        self.setFixedSize(1600, 1000)
        self.show()
        self.menu_widget.buttonLineDiagram.clicked.connect(self.ClickedFileLine)
        self.menu_widget.buttonHistogram.clicked.connect(self.ClickedFileHist)
        self.menu_widget.buttonPieDiagram.clicked.connect(self.ClickedFilePie)

    def ClickedFileLine(self):
        """Checks whether buttons are clicked to change the widget"""
        self.file_diagram = File(True, 1)
        self.setCentralWidget(self.file_diagram)
        self.file_diagram.button_back.clicked.connect(self.ClickBackToMenu)
        self.file_diagram.button_file.clicked.connect(self.ChooseFileLine)
        self.file_diagram.input_data.clicked.connect(self.InputLine)

    def ClickedFileHist(self):
        """Checks whether buttons are clicked to change the widget"""
        self.its_hist()
        self.file_diagram = File(False, 2)
        self.setCentralWidget(self.file_diagram)
        self.file_diagram.button_back.clicked.connect(self.ClickBackToMenu)
        self.file_diagram.button_file.clicked.connect(self.ChooseFile)
        self.file_diagram.input_data.clicked.connect(self.InputHistPie)

    def ClickedFilePie(self):
        """Checks whether buttons are clicked to change the widget"""
        self.file_diagram = File(False, 3)
        self.setCentralWidget(self.file_diagram)
        self.file_diagram.button_back.clicked.connect(self.ClickBackToMenu)
        self.file_diagram.button_file.clicked.connect(self.ChooseFile)
        self.file_diagram.input_data.clicked.connect(self.InputHistPie)

    def ChooseFileLine(self):
        """Checks input files"""
        dialog = QFileDialog()
        dialog_success = dialog.exec()
        if dialog_success == 1:
            response = dialog.selectedFiles()
            data = response[0]
            new_file_obj = GoThroughFile(data, True)
            if new_file_obj.get_is_file_correct():
                # in case file is correct
                self.graph_widget = Graph(1, data)
                self.setCentralWidget(self.graph_widget)
                self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(1))
                self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(1))
            else:
                # if file is not correct
                self.file_diagram.add_error_message()
        else:
            # if user cancels
            pass

    def ChooseFile(self):
        """Checks input files"""
        dialog = QFileDialog()
        dialog_success = dialog.exec()
        if dialog_success == 1:
            response = dialog.selectedFiles()
            data = response[0]
            new_file_obj = GoThroughFile(data, False)
            if new_file_obj.get_is_file_correct():
                # in case file is correct
                if self.its_histogram:
                    self.graph_widget = Graph(2, data)
                    self.setCentralWidget(self.graph_widget)
                    self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(2))
                    self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(2))
                else:
                    self.graph_widget = Graph(3, data)
                    self.setCentralWidget(self.graph_widget)
                    self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(3))
                    self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(3))
            else:
                # if file is not correct
                self.file_diagram.add_error_message()
        else:
            # if user cancels
            pass

    def InputLine(self):
        """Shows input data window when write data is clicked"""
        self.add_data = LineInput()
        self.add_data.show()
        self.add_data.ok_button.clicked.connect(self.OkInputLine)

    def InputHistPie(self):
        """Shows input data window when write data is clicked"""
        self.add_data = HistPieInput()
        self.add_data.show()
        self.add_data.ok_button.clicked.connect(self.OkInputHistPie)

    def OkInputLine(self):
        """Saves the input and creates Graph as a central widget"""
        data_list = []
        self.add_data.close()
        data_list_temp = self.add_data.get_data_list()
        for i in data_list_temp:
            if i.text() != '':
                data_list.append(i.text())

        check_data = CheckInputLine(data_list)
        if not check_data.get_is_correct():
            # if data is incorrect
            self.file_diagram.add_error_message()
        else:
            # if data is correct
            self.graph_widget = Graph(1, check_data.get_data_list())
            self.setCentralWidget(self.graph_widget)
            self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(1))
            self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(1))

    def OkInputHistPie(self):
        """Saves the input and creates Graph as a central widget"""
        data_list = []
        self.add_data.close()
        data_list_temp = self.add_data.get_data_list()
        for i in data_list_temp:
            if i.text() != '':
                data_list.append(i.text())

        check_data = CheckInputHistPie(data_list)
        if not check_data.get_is_correct():
            # if data is incorrect
            self.file_diagram.add_error_message()

        else:
            # if data is correct
            if self.its_histogram:
                self.graph_widget = Graph(2, check_data.get_data_list())
                self.setCentralWidget(self.graph_widget)
                self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(2))
                self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(2))
            else:
                self.graph_widget = Graph(3, check_data.get_data_list())
                self.setCentralWidget(self.graph_widget)
                self.graph_widget.back_button.clicked.connect(lambda: self.BackToFile(3))
                self.graph_widget.axis_button.clicked.connect(lambda: self.AxisButton(3))

    def its_hist(self):
        """sets the boolean value as True for histogram"""
        self.its_histogram = True

    def ClickBackToMenu(self):
        """Makes clicking back button go back to menu window"""
        self.init_ui()

    def BackToFile(self, num):
        """Makes clicking back button go back to select file -window"""
        if num == 1:
            self.ClickedFileLine()
        elif num == 2:
            self.ClickedFileHist()
        else:
            self.ClickedFilePie()

    def AxisButton(self, num):
        """Shows name axis window when 'Name labels' button is clicked"""
        if (self.graph_widget.axis_button.text() == 'Name headline\n and axis' or
                self.graph_widget.axis_button.text() == 'Name headline'):
            self.open_axis_window = NameAxisWindow(num)
            self.open_axis_window.show()
            self.open_axis_window.ok_button.clicked.connect(lambda: self.OkButtonClicked(num))
        else:
            self.open_axis_window = NameAxisWindow(num)
            self.open_axis_window.show()
            self.open_axis_window.ok_button.clicked.connect(lambda: self.OkButtonClicked(num))

    def OkButtonClicked(self, num):
        """Saves the names of diagram and axis. Then gives them to graphic item"""
        self.graph_widget.graph_item.remove_old_names()
        headline = self.open_axis_window.headline.text()
        self.open_axis_window.close()
        if num == 1 or num == 2:
            self.graph_widget.axis_button.setText('Rename headline\n'
                                                  'and axis')
        else:
            self.graph_widget.axis_button.setText('Rename headline')
        if num == 1:
            x_lab = self.open_axis_window.x_edit.text()
            y_lab = self.open_axis_window.y_edit.text()
            self.graph_widget.graph_item.set_names(headline, x_lab, y_lab)
        elif num == 2:
            y_lab = self.open_axis_window.y_edit.text()
            self.graph_widget.graph_item.set_names(headline, y_lab)
        else:
            self.graph_widget.graph_item.set_names(headline)

