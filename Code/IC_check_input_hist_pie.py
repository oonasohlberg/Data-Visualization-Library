class CheckInputHistPie:
    def __init__(self, data):
        """Gets a list of written items"""
        self.data = data                                # input data
        self.data_dict = {}                             # initialize dict for data
        self.is_data_correct = self.CheckInput()        # checks if data is correct

    def CheckInput(self):
        """Checks if the input is in a right form"""
        x_name_list = []
        try:
            line_count = 0
            y_sum_hist_pie = True
            for item in self.data:

                # checks if there is a comma that separates two variables
                parts = item.split(',')

                parts[0] = parts[0].strip()
                parts[1] = parts[1].strip()

                # checks if there are exactly two datapoints on each line
                if len(parts) != 2:
                    return False

                # checks if x-value is not empty
                if parts[0] == "":
                    return False

                # checks if hist and pie data dont include same x-values in one graph
                if parts[0] in x_name_list:
                    return False
                else:
                    x_name_list.append(parts[0])

                # checks if y-value is a digit
                try:
                    int(parts[1])
                except ValueError:
                    try:
                        float(parts[1])
                    except ValueError:
                        return False

                # turns boolean to False, if y_value is not zero (avoiding division by zero)
                if y_sum_hist_pie:
                    if float(parts[1]) != 0:
                        y_sum_hist_pie = False

                # checks if y-value is between 0 and 10000
                if float(parts[1]) > 10000 or float(parts[1]) < 0:
                    return False

                # adds data point in dictionary
                self.data_dict[parts[0]] = parts[1]

                line_count += 1

            # returns False if there are no data points
            if line_count == 0:
                return False

            # returns False if the sum of y-values is 0 (division by zero)
            if y_sum_hist_pie:
                return False

            # returns True if there are no mistakes
            return True

        # returns False if there are problems with input
        except Exception:
            return False

    def get_is_correct(self):
        """returns True if data is valid"""
        return self.is_data_correct

    def get_data_list(self):
        """returns dictionary containing the data"""
        return self.data_dict
