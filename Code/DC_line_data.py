
from DS_linked_list import LinkedList
class LineData:
    """Does some calculations for line diagram"""
    def __init__(self, data):

        self.data = data            # the data to be plotted

        # initialize some variables and values
        self.x_start = 610
        self.x_end = 1390
        self.y_start = 960
        self.y_end = 180
        self.len_x = 1390-610
        self.len_y = 960-180
        self.x_min = 0
        self.y_min = 0
        self.x_max = 0
        self.y_max = 0
        self.data_size = 0
        self.x_axis_nums = []
        self.y_axis_nums = []
        self.min_point = None
        self.max_point = None

        # does some calculations for data and stores it in linked list
        if isinstance(self.data, list):
            self.data_list = self.count_max_min_input()
        else:
            self.data_list = self.count_max_min()

        # some calculations for data
        self.get_scaled_values()
        self.mean = self.calc_mean()
        self.mean_x = self.calc_mean_x()
        self.sd_xy = self.calc_sd_xy()
        self.sd_x = self.calc_sd_x()
        self.sd_y = self.calc_sd_y()
        self.correlation = self.calc_correlation()
        self.lin_reg_line_slope = self.calc_lin_reg_line_slope()
        self.lin_reg_line_intercept = self.calc_lin_reg_line_intercept()
        self.lin_reg_points = self.calc_lin_reg_points()

    def count_max_min_input(self):
        """If input isn't a file"""
        x_min = False
        y_min = False
        x_max = False
        y_max = False
        list_of_data = LinkedList()
        for item in self.data:
            sub = []
            x_value = float(item[0])
            y_value = float(item[1])
            sub.append(x_value)
            sub.append(y_value)
            if x_min is False and y_min is False and x_max is False and y_max is False:
                x_min = x_value
                y_min = y_value
                x_max = x_value
                y_max = y_value
            else:
                if x_value < x_min:
                    x_min = x_value
                elif x_value > x_max:
                    x_max = x_value

                if y_value < y_min:
                    y_min = y_value
                elif y_value > y_max:
                    y_max = y_value
            self.data_size += 1
            list_of_data.add_last(sub)
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        return list_of_data

    def count_max_min(self):
        """if input is a file"""
        file = open(self.data)
        x_min = False
        y_min = False
        x_max = False
        y_max = False
        list_of_data = LinkedList()
        for line in file:
            sub = []
            parts = line.split(',')
            x_value = float(parts[0].strip())
            y_value = float(parts[1].strip())
            sub.append(x_value)
            sub.append(y_value)
            if x_min is False and y_min is False and x_max is False and y_max is False:
                x_min = x_value
                y_min = y_value
                x_max = x_value
                y_max = y_value
            else:
                if x_value < x_min:
                    x_min = x_value
                elif x_value > x_max:
                    x_max = x_value

                if y_value < y_min:
                    y_min = y_value
                elif y_value > y_max:
                    y_max = y_value
            self.data_size += 1
            list_of_data.add_last(sub)
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        file.close()
        return list_of_data

    def get_data(self):
        """returns data as a linked list"""
        if isinstance(self.data, list):
            return self.count_max_min_input()
        else:
            return self.count_max_min()

    def get_x_min(self):
        """returns min x-value"""
        return self.x_min

    def get_y_min(self):
        """returns min y-value"""
        return self.y_min

    def get_x_max(self):
        """returns max x-value"""
        return self.x_max

    def get_y_max(self):
        """returns max y-value"""
        return self.y_max

    def get_min_point(self):
        """returns min point"""
        return self.min_point

    def get_max_point(self):
        """returns max point"""
        return self.max_point

    def get_size_of_data(self):
        return self.data_size

    def get_as_list(self):
        """gets data as two-dimensional list"""
        data_list = []
        data = self.get_data()
        for i in range(int(self.get_size_of_data()/2)):
            sub = []
            cur = data.get_at_position(i)
            sub.append(cur[0])
            sub.append(cur[1])
            data_list.append(sub)
        return data_list

    def get_scaled_values(self):
        """returns linked list which contains scaled values of the data, so it can be plotted in QGraphicsView"""
        scaled_list = LinkedList()
        for i in range(self.get_size_of_data()):
            sub = []
            cur = self.data_list.get_at_position(i)
            sub.append(self.x_start + ((cur[0]-self.x_min)/(self.x_max-self.x_min)) * self.len_x)
            sub.append(self.y_start - ((cur[1]-self.y_min)/(self.y_max-self.y_min)) * self.len_y)
            scaled_list.add_last(sub)
        return scaled_list

    def sort_by_x_increasing(self):
        """Sorts the linked list by x containing scaled values, so the lines can be drawn"""
        sorted_list = LinkedList()
        scaled_list = self.get_scaled_values()
        for j in range(self.get_size_of_data()):
            min_point = scaled_list.get_at_position(0)
            min_ind = 0
            for i in range(1, self.get_size_of_data()-j):
                if scaled_list.get_at_position(i)[0] < min_point[0]:
                    min_point = scaled_list.get_at_position(i)
                    min_ind = i
            sorted_list.add_last(min_point)
            scaled_list.remove_position(min_ind)
        return sorted_list

    def sort_by_y_increasing(self):
        """Sorts the linked list by y, not scaled"""
        sorted_list = LinkedList()
        data = self.data_list
        for j in range(self.get_size_of_data()):
            min_point = data.get_at_position(0)
            min_ind = 0
            for i in range(1, self.get_size_of_data()-j):
                if data.get_at_position(i)[1] < min_point[1]:
                    min_point = data.get_at_position(i)
                    min_ind = i
            sorted_list.add_last(min_point)
            data.remove_position(min_ind)
        return sorted_list

    def calc_x_axis_nums(self):
        """Calculates x-axis nums"""
        first_x = self.x_min
        self.x_axis_nums.append(first_x)
        for i in range(7):
            axis_num = self.x_min + ((90 + i * 100)/self.len_x)*(self.x_max - self.x_min)
            self.x_axis_nums.append(axis_num)
        last_x = self.x_max
        self.x_axis_nums.append(last_x)
        return self.x_axis_nums

    def calc_y_axis_nums(self):
        """Calculates y-axis nums"""
        first_y = self.y_min
        self.y_axis_nums.append(first_y)
        for i in range(7):
            axis_num = self.y_min + ((90 + i * 100)/self.len_y)*(self.y_max - self.y_min)
            self.y_axis_nums.append(axis_num)
        last_y = self.y_max
        self.y_axis_nums.append(last_y)
        return self.y_axis_nums

    def calc_mean(self):
        """Calculates mean"""
        y_sum = 0
        for i in range(self.get_size_of_data()):
            y_sum += self.data_list.get_at_position(i)[1]
        mean = self.round_num(y_sum/self.get_size_of_data())
        return mean

    def calc_mean_x(self):
        """Calculates mean of x values"""
        y_sum = 0
        for i in range(self.get_size_of_data()):
            y_sum += self.data_list.get_at_position(i)[0]
        mean = self.round_num(y_sum/self.get_size_of_data())
        return mean

    def calc_sd_xy(self):
        """calculates standard deviation of x and y"""
        sd_xy = 0
        for i in range(self.get_size_of_data()):
            sd_xy += ((self.data_list.get_at_position(i)[0] - self.mean_x)
                      * (self.data_list.get_at_position(i)[1] - self.mean))
        sd_xy_norm = sd_xy/self.get_size_of_data()
        return sd_xy_norm

    def calc_sd_x(self):
        """calculates standard deviation for x"""
        sd_x = 0
        for i in range(self.get_size_of_data()):
            sd_x += (self.data_list.get_at_position(i)[0] - self.mean_x)**2
        sd_x_norm = (sd_x/self.get_size_of_data())**0.5
        return sd_x_norm

    def calc_sd_y(self):
        """calculates standard deviation for x"""
        sd_y = 0
        for i in range(self.get_size_of_data()):
            sd_y += (self.data_list.get_at_position(i)[1] - self.mean)**2
        sd_y_norm = (sd_y/self.get_size_of_data())**0.5
        return sd_y_norm

    def calc_correlation(self):
        """calculates correlation"""
        if self.sd_x == 0 or self.sd_y == 0:
            correlation = 0
        else:
            correlation = self.round_num(self.sd_xy/(self.sd_x*self.sd_y))
        return correlation

    def calc_lin_reg_line_slope(self):
        """calculates linear regression slope as scaled"""
        if self.sd_x != 0:
            slope = self.sd_xy/self.sd_x**2
        else:
            slope = 0
        return slope

    def calc_lin_reg_line_intercept(self):
        """calculates linear regression intercept as scaled"""
        intercept = self.mean - self.lin_reg_line_slope * self.mean_x
        return intercept

    def calc_lin_reg_points(self):
        """calculates starting and ending point of linear model"""
        points = []
        y1 = self.lin_reg_line_slope * self.x_min + self.lin_reg_line_intercept
        if self.y_min <= y1 <= self.y_max:            # on left side
            sub = []
            sub.append(round(self.x_start, 2))
            sub.append(round(self.y_start - ((y1-self.y_min)/(self.y_max-self.y_min)) * self.len_y, 2))
            if sub not in points:
                points.append(sub)

        y2 = self.lin_reg_line_slope * self.x_max + self.lin_reg_line_intercept
        if self.y_min <= y2 <= self.y_max:               # on right side
            sub = []
            sub.append(round(self.x_end, 2))
            sub.append(round(self.y_start - ((y2-self.y_min)/(self.y_max-self.y_min)) * self.len_y, 2))
            if sub not in points:
                points.append(sub)

        if self.lin_reg_line_slope != 0:
            x1 = (self.y_min - self.lin_reg_line_intercept)/self.lin_reg_line_slope
            if self.x_min <= x1 <= self.x_max:              # on downside
                sub = []
                sub.append(round(self.x_start + ((x1-self.x_min)/(self.x_max-self.x_min)) * self.len_x, 2))
                sub.append(round(self.y_start, 2))
                if sub not in points:
                    points.append(sub)

            x2 = (self.y_max - self.lin_reg_line_intercept)/self.lin_reg_line_slope
            if self.x_min <= x2 <= self.x_max:                 # on upside
                sub = []
                sub.append(round(self.x_start + ((x2-self.x_min)/(self.x_max-self.x_min)) * self.len_x, 2))
                sub.append(round(self.y_end, 2))
                if sub not in points:
                    points.append(sub)

        return points

    def calc_median(self):
        """Calculates median"""
        sorted_by_y = self.sort_by_y_increasing()
        len_data = self.get_size_of_data()
        if len_data % 2 == 0:
            median = (sorted_by_y.get_at_position(int(len_data / 2) - 1)[1] + sorted_by_y.get_at_position(int(len_data /2))[1])/2
        else:
            median = sorted_by_y.get_at_position(int(len_data / 2))[1]
        median = self.round_num(median)
        return median

    def round_num(self, num):
        """rounds number in three or four significant numbers, depending on number"""
        new_num = 0
        # numbers over 1000 is rounded in 4 significant
        if 100 <= abs(num) < 10000000:
            a = 0
            for i in range(5):
                if 100*10**i <= abs(num) < 100*10**(i+1):
                    new_num = int(round(num, a+1))
                a -= 1
        # numbers under 1000 is rounded in 3 significant
        elif 0.00001 <= abs(num) < 100:
            b = 7
            for j in range(7):
                if 0.00001*10**j <= abs(num) < 0.00001*10**(j+1):
                    new_num = float(round(num, b))
                b -= 1
        else:
            # if number is under abs(0.00001), 7 decimals is shown
            new_num = round(num, 7)
        return new_num

    def num_length(self, num):
        """Returns length of num"""
        return len(num)
