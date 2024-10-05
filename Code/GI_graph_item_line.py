from PyQt6.QtWidgets import QGraphicsLineItem, QGraphicsEllipseItem
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QPen, QColor
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
from DC_line_data import LineData

class GraphItemLine(QtWidgets.QGraphicsItem):
    """Makes the graphics item window for the line diagram"""
    def __init__(self, data, scene):
        """Create scene and create LineData object that counts the necessary information"""
        super().__init__()
        self.scene = scene                       # adds scene parameter as self.scene
        self.data = data                         # data to be plotted
        self.count_data = LineData(self.data)    # does some counting for data

        # initializes some variables
        self.x_grid = None
        self.y_grid = None
        self.size_of_grid = 20
        self.grid_list = []
        self.radius = 5
        self.headline = None
        self.y_axis = None
        self.x_axis = None
        self.lin_reg_line = None
        self.mean_line = None
        self.mean_text = None
        self.median_line = None
        self.median_text = None

        # Define the coordinates of axis
        self.axis_marginal = 10

        self.x_line_x_start = self.count_data.x_start - self.axis_marginal
        self.x_line_x_end = self.count_data.x_end + self.axis_marginal
        self.x_line_y = self.count_data.y_start + self.axis_marginal
        self.width_x = self.x_line_x_end - self.x_line_x_start

        self.y_line_y_start = self.count_data.y_start + self.axis_marginal
        self.y_line_y_end = self.count_data.y_end - self.axis_marginal
        self.y_line_x = self.count_data.x_start - self.axis_marginal
        self.width_y = self.y_line_y_start - self.y_line_y_end

        # create graph
        self.add_axis()
        self.add_pointer()
        self.add_coord_lines()
        self.create_data_points()
        self.create_connecting_lines()
        self.add_axis_nums()
        self.add_names_default()
        self.create_grid()
        self.create_lin_reg_line()

    def add_axis(self):
        """Adds axis"""
        x_line = QGraphicsLineItem(self.x_line_x_start, self.x_line_y, self.x_line_x_end, self.x_line_y)
        pen = QPen()
        pen.setWidthF(3)
        x_line.setPen(pen)
        self.scene.addItem(x_line)

        y_line = QGraphicsLineItem(self.y_line_x, self.y_line_y_start, self.y_line_x, self.y_line_y_end)
        pen = QPen()
        pen.setWidthF(3)
        y_line.setPen(pen)
        self.scene.addItem(y_line)

    def add_pointer(self):
        """Adds pointer in x- and y-axis"""
        x_r = QGraphicsLineItem(self.x_line_x_end, self.x_line_y, self.x_line_x_end - 3, self.x_line_y + 3)
        pen = QPen()
        pen.setWidthF(2)
        x_r.setPen(pen)
        self.scene.addItem(x_r)

        x_l = QGraphicsLineItem(self.x_line_x_end, self.x_line_y, self.x_line_x_end - 3, self.x_line_y - 3)
        pen = QPen()
        pen.setWidthF(2)
        x_l.setPen(pen)
        self.scene.addItem(x_l)

        y_l = QGraphicsLineItem(self.y_line_x, self.y_line_y_end, self.y_line_x - 3, self.y_line_y_end + 3)
        pen = QPen()
        pen.setWidthF(2)
        y_l.setPen(pen)
        self.scene.addItem(y_l)

        y_r = QGraphicsLineItem(self.y_line_x, self.y_line_y_end, self.y_line_x + 3, self.y_line_y_end + 3)
        pen = QPen()
        pen.setWidthF(2)
        y_r.setPen(pen)
        self.scene.addItem(y_r)

    def add_coord_lines(self):
        """Adds small lines in axis"""
        x_first_line = QGraphicsLineItem(self.x_line_x_start + self.axis_marginal, self.x_line_y - 5,
                                         self.x_line_x_start + self.axis_marginal, self.x_line_y + 5)
        pen = QPen()
        pen.setWidthF(3)
        x_first_line.setPen(pen)
        self.scene.addItem(x_first_line)

        x_last_line = QGraphicsLineItem(self.x_line_x_end - self.axis_marginal, self.x_line_y - 5,
                                        self.x_line_x_end - self.axis_marginal, self.x_line_y + 5)
        pen = QPen()
        pen.setWidthF(3)
        x_last_line.setPen(pen)
        self.scene.addItem(x_last_line)

        y_first_line = QGraphicsLineItem(self.y_line_x - 5, self.y_line_y_start - self.axis_marginal,
                                         self.y_line_x + 5, self.y_line_y_start - self.axis_marginal)
        pen = QPen()
        pen.setWidthF(3)
        y_first_line.setPen(pen)
        self.scene.addItem(y_first_line)

        y_last_line = QGraphicsLineItem(self.y_line_x - 5, self.y_line_y_end + self.axis_marginal,
                                        self.y_line_x + 5, self.y_line_y_end + self.axis_marginal)
        pen = QPen()
        pen.setWidthF(3)
        y_last_line.setPen(pen)
        self.scene.addItem(y_last_line)

        i = 100
        while i <= 700:
            x_small_line = QGraphicsLineItem(self.x_line_x_start+i, self.x_line_y - 5,
                                             self.x_line_x_start+i, self.x_line_y + 5)
            pen = QPen()
            pen.setWidthF(3)
            x_small_line.setPen(pen)
            self.scene.addItem(x_small_line)
            i += 100

        j = 100
        while j <= 700:
            y_small_line = QGraphicsLineItem(self.y_line_x - 5, self.y_line_y_start-j,
                                             self.y_line_x + 5, self.y_line_y_start-j)
            pen = QPen()
            pen.setWidthF(3)
            y_small_line.setPen(pen)
            self.scene.addItem(y_small_line)
            j += 100

    def add_names_default(self):
        """Adds default axis names and headline"""
        self.headline = QGraphicsTextItem('Headline')
        self.x_axis = QGraphicsTextItem('x-axis')
        self.y_axis = QGraphicsTextItem('y-axis')

        self.headline.setFont(QFont('Arial', 20))
        self.x_axis.setFont(QFont('Arial', 15))
        self.y_axis.setFont(QFont('Arial', 15))

        self.headline.moveBy(900, 130)
        self.scene.addItem(self.headline)

        self.x_axis.moveBy(1000, 993)
        self.scene.addItem(self.x_axis)

        self.y_axis.setRotation(270)
        self.y_axis.moveBy(490, 600)
        self.scene.addItem(self.y_axis)

    def set_names(self, h, x, y):
        """Adds names in axis"""
        self.headline = QGraphicsTextItem(h)
        self.x_axis = QGraphicsTextItem(x)
        self.y_axis = QGraphicsTextItem(y)

        self.headline.setFont(QFont('Arial', 20))
        self.x_axis.setFont(QFont('Arial', 15))
        self.y_axis.setFont(QFont('Arial', 15))

        self.headline.moveBy(900, 130)
        self.scene.addItem(self.headline)

        self.x_axis.moveBy(1000, 993)
        self.scene.addItem(self.x_axis)

        self.y_axis.setRotation(270)
        self.y_axis.moveBy(490, 600)
        self.scene.addItem(self.y_axis)

    def remove_old_names(self):
        """removes old headline and axis names when new are added"""
        self.scene.removeItem(self.headline)
        self.scene.removeItem(self.x_axis)
        self.scene.removeItem(self.y_axis)

    def create_data_points(self):
        """Creates data points"""
        data_points = self.count_data.get_scaled_values()
        for i in range(self.count_data.get_size_of_data()):
            cur = data_points.get_at_position(i)
            point = QGraphicsEllipseItem(cur[0]-self.radius/2, cur[1]-self.radius/2, 2*self.radius, 2*self.radius)
            point.setBrush(QColor(0, 102, 51))
            self.scene.addItem(point)

    def create_connecting_lines(self):
        """Creates connecting lines between datapoints"""
        data_points = self.count_data.sort_by_x_increasing()
        for i in range(self.count_data.get_size_of_data() - 1):
            cur = data_points.get_at_position(i)
            next_point = data_points.get_at_position(i+1)
            line = QGraphicsLineItem(cur[0]+self.radius/2, cur[1]+self.radius/2, next_point[0]+self.radius/2, next_point[1]+self.radius/2)
            pen = QPen()
            pen.setWidthF(2)
            line.setPen(pen)
            self.scene.addItem(line)

    def create_grid(self):
        """create grid"""
        i = 0
        self.grid_list = []
        while i <= self.width_x:
            self.x_grid = QGraphicsLineItem(self.x_line_x_start, self.x_line_y-i,
                                            self.x_line_x_end, self.x_line_y-i)
            if i in [0, 100, 200, 300, 400, 500, 600, 700, 800]:
                pen = QPen()
                pen.setWidthF(1.5)
            else:
                pen = QPen()
                pen.setWidthF(0.5)
            self.x_grid.setPen(pen)
            self.grid_list.append(self.x_grid)
            i += self.size_of_grid
        l = 0
        while l <= self.width_y:
            self.y_grid = QGraphicsLineItem(self.y_line_x + l, self.y_line_y_start,
                                            self.y_line_x + l, self.y_line_y_end)
            if l in [0, 100, 200, 300, 400, 500, 600, 700, 800]:
                pen = QPen()
                pen.setWidthF(1.5)
            else:
                pen = QPen()
                pen.setWidthF(0.5)
            self.y_grid.setPen(pen)
            self.grid_list.append(self.y_grid)
            l += self.size_of_grid

    def add_grid(self):
        """Adds a grid"""
        for item in self.grid_list:
            self.scene.addItem(item)

    def remove_grid(self):
        """Removes grid"""
        for item in self.grid_list:
            self.scene.removeItem(item)

    def add_axis_nums(self):
        """Add numbers to axis"""
        width_x = 0
        for i in self.count_data.calc_x_axis_nums():
            rounded_i = self.count_data.round_num(i)
            len_x = self.count_data.num_length(str(rounded_i))
            point_x = QGraphicsTextItem(str(rounded_i))
            point_x.setFont(QFont("Arial", 12))
            if i == self.count_data.get_x_min():
                point_x.moveBy(597 - len_x**1.4, 979)
            elif i == self.count_data.get_x_max():
                point_x.moveBy(687 + 6 * 100 + 90 - len_x**1.4, 979)
            else:
                point_x.moveBy(687 + width_x - len_x**1.4, 979)
                width_x += 100
            self.scene.addItem(point_x)

        width_y = 0
        for j in self.count_data.calc_y_axis_nums():
            rounded_j = self.count_data.round_num(j)
            len_y = self.count_data.num_length(str(rounded_j))
            point_y = QGraphicsTextItem(str(rounded_j))
            point_y.setFont(QFont("Arial", 12))
            if j == self.count_data.get_y_min():
                point_y.moveBy(565 - len_y**1.9, 858 + 87.5)
            elif j == self.count_data.get_y_max():
                point_y.moveBy(565 - len_y**1.9, 858 - 6 * 97.5 - 103)
            else:
                point_y.moveBy(565 - len_y**1.9, 858-width_y)
                width_y += 100
            self.scene.addItem(point_y)

    def draw_mean(self, mean, median):
        """Draws a mean line"""
        scaled_mean = self.count_data.y_start - ((mean-self.count_data.y_min) /
                                                 (self.count_data.y_max-self.count_data.y_min)) * self.count_data.len_y
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
        scaled_median = self.count_data.y_start - ((median-self.count_data.y_min) /
                                                   (self.count_data.y_max-self.count_data.y_min)) * self.count_data.len_y
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

    def create_lin_reg_line(self):
        """creates linear model"""
        lin_reg_points = self.count_data.lin_reg_points
        if len(lin_reg_points) == 2:
            self.lin_reg_line = QGraphicsLineItem(lin_reg_points[0][0], lin_reg_points[0][1],
                                                   lin_reg_points[1][0], lin_reg_points[1][1])
            pen = QPen(QColor('red'))
            pen.setWidthF(3)
            self.lin_reg_line.setPen(pen)
        else:
            self.lin_reg_line = QGraphicsTextItem('Error in creating linear regression')
            self.lin_reg_line.setFont(QFont('Arial', 20))
            self.lin_reg_line.moveBy(self.x_line_x_start + 15, self.y_line_y_end + 15)

    def add_linear_model(self):
        """adds linear model"""
        self.scene.addItem(self.lin_reg_line)

    def remove_linear_model(self):
        """removes linear model"""
        self.scene.removeItem(self.lin_reg_line)

    def boundingRect(self):
        """implemented bounding rect"""
        return QRectF(500, 500, 100, 530)

