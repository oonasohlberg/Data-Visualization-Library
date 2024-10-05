
class GoThroughFile:
    """Checks if the input file is valid"""
    def __init__(self, path, bool):
        self.path = path                                # input file
        self.is_line = bool                             # True if graph is line diagram

    def get_path(self):
        """Returns the file"""
        return self.path

    def get_is_line(self):
        """Returns True is line graph is chosen"""
        return self.is_line

    def get_is_file_correct(self):
        """Returns true if file is valid"""
        return self.CheckFile()

    def CheckFile(self):
        """Checks if the lines in file are in a correct form"""
        max_y = float(-10000000)      # default
        min_y = float(10000000)
        max_x = float(-10000000)
        min_x = float(10000000)
        x_name_list = []
        try:
            file = open(self.path)
            line_count = 0
            y_sum_hist_pie = True
            for line in file:

                # checks if there is a comma that separates two variables
                parts = line.split(',')

                parts[0] = parts[0].strip()
                parts[1] = parts[1].strip()

                # checks if there are exactly two datapoints on each line
                if len(parts) != 2:
                    return False

                # checks if hist and pie data dont include same x-values in one graph
                if not self.get_is_line():
                    if parts[0] in x_name_list:
                        return False
                    else:
                        x_name_list.append(parts[0])

                # checks if max y, and x and min y and x in line diagram are not the same
                if self.get_is_line():
                    if float(parts[1]) > max_y:
                        max_y = float(parts[1])
                    if float(parts[1]) < min_y:
                        min_y = float(parts[1])

                    if float(parts[0]) > max_x:
                        max_x = float(parts[0])
                    if float(parts[0]) < min_x:
                        min_x = float(parts[0])

                # checks if line diagram's x-axis values are digits
                if self.get_is_line():
                    try:
                        int(parts[0])
                    except ValueError:
                        try:
                            float(parts[0])
                        except ValueError:
                            return False

                # checks if histogram and pie diagram x-values are not empty
                if not self.get_is_line():
                    if parts[0] == "":
                        return False

                # checks if y-values are digits

                try:
                    int(parts[1])
                except ValueError:
                    try:
                        float(parts[1])
                    except ValueError:
                        return False

                if not self.get_is_line():
                    if y_sum_hist_pie:
                        if float(parts[1]) != 0:
                            y_sum_hist_pie = False

                line_count += 1
                # checks line count
                if not self.get_is_line():
                    if line_count > 20:
                        return False
                if self.get_is_line():
                    if line_count > 50:
                        return False

                # checks if line diagrams values are between 10^-6 and 9999999
                if self.get_is_line():
                    if abs(float(parts[0])) > 9999999:
                        return False
                    if abs(float(parts[1])) > 9999999:
                        return False
                if not self.get_is_line():
                    if float(parts[1]) > 10000 or float(parts[1]) < 0:
                        return False

            # if all y values are zero (the graph is not significant)
            if not self.get_is_line():
                if y_sum_hist_pie:
                    return False

            # checks if it's not an empty file or 1 line in line diagram
            if self.get_is_line():
                if line_count < 2:
                    return False
                # max and min are the same -> zero division
                if max_y == min_y or max_x == min_x:
                    return False
            else:
                if line_count == 0:
                    return False

            # returns True if there were no errors
            return True

        # returns False if there occurs a problem in file
        except Exception:
            return False

