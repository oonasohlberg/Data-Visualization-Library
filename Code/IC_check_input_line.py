

class CheckInputLine:
    def __init__(self, data):
        """Gets a list of written items"""
        self.data = data                                # input data
        self.data_list = []                             # initialize list for data
        self.is_data_correct = self.CheckInput()        # check if input is correct

    def CheckInput(self):
        """Checks if input is in a right form"""
        max_y = float(-10000000)      # default values
        min_y = float(10000000)
        max_x = float(-10000000)
        min_x = float(10000000)
        try:
            line_count = 0
            for item in self.data:

                # creates sublist on each iteration, where one data point is stored
                sub = []

                # checks if there is a comma that separates two variables
                parts = item.split(',')

                parts[0] = parts[0].strip()
                parts[1] = parts[1].strip()

                # checks if there are exactly two datapoints on each line
                if len(parts) != 2:
                    return False

                if float(parts[1]) > max_y:
                    max_y = float(parts[1])
                if float(parts[1]) < min_y:
                    min_y = float(parts[1])
                if float(parts[0]) > max_x:
                    max_x = float(parts[0])
                if float(parts[0]) < min_x:
                    min_x = float(parts[0])

                # checks if x- and y- values are digits
                try:
                    int(parts[0])
                except ValueError:
                    try:
                        float(parts[0])
                    except ValueError:
                        return False
                try:
                    int(parts[1])
                except ValueError:
                    try:
                        float(parts[1])
                    except ValueError:
                        return False

                # checks if values are between -9999999 and 9999999
                if abs(float(parts[0])) > 9999999:
                    return False

                if abs(float(parts[1])) > 9999999:
                    return False

                # adds sub in list
                sub.append(parts[0])
                sub.append(parts[1])
                self.data_list.append(sub)

                line_count += 1

            # checks if there is at least one data point
            if line_count < 2:
                return False
            if max_y == min_y or max_x == min_x:
                return False

            # returns true if input has no mistakes
            return True

        # returns False if some error occurs
        except Exception:
            return False

    def get_is_correct(self):
        """Returns true if the data is valid"""
        return self.is_data_correct

    def get_data_list(self):
        """Returns the data in list"""
        return self.data_list
