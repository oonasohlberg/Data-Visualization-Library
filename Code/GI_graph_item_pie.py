
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
from DC_hist_pie_data import HistPieData

class GraphItemPie(QtWidgets.QGraphicsItem):
    """Makes the graphics item window for the diagram"""
    def __init__(self, data, scene):
        """Create scene and create HistPieData object that counts the necessary information"""
        super().__init__()

        self.scene = scene                           # adds scene parameter as self.scene
        self.data = data
        self.count_data = HistPieData(self.data)    # does some counting for data

        # initializes headline
        self.headline = None

        # defines coordinates for the graph
        self.x_start = 800
        self.y_start = 100
        self.width = 650
        self.length = 650

        self.rect_width = 20
        self.rect_height = 20
        self.rect_start_x = 450
        self.rect_start_y = 50
        self.rect_dist = 40

        # gets data and data as increasing
        self.data_sum = self.count_data.count_sum_data()
        self.sorted_data_inc = self.count_data.sort_increasing()

        # create the graph
        self.color_list = self.create_pie_colors()
        self.create_pie()
        self.add_color_rect()
        self.add_names()
        self.add_percentages()
        self.add_headline_default()


    def set_names(self, h):
        """Sets headline"""
        self.headline = QGraphicsTextItem(h)
        self.headline.setFont(QFont('Arial', 20))
        self.headline.moveBy(800, 1)
        self.scene.addItem(self.headline)

    def add_headline_default(self):
        """sets default headline"""
        self.headline = QGraphicsTextItem('Headline')
        self.headline.setFont(QFont('Arial', 20))
        self.headline.moveBy(800, 1)
        self.scene.addItem(self.headline)

    def create_pie_colors(self):
        """Defines 20 colors in a list"""
        # this list is made by ChatGPT
        colors = [
            QColor(255, 204, 153),   # Light Apricot
            QColor(204, 255, 153),   # Light Lime Green
            QColor(153, 204, 255),   # Light Baby Blue
            QColor(255, 255, 153),   # Light Yellow
            QColor(255, 153, 204),   # Light Pink
            QColor(153, 255, 255),   # Light Cyan
            QColor(255, 204, 153),   # Light Peach
            QColor(204, 153, 255),   # Light Lavender
            QColor(255, 204, 204),   # Light Salmon
            QColor(204, 255, 204),   # Light Mint
            QColor(204, 204, 255),   # Light Lavender Blue
            QColor(255, 255, 204),   # Light Beige
            QColor(255, 204, 255),   # Light Orchid
            QColor(204, 255, 255),   # Light Aqua
            QColor(255, 224, 153),   # Light Orange
            QColor(224, 153, 255),   # Light Violet
            QColor(153, 255, 224),   # Light Seafoam Green
            QColor(255, 153, 224),   # Light Rose
            QColor(153, 224, 255),   # Light Celeste
            QColor(255, 204, 153)    # Light Tan
            ]
        return colors

    def get_color_list(self):
        """returns color list"""
        return self.color_list

    def create_pie(self):
        """creates the pie"""
        data_len = self.count_data.get_len_data()
        data = self.sorted_data_inc

        increase = 0
        for i in range(data_len):
            circle = QGraphicsEllipseItem(self.x_start, self.y_start, self.width, self.length)
            circle.setStartAngle(90*16 + int(increase))
            circle.setSpanAngle(int((list(data.values())[i]/self.data_sum)*360*16))
            circle.setBrush(self.color_list[i])
            self.scene.addItem(circle)
            increase += (list(data.values())[i]/self.data_sum)*360*16

    def add_color_rect(self):
        """adds small rectangles with color in pie"""
        data_len = self.count_data.get_len_data()

        for i in range(data_len):
            rect = QGraphicsRectItem(self.rect_start_x, self.rect_start_y + i * self.rect_dist,
                                     self.rect_width, self.rect_height)
            rect.setBrush(self.color_list[data_len - 1 - i])
            self.scene.addItem(rect)

    def add_names(self):
        """Adds names (keys) next to color rectangles"""
        data = self.sorted_data_inc
        data_len = self.count_data.get_len_data()
        for i in range(data_len):
            text = QGraphicsTextItem(list(data.keys())[data_len - 1 - i][0:15])
            text.setFont(QFont("Arial", 12))
            text.moveBy(self.rect_start_x + 30, self.rect_start_y - 3 + i * self.rect_dist)
            self.scene.addItem(text)

    def add_percentages(self):
        """calculate the percentages of the data"""
        data = self.sorted_data_inc
        data_len = self.count_data.get_len_data()
        for i in range(data_len):
            percentage = float(round(100 * float(list(data.values())[data_len - 1 - i])/self.data_sum, 1))
            str_percentage = QGraphicsTextItem(str(percentage) + '%')
            str_percentage.setFont(QFont("Arial", 12))
            str_percentage.moveBy(self.rect_start_x + 240, self.rect_start_y - 3 + i * self.rect_dist)
            self.scene.addItem(str_percentage)

    def remove_old_names(self):
        """removes old headline when new is added"""
        self.scene.removeItem(self.headline)

    def boundingRect(self):
        """implemented bounding rect"""
        return QRectF(500, 500, 100, 200)




