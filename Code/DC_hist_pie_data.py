class HistPieData:
    """Does some calculations for histogram"""
    def __init__(self, data):
        self.data = data            # given data

        # initializes some variables
        self.x_line_x_start = 600
        self.x_line_x_end = 1400
        self.x_line_y = 970
        self.width_x = self.x_line_x_end - self.x_line_x_start

        self.y_line_y_start = 970
        self.y_line_y_end = 170 + 10
        self.y_line_x = 600
        self.width_y = self.y_line_y_start - self.y_line_y_end

        self.len_data = 0
        self.y_max = 0
        self.y_min = 0
        self.min_value_list = []
        self.max_value_list = []

        # does some calculations for data and returns it as a dict
        if isinstance(self.data, dict):
            self.data_list = self.go_through_input(self.data)
        else:
            self.data_list = self.go_through_file(self.data)

        # calculate numbers for y-axis for histogram
        self.y_axis_nums = self.calc_y_axis_nums()

    def go_through_input(self, data):
        """goes through the data and finds some significant values"""
        list_of_data = {}
        y_min = False
        y_max = False
        min_value_list = None
        max_value_list = None
        x_values = list(data.keys())
        y_values = list(data.values())
        for i in range(len(data)):
            x_value = x_values[i]
            y_value = float(y_values[i])
            list_of_data[x_value] = y_value

            if y_min is False and y_max is False:
                min_value_list = []
                max_value_list = []
                y_min = y_value
                y_max = y_value
                min_value_list.append(x_value)
                max_value_list.append(x_value)
            else:
                if y_value < y_min:
                    min_value_list = []
                    y_min = y_value
                    min_value_list.append(x_value)
                elif y_value == y_min:
                    min_value_list.append(x_value)

                if y_value > y_max:
                    max_value_list = []
                    y_max = y_value
                    max_value_list.append(x_value)
                elif y_value == y_max:
                    max_value_list.append(x_value)
        self.y_min = y_min
        self.y_max = y_max
        self.min_value_list = min_value_list
        self.max_value_list = max_value_list
        self.len_data = len(data)
        return list_of_data

    def go_through_file(self, data):
        """goes through the data and stores it as a dictionary and finds some significant values"""
        file = open(data)
        y_min = False
        y_max = False
        min_value_list = None
        max_value_list = None
        list_of_data = {}
        length = 0
        for line in file:
            parts = line.split(',')
            x_value = parts[0].strip()
            y_value = float(parts[1].strip())
            list_of_data[x_value] = y_value
            if y_min is False and y_max is False:
                min_value_list = []
                max_value_list = []
                y_min = y_value
                y_max = y_value
                min_value_list.append(x_value)
                max_value_list.append(x_value)
            else:
                if y_value < y_min:
                    min_value_list = []
                    y_min = y_value
                    min_value_list.append(x_value)
                elif y_value == y_min:
                    min_value_list.append(x_value)

                if y_value > y_max:
                    max_value_list = []
                    y_max = y_value
                    max_value_list.append(x_value)
                elif y_value == y_max:
                    max_value_list.append(x_value)
            length += 1
        self.y_min = y_min
        self.y_max = y_max
        self.min_value_list = min_value_list
        self.max_value_list = max_value_list
        self.len_data = length
        file.close()
        return list_of_data

    def get_data(self):
        """returns data as a dictionary"""
        if isinstance(self.data, dict):
            return self.go_through_input(self.data)
        else:
            return self.go_through_file(self.data)

    def get_len_data(self):
        """returns length of data"""
        return self.len_data

    def get_min(self):
        """returns min y-value"""
        return self.y_min

    def get_max(self):
        """returns max y-value"""
        return self.y_max

    def get_data_list(self):
        """returns data as a dictionary as class value"""
        return self.data_list

    def get_min_values(self):
        """returns min x-values as a list"""
        return self.min_value_list

    def get_max_values(self):
        """returns max x-values as a list"""
        return self.max_value_list

    def calc_y_axis_nums(self):
        """Calculates y-axis nums"""
        y_list = []
        for i in range(9):
            y_list.append(self.get_max()*(i/8))
        return y_list

    def get_y_axis_nums(self):
        """returns y-axis nums as a list"""
        return self.y_axis_nums

    def sort_increasing(self):
        """Sort increasing"""
        sort_dict = self.get_data()
        sorted_dict = {}
        for i in range(self.len_data):
            min_value = list(sort_dict.values())[0]
            min_item = list(sort_dict.keys())[0]
            count = 0
            for j in sort_dict.values():
                if j < min_value:
                    min_value = j
                    min_item = list(sort_dict.keys())[count]
                count += 1
            sorted_dict[min_item] = min_value
            del sort_dict[min_item]
        return sorted_dict

    def calc_mean(self):
        """calculate mean"""
        data = self.get_data()
        y_values = list(data.values())
        item_sum = 0
        for item in y_values:
            item_sum += item
        mean = item_sum/self.get_len_data()
        mean = self.round_num(mean)
        return mean

    def calc_median(self):
        """calculate median"""
        data = self.sort_increasing()
        y_list = list(data.values())
        if self.get_len_data() % 2 == 0:
            median = (y_list[int((self.get_len_data()/2)-1)] + y_list[int(self.get_len_data()/2)])/2
        else:
            median = y_list[int(self.get_len_data()/2)]
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

    def count_sum_data(self):
        """counts sum of datapoints"""
        data_sum = 0
        for i in self.data_list.values():
            data_sum += i
        return data_sum

    def get_rounded_sum(self):
        """returns rounded sum of data"""
        return self.round_num(self.count_sum_data())
