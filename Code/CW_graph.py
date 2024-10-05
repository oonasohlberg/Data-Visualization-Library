
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from GI_graph_item_line import GraphItemLine
from GI_graph_item_hist import GraphItemHist
from GI_graph_item_pie import GraphItemPie
from OW_info_window_line import InfoWindowLine
from OW_info_window_hist_pie import InfoWindowHistPie
from OW_show_data import ShowData

class Graph(QtWidgets.QWidget):
    """Creates widget which opens when correct file is selected"""
    def __init__(self, dia_type, graph_data):
        super().__init__()

        self.type = dia_type            # type of diagram chosen
        self.data = graph_data          # data to be plotted
        self.scene = QGraphicsScene()   # create Graphics scene
        self.graph_item = None          # define graph item
        self.axis_button = None         # define axis button
        self.sort_hist_button = None    # define sort hist button
        self.linear_model_button = None     # define linear model button
        self.info_button = None         # define info button
        self.show_data_button = None    # define show data button
        self.mean_button = None         # define mean button
        self.median_button = None       # define median button
        self.grid_button = None         # define grid button

        """initializes some values"""
        if self.type == 1:
            self.max_y = None
            self.min_y = None
            self.data_amount = None
            self.mean = None
            self.median = None
            self.data_sum = None
            self.correlation = None
        else:
            self.data_amount = None
            self.max_values = None
            self.min_values = None
            self.max_y = None
            self.min_y = None
            if self.type == 2:
                self.mean = None
                self.median = None
                self.data_sum = None
            else:
                self.mean = None
                self.median = None
                self.data_sum = None

        self.open_info_window = None
        self.open_data_window = None
        self.data_as_list = None
        self.view = None

        # Create main layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Create layout for headline
        self.up_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.up_layout)
        self.layout.addLayout(self.up_layout)

        # create back button
        self.back_button = QPushButton('Back')
        self.back_button.setStyleSheet('background-color: antiquewhite')
        self.back_button.setFont(QFont('Arial', 15))
        self.back_button.setFixedSize(QtCore.QSize(150, 70))
        self.up_layout.addWidget(self.back_button)

        # create headline
        self.headline_label = QLabel(f'\t\t\t\t\t\t{self.set_type(self.type)}')
        self.headline_label.setFont(QFont("Arial", 20))
        self.up_layout.addWidget(self.headline_label)

        # Create layout for info and diagram
        self.down_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.down_layout)
        self.layout.addLayout(self.down_layout)

        # Create layout for info
        self.info_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.info_layout)
        self.down_layout.addLayout(self.info_layout)

        # Create layout for graph
        self.diagram_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.diagram_layout)
        self.down_layout.addLayout(self.diagram_layout)
        self.add_info()
        self.draw_diagram()
        self.define_info_values()
        self.show_data()
        self.set_info_button()
        if self.type == 2:
            self.sort_hist()
        if self.type == 1:
            self.linear_line()
        if self.type == 1 or self.type == 2:
            self.add_remove_grid()
            self.add_mean_line()
            self.add_median_line()
        self.add_axis_names()

    def add_info(self):
        """Add headline"""
        if self.type == 1:
            info_label = QLabel('        Settings\n\n')
        elif self.type == 2:
            info_label = QLabel('        Settings')
        else:
            info_label = QLabel('        Settings\n\n\n\n\n\n\n\n\n\n\n')
        info_label.setFont(QFont("Arial", 25))
        self.info_layout.addWidget(info_label)

    def draw_diagram(self):
        """Creates GraphicsItem window for the diagram"""
        if self.type == 1:
            self.graph_item = GraphItemLine(self.data, self.scene)
        elif self.type == 2:
            self.graph_item = GraphItemHist(self.data, self.scene)
        else:
            self.graph_item = GraphItemPie(self.data, self.scene)

        self.scene.addItem(self.graph_item)         # adds GraphicsItem to scene
        self.view = QGraphicsView(self.scene)       # adds Graphics view as view
        self.view.setFixedSize(1200, 930)   # sets size of view
        self.diagram_layout.addWidget(self.view)    # adds view in diagram layout

    def define_info_values(self):
        """defines values for info window"""
        if self.type == 1:
            self.max_y = self.graph_item.count_data.get_y_max()
            self.min_y = self.graph_item.count_data.get_y_min()
            self.data_amount = self.graph_item.count_data.get_size_of_data()
            self.mean = self.graph_item.count_data.calc_mean()
            self.median = self.graph_item.count_data.calc_median()
            self.correlation = self.graph_item.count_data.calc_correlation()
            self.data_as_list = self.graph_item.count_data.get_as_list()
        else:
            self.data_amount = self.graph_item.count_data.get_len_data()
            self.max_values = self.graph_item.count_data.get_max_values()
            self.min_values = self.graph_item.count_data.get_min_values()
            self.max_y = self.graph_item.count_data.get_max()
            self.min_y = self.graph_item.count_data.get_min()
            if self.type == 2:
                self.mean = self.graph_item.count_data.calc_mean()
                self.median = self.graph_item.count_data.calc_median()
            else:
                self.mean = None
                self.median = None
                self.data_sum = self.graph_item.count_data.get_rounded_sum()

    def add_axis_names(self):
        """Adds name axis button"""
        if self.type == 3:
            self.axis_button = QPushButton('Name headline')
        else:
            self.axis_button = QPushButton('Name headline\n and axis')
        self.axis_button.setStyleSheet('background: pink')
        self.axis_button.setFont(QFont('Arial', 15))
        self.axis_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.axis_button)

    def sort_hist(self):
        """Creates button to sort the graph increasing"""
        self.sort_hist_button = QPushButton('Sort')
        self.sort_hist_button.setStyleSheet('background: pink')
        self.sort_hist_button.setFont(QFont('Arial', 15))
        self.sort_hist_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.sort_hist_button)
        self.sort_hist_button.clicked.connect(self.sort_hist_button_clicked)

    def linear_line(self):
        """Creates button to add linear model to graph"""
        self.linear_model_button = QPushButton('Add linear model')
        self.linear_model_button.setStyleSheet('background: pink')
        self.linear_model_button.setFont(QFont('Arial', 15))
        self.linear_model_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.linear_model_button)
        self.linear_model_button.clicked.connect(self.linear_model_button_clicked)

    def set_info_button(self):
        """Creates info button"""
        self.info_button = QPushButton('Graph information')
        self.info_button.setStyleSheet('background: pink')
        self.info_button.setFont(QFont('Arial', 15))
        self.info_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.info_button)
        self.info_button.clicked.connect(lambda: self.info_button_clicked(self.type))

    def show_data(self):
        """Creates button that shows the input data"""
        self.show_data_button = QPushButton('Show data')
        self.show_data_button.setStyleSheet('background: pink')
        self.show_data_button.setFont(QFont('Arial', 15))
        self.show_data_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.show_data_button)
        self.show_data_button.clicked.connect(self.show_data_button_clicked)

    def add_mean_line(self):
        """Adds a button for mean line"""
        self.mean_button = QPushButton('Show mean')
        self.mean_button.setStyleSheet('background: pink')
        self.mean_button.setFont(QFont('Arial', 15))
        self.mean_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.mean_button)
        self.mean_button.clicked.connect(self.mean_button_clicked)

    def add_median_line(self):
        """Adds a button for median line"""
        self.median_button = QPushButton('Show median')
        self.median_button.setStyleSheet('background: pink')
        self.median_button.setFont(QFont('Arial', 15))
        self.median_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.median_button)
        self.median_button.clicked.connect(self.median_button_clicked)

    def mean_button_clicked(self):
        """Checks if mean button is clicked"""
        if self.mean_button.text() == 'Show mean':
            self.mean_button.setText('Remove mean')
            self.graph_item.draw_mean(self.mean, self.median)
        else:
            self.mean_button.setText('Show mean')
            self.graph_item.remove_mean()

    def median_button_clicked(self):
        """Checks if median button is clicked"""
        if self.median_button.text() == 'Show median':
            self.median_button.setText('Remove median')
            self.graph_item.draw_median(self.median, self.mean)
        else:
            self.median_button.setText('Show median')
            self.graph_item.remove_median()

    def sort_hist_button_clicked(self):
        """sorts or unsorts graph when the button is clicked"""
        if self.sort_hist_button.text() == 'Sort':
            is_sorted = True
            self.sort_hist_button.setText('Original')
            self.graph_item.add_rectangles(is_sorted)
            self.graph_item.add_x_names(is_sorted)
        else:
            is_sorted = False
            self.sort_hist_button.setText('Sort')
            self.graph_item.add_rectangles(is_sorted)
            self.graph_item.add_x_names(is_sorted)

    def linear_model_button_clicked(self):
        """adds and removes linear model"""
        if self.linear_model_button.text() == 'Add linear model':
            self.linear_model_button.setText('Remove linear model')
            self.graph_item.add_linear_model()
        else:
            self.linear_model_button.setText('Add linear model')
            self.graph_item.remove_linear_model()

    def add_remove_grid(self):
        """Adds add/remove grid button"""
        self.grid_button = QPushButton("Add grid")
        self.grid_button.setStyleSheet('background: pink')
        self.grid_button.setFont(QFont('Arial', 15))
        self.grid_button.setFixedSize(QtCore.QSize(300, 100))
        self.info_layout.addWidget(self.grid_button)
        self.grid_button.clicked.connect(self.grid_button_clicked)

    def grid_button_clicked(self):
        """Adds grid/removes grid when button is clicked"""
        if self.grid_button.text() == "Add grid":
            self.grid_button.setText("Remove grid")
            self.graph_item.add_grid()
        else:
            self.grid_button.setText("Add grid")
            self.graph_item.remove_grid()

    def info_button_clicked(self, type):
        """When info button is clicked, it shows a new window containing info"""
        if type == 1:
            self.open_info_window = InfoWindowLine(self.max_y, self.min_y, self.data_amount, self.mean, self.median,
                                                   self.correlation)
            self.open_info_window.show()
        else:
            self.open_info_window = InfoWindowHistPie(type, self.data_amount, self.max_values, self.min_values, self.max_y,
                                                      self.min_y, self.mean, self.median, self.data_sum)
            self.open_info_window.show()

    def show_data_button_clicked(self):
        """Shows data in a new window when the button is clicked"""
        if self.type == 1:
            data = self.data_as_list
        else:
            data = self.graph_item.count_data.get_data()
        self.open_data_window = ShowData(data)
        self.open_data_window.show()

    def set_type(self, num):
        """Returns the type of the diagram"""
        if num == 1:
            return 'Line diagram'
        elif num == 2:
            return'Histogram'
        else:
            return'Pie diagram'
