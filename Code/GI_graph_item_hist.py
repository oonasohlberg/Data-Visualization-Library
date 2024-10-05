from PyQt6.QtWidgets import QGraphicsLineItem, QGraphicsRectItem
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QPen, QColor
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
from DC_hist_pie_data import HistPieData

class GraphItemHist(QtWidgets.QGraphicsItem):
    def __init__(self, data, scene):
        """Makes the graphics item window for the diagram"""
        super().__init__()

        self.scene = scene                          # adds scene parameter as self.scene
        self.data = data                            # data to be plotted
        self.count_data = HistPieData(self.data)    # does some counting for data

        # initializes some variables
        self.headline = None
        self.y_axis = None
        self.rect_list = []
        self.name_list = []
        self.is_sorted = False
        self.grid_list = []
        self.mean_line = None
        self.mean_text = None
        self.median_line = None
        self.median_text = None

        # gets data and data in order
        self.data_list = self.count_data.get_data()
        self.sorted_data_inc = self.count_data.sort_increasing()

        # coordinates for the graph
        self.size_of_grid = 20
        self.x_line_x_start = 600
        self.x_line_x_end = 1400
        self.x_line_y = 970
        self.width_x = self.x_line_x_end - self.x_line_x_start

        self.y_line_y_start = 970
        self.y_line_y_end = 170
        self.y_line_x = 600
        self.width_y = self.y_line_y_start - self.y_line_y_end

        # create graph
        self.add_axis()
        self.add_coord_lines()
        self.add_rectangles(self.is_sorted)
        self.add_axis_nums()
        self.add_x_names(self.is_sorted)
        self.add_names_default()
        self.create_grid()

    def add_axis(self):
        """Adds axis"""
        x_line = QGraphicsLineItem(self.x_line_x_start, self.x_line_y,
                                   self.x_line_x_end, self.x_line_y)
        pen = QPen()
        pen.setWidthF(3)
        x_line.setPen(pen)
        self.scene.addItem(x_line)

        y_line = QGraphicsLineItem(self.y_line_x, self.y_line_y_start,
                                   self.y_line_x, self.y_line_y_end)
        pen = QPen()
        pen.setWidthF(3)
        y_line.setPen(pen)
        self.scene.addItem(y_line)

    def add_coord_lines(self):
        """Adds the small lines in axis"""
        j = 0
        while j <= self.width_y:
            y_small_line = QGraphicsLineItem(self.y_line_x - 5, self.y_line_y_start-j, self.y_line_x + 5, self.y_line_y_start-j)
            pen = QPen()
            pen.setWidthF(3)
            y_small_line.setPen(pen)
            self.scene.addItem(y_small_line)
            j += 100

    def set_names(self, h, y):
        """Sets headline and name for y-axis"""
        self.headline = QGraphicsTextItem(h)
        self.y_axis = QGraphicsTextItem(y)

        self.headline.setFont(QFont('Arial', 20))
        self.y_axis.setFont(QFont('Arial', 15))

        self.headline.moveBy(900, 130)
        self.scene.addItem(self.headline)

        self.y_axis.setRotation(270)
        self.y_axis.moveBy(520, 600)
        self.scene.addItem(self.y_axis)

    def add_names_default(self):
        """adds default headline and y-axis name"""
        self.headline = QGraphicsTextItem('Headline')
        self.y_axis = QGraphicsTextItem('y-axis')

        self.headline.setFont(QFont('Arial', 20))
        self.y_axis.setFont(QFont('Arial', 15))

        self.headline.moveBy(900, 130)
        self.scene.addItem(self.headline)

        self.y_axis.setRotation(270)
        self.y_axis.moveBy(520, 600)
        self.scene.addItem(self.y_axis)

    def create_grid(self):
        """create grid"""
        self.grid_list = []
        l = 0
        while l <= self.width_y:
            y_grid = QGraphicsLineItem(self.y_line_x+l, self.y_line_y_start, self.y_line_x+l, self.y_line_y_end)
            if l in [0, 100, 200, 300, 400, 500, 600, 700, 800]:
                pen = QPen()
                pen.setWidthF(1.5)
            else:
                pen = QPen()
                pen.setWidthF(0.5)
            y_grid.setPen(pen)
            self.grid_list.append(y_grid)
            l += self.size_of_grid
        i = 0
        while i <= self.width_x:
            x_grid = QGraphicsLineItem(self.x_line_x_start, self.x_line_y-i, self.x_line_x_end, self.x_line_y-i)
            if i in [0, 100, 200, 300, 400, 500, 600, 700, 800]:
                pen = QPen()
                pen.setWidthF(1.5)
            else:
                pen = QPen()
                pen.setWidthF(0.5)
            x_grid.setPen(pen)
            self.grid_list.append(x_grid)
            i += self.size_of_grid

    def add_grid(self):
        """adds grid when its clicked"""
        for item in self.grid_list:
            self.scene.addItem(item)

    def remove_grid(self):
        """Removes grid"""
        for item in self.grid_list:
            self.scene.removeItem(item)

    def add_rectangles(self, is_sorted):
        """Adds rectangles"""
        data_size = self.count_data.get_len_data()
        if len(self.rect_list) != 0:
            for item in self.rect_list:
                self.scene.removeItem(item)
        self.rect_list = []

        if is_sorted:           # if sort button is clicked
            data_list = list(self.sorted_data_inc.values())
        else:
            data_list = list(self.data_list.values())

        width_x = self.width_x/data_size
        for i in range(data_size):
            y_value = data_list[i]
            x1 = self.x_line_x_start + i * width_x
            y1 = self.x_line_y - (y_value/self.count_data.get_max())*self.width_y
            x2 = x1 + width_x
            y2 = self.x_line_y
            rect = QGraphicsRectItem(x1, y1, x2 - x1, y2 - y1)
            if 1 <= data_size < 6:
                rect.setBrush(QColor(240, 255, 224))
            elif 6 <= data_size < 11:
                rect.setBrush(QColor(255, 255, 204))
            elif 11 <= data_size < 16:
                rect.setBrush(QColor(224, 240, 255))
            else:
                rect.setBrush(QColor(255, 240, 224))
            self.rect_list.append(rect)
            self.scene.addItem(rect)

    def add_axis_nums(self):
        """Adds numbers to y-axis"""
        y_axis_nums = self.count_data.get_y_axis_nums()
        width_y = 0
        for num in y_axis_nums:
            rounded_num = self.count_data.round_num(num)
            num_len = self.count_data.num_length(str(rounded_num))
            point_y = QGraphicsTextItem(str(rounded_num))
            point_y.setFont(QFont("Arial", 12))
            point_y.moveBy(565 - num_len**1.9, self.x_line_y-15-width_y)
            self.scene.addItem(point_y)
            width_y += 100

    def add_x_names(self, is_sorted):
        """adds names for x-values"""
        if len(self.name_list) != 0:
            for item in self.name_list:
                self.scene.removeItem(item)
        self.name_list = []

        if is_sorted:           # if sort button is clicked
            data_list = list(self.sorted_data_inc.keys())
        else:
            data_list = list(self.data_list.keys())
        i = 0
        for name in data_list:
            cutted_name = name[0:9]
            x_name = QGraphicsTextItem(cutted_name)
            x_name.setFont(QFont("Arial", 11))
            x_name.moveBy(self.y_line_x + 5 + i*(self.width_x/self.count_data.get_len_data()), self.x_line_y + 43)
            x_name.setRotation(330)
            self.name_list.append(x_name)
            self.scene.addItem(x_name)
            i += 1

    def remove_old_names(self):
        """removes old headline and y-axis name when new are added"""
        self.scene.removeItem(self.headline)
        self.scene.removeItem(self.y_axis)

    def draw_mean(self, mean, median):
        """Draws a mean line"""
        scaled_mean = self.x_line_y - (mean/self.count_data.get_max())*self.width_y

        self.mean_line = QGraphicsLineItem(self.x_line_x_start, scaled_mean, self.x_line_x_end, scaled_mean)
        pen = QPen()
        pen.setWidthF(2)
        self.mean_line.setPen(pen)
        self.scene.addItem(self.mean_line)

        self.mean_text = QGraphicsTextItem(f'mean: {mean}')
        self.mean_text.setDefaultTextColor(QColor(199, 21, 133))
        self.mean_text.setFont(QFont('Arial', 12))
        if mean >= median:
            self.mean_text.moveBy(self.x_line_x_start + 15, scaled_mean - 25)
        else:
            self.mean_text.moveBy(self.x_line_x_start + 15, scaled_mean)
        self.scene.addItem(self.mean_text)

    def remove_mean(self):
        """Removes a mean line"""
        self.scene.removeItem(self.mean_line)
        self.scene.removeItem(self.mean_text)

    def draw_median(self, median, mean):
        """Draws a median line"""
        scaled_median = self.x_line_y - (median/self.count_data.get_max())*self.width_y
        self.median_line = QGraphicsLineItem(self.x_line_x_start, scaled_median, self.x_line_x_end, scaled_median)
        pen = QPen()
        pen.setWidthF(2)
        self.median_line.setPen(pen)
        self.scene.addItem(self.median_line)

        self.median_text = QGraphicsTextItem(f'median: {median}')
        self.median_text.setFont(QFont('Arial', 12))
        self.median_text.setDefaultTextColor(QColor(0, 139, 139))
        if median > mean:
            self.median_text.moveBy(self.x_line_x_start + 15, scaled_median - 25)
        else:
            self.median_text.moveBy(self.x_line_x_start + 15, scaled_median)
        self.scene.addItem(self.median_text)

    def remove_median(self):
        """Removes a median line"""
        self.scene.removeItem(self.median_line)
        self.scene.removeItem(self.median_text)

    def boundingRect(self):
        """implemented bounding rect"""
        return QRectF(500, 500, 100, 530)
