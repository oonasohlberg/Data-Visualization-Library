import unittest
import sys
from PyQt6 import QtWidgets
from CW_file import File
from CW_menu import Menu
from IC_check_file import GoThroughFile
from IC_check_input_hist_pie import CheckInputHistPie
from IC_check_input_line import CheckInputLine
from CW_graph import Graph
from GI_graph_item_hist import GraphItemHist
from GI_graph_item_line import GraphItemLine
from GI_graph_item_pie import GraphItemPie
from DC_hist_pie_data import HistPieData
from ID_hist_pie_input import HistPieInput
from OW_info_window_hist_pie import InfoWindowHistPie
from OW_info_window_line import InfoWindowLine
from ID_line_input import LineInput
from DC_line_data import LineData
from DS_linked_list import LinkedList, ListNode
from OW_name_axis import NameAxisWindow
from OW_show_data import ShowData



app = QtWidgets.QApplication(sys.argv)

class Test(unittest.TestCase):
    """Some unittests for functions and variables in my program"""

    # set up
    def setUp(self):
        # file
        self.file_window_line = File(False, 1)
        self.file_window_hist = File(False, 2)
        self.file_window_pie = File(False, 3)

        # menu
        self.menu_test = Menu()

        # check_file
        self.check_file = GoThroughFile('example_pie.txt', True)

        # check_input_hist_pie
        self.check_input_hist_pie = CheckInputHistPie(['1,2', '3,5'])
        self.check_input_hist_pie_error = CheckInputHistPie(['1,2', '1,5'])

        # check_input_line
        self.check_input_line = CheckInputLine(['1,2', '3,5'])
        self.check_input_line_error = CheckInputLine(['1,2', '3,2'])

        # graph
        self.check_graph_line = Graph(1, 'example files\example_line_diagram.txt')
        self.check_graph_hist = Graph(2, 'example files\example_histogram.txt')
        self.check_graph_pie = Graph(3, 'example files\example_pie.txt')

        # graph_item_hist
        self.check_graph_item_hist = GraphItemHist('example files\example_histogram.txt', self.check_graph_hist.scene)

        # graph_item_line
        self.check_graph_item_line = GraphItemLine('example files\example_line_diagram.txt', self.check_graph_line.scene)

        # graph item pie
        self.check_graph_item_pie = GraphItemPie('example files\example_pie.txt', self.check_graph_pie.scene)

        # histdata
        self.check_hist_data = HistPieData('example files\example_histogram.txt')
        self.check_pie_data = HistPieData('example files\example_pie.txt')
        self.check_hist_data_input = HistPieData({'suomi': '4', 'ruotsi': '3', 'norja': '6'})
        self.check_pie_data_input = HistPieData({'suomi': '4', 'ruotsi': '3', 'norja': '6'})

        # linedata
        self.check_line_data = LineData('example files\example_line_diagram.txt')
        self.check_line_data_input = LineData([['1', '2'], ['3', '4'], ['5', '6']])

        # histpie_input
        self.check_hist_pie_input = HistPieInput()

        # info_window_hist_pie
        self.check_info_window_hist_pie = InfoWindowHistPie(2, 4, 'suomi', 'ruotsi', 6, 3, 5, 4.5, 16)

        # info_window_line
        self.check_info_window_line = InfoWindowLine(10, 5, 5, 7, 8)

        # line_input
        self.check_line_input = LineInput()

        # linkedlist
        self.check_linked_list = LinkedList()
        self.check_list_node = ListNode(3)

        # nameaxis
        self.check_name_axis_line = NameAxisWindow(1)
        self.check_name_axis_hist = NameAxisWindow(2)
        self.check_name_axis_pie = NameAxisWindow(3)

        # show_data
        self.check_show_data_line = ShowData([['1', '2'], ['3', '4'], ['5', '6']])
        self.check_show_data_hist_pie = ShowData({'suomi': '4', 'ruotsi': '3', 'norja': '6'})

    #file

    # checks if there is no warning message by default
    def test_warning_msg_bool(self):
        self.assertEqual(self.file_window_line.warning_message_exists, False,
                         "There shouldn't be warning message by default")
        self.assertEqual(self.file_window_hist.warning_message_exists, False,
                         "There shouldn't be warning message by default")
        self.assertEqual(self.file_window_pie.warning_message_exists, False,
                         "There shouldn't be warning message by default")
    # Checks if boolean is_line is false by default
    def test_is_line(self):
        self.assertEqual(self.file_window_line.is_line, False,
                         "Is line should be False by default")
        self.assertEqual(self.file_window_hist.is_line, False,
                         "Is line should be False by default")
        self.assertEqual(self.file_window_pie.is_line, False,
                         "Is line should be False by default")
    # tests if the types are right
    def test_type(self):
        self.assertEqual(self.file_window_line.type, 1,
                         "Type of line diagram should be 1")
        self.assertEqual(self.file_window_hist.type, 2,
                         "Type of histogram should be 2")
        self.assertEqual(self.file_window_pie.type, 3,
                         "Type of pie diagram should be 3")
    # tests if button is right type
    def test_button_input_data(self):
        self.assertIsInstance(self.file_window_line.input_data, QtWidgets.QPushButton,
                              "Write data button should be QPushButton")
    # tests if layout is right type
    def test_layout(self):
        self.assertIsInstance(self.file_window_line.layout, QtWidgets.QVBoxLayout,
                              "The layout should be type QVBoxLayout")

    # menu

    # Test if the headline is QLabel
    def test_menu_headline(self):
        self.assertIsInstance(self.menu_test.layout_up.label, QtWidgets.QLabel,
                              "Headline should be type QLabel")

    # checkfile

    # Check file returns False, when incorrect input
    def test_check_file1(self):
        self.assertFalse(self.check_file.CheckFile(),
                         "Wrong kind of input should return False")

    # check_input_hist_pie

    # check if function returns data as a dict
    def test_input_hist_pie_as_dict(self):
        self.assertIsInstance(self.check_input_hist_pie.get_data_list(), dict,
                              "Data structure should be dictionary")
    # returns true when correct input
    def test_correct_input_hist_pie(self):
        self.assertTrue(self.check_input_hist_pie.CheckInput(),
                        "Right kind of input should return True")
    # wrong input
    def test_wrong_input_hist_pie(self):
        self.assertFalse(self.check_input_hist_pie_error.CheckInput(),
                         "Wrong kind of input should return False")

    # check_input_hist_pie
    def test_input_line_as_list(self):
        self.assertIsInstance(self.check_input_line.get_data_list(), list,
                              "Data structure should be list")
    # correct input
    def test_correct_line_input(self):
        self.assertTrue(self.check_input_line.CheckInput(),
                        "Right kind of input should return True")
    # wrong input
    def test_wrong_input_line(self):
        self.assertFalse(self.check_input_line_error.CheckInput(),
                         "Wrong kind of input should return False")

    # graph
    # type
    def test_graph_line(self):
        self.assertEqual(self.check_graph_line.type, 1,
                         "Graph type for line should be 1")
        self.assertEqual(self.check_graph_pie.type, 3,
                         "Graph type for pie should be 3")
    # test if graph_item is right object
    def test_graph_line_graph_item(self):
        self.assertIsInstance(self.check_graph_line.graph_item, GraphItemLine,
                              "graph_item for line diagram in class Graph should be GraphItemLine")
        self.assertIsInstance(self.check_graph_pie.graph_item, GraphItemPie,
                              "graph_item for pie in class Graph should be GraphItemPie")
    # test max y-value
    def test_max_y(self):
        self.assertEqual(self.check_graph_line.max_y, 135.8,
                         "maximum y-value for this data should be 135.8")
    # test min y-value
    def test_min_y(self):
        self.assertEqual(self.check_graph_line.min_y, 50.2,
                         "minimum y-value for this data should be 50.2")
    # test amount of data
    def test_amount_data(self):
        self.assertEqual(self.check_graph_line.data_amount, 40,
                         "amount of data for this data should be 40")
        self.assertEqual(self.check_graph_pie.data_amount, 13,
                         "amount of data for this data should be 13")
    # test mean
    def test_mean(self):
        self.assertEqual(self.check_graph_line.mean, 89,
                         "mean for this data should be 89")
    # test median
    def test_median(self):
        self.assertEqual(self.check_graph_line.median, 87.8,
                         "median for this data should be 87.8")
    # data as list
    def test_data_as_list(self):
        self.assertIsInstance(self.check_graph_line.data_as_list, list,
                              "method data_as_list should return data structure list")
    # test max values
    def test_max_values(self):
        self.assertEqual(self.check_graph_hist.max_values, ['Lasse'],
                         "maximum values for this data should be Lasse")
    # test min values is a list
    def test_min_values(self):
        self.assertIsInstance(self.check_graph_hist.min_values, list,
                              "minimum values should be in data structure list")

    # graph_item_hist, graph_item_line, graph_item_pie
    # test count data
    def test_count_data(self):
        self.assertIsInstance(self.check_graph_item_hist.count_data, HistPieData,
                              "item count_data should be class HistPieData")
        self.assertIsInstance(self.check_graph_item_line.count_data, LineData,
                              "item count_data should be class LineData")

    # test headline type
    def test_default_headline(self):
        self.assertIsInstance(self.check_graph_item_hist.headline, QtWidgets.QGraphicsTextItem,
                              "graph items headline should be QGraphicsTextItem")
    # test some values
    def test_size_of_grid(self):
        self.assertEqual(self.check_graph_item_hist.size_of_grid, 20,
                         "Size of grid for hist should be 20")
        self.assertEqual(self.check_graph_item_line.size_of_grid, 20,
                         "Size of grid for line should be 20")
    def test_x_line_x_start(self):
        self.assertEqual(self.check_graph_item_hist.x_line_x_start, 600,
                         "x-line should start for hist in x: 600")
    def test_x_line_x_end(self):
        self.assertEqual(self.check_graph_item_hist.x_line_x_end, 1400,
                         "x-line should end for hist in x: 1400")
    def test_x_line_y(self):
        self.assertEqual(self.check_graph_item_hist.x_line_y, 970,
                         "x-line should start for hist in y: 970")
    #test grid list
    def test_grid_list(self):
        self.assertIsInstance(self.check_graph_item_hist.grid_list, list,
                              "grid_list should be data structure list")
    #test rect list
    def test_rect_list(self):
        self.assertIsInstance(self.check_graph_item_hist.rect_list, list,
                              "list of rectangles should be data structure list")
    # test color list is a list
    def test_color_list(self):
        self.assertIsInstance(self.check_graph_item_pie.color_list, list,
                              "list of pie colors should be data structure list")
    def test_pie_rect(self):
        self.assertEqual(self.check_graph_item_pie.rect_width, 20,
                         "rectangle width should be 20")
        self.assertEqual(self.check_graph_item_pie.rect_height, 20,
                         "rectangle height should be 20")
        self.assertEqual(self.check_graph_item_pie.rect_start_x, 450,
                         "rectangle start x-coordinate: 450")
        self.assertEqual(self.check_graph_item_pie.rect_start_y, 50,
                         "rectangle start y-coordinate: 50")
        self.assertEqual(self.check_graph_item_pie.rect_dist, 40,
                         "rectangle distance should be 40")

    def test_sorted(self):
        self.assertIsInstance(self.check_graph_item_pie.sorted_data_inc, dict,
                              "sorted pie data should be dictionary")


    # histdata, linedata
    # linedata values
    def test_line_data_values(self):
        self.assertEqual(self.check_line_data.x_start, 610,
                         "starting x-coordinate for axis: 610")
        self.assertEqual(self.check_line_data.x_end, 1390,
                         "ending x-coordinate for axis: 1390")
        self.assertEqual(self.check_line_data.y_start, 960,
                         "starting y-coordinate for axis: 960")
        self.assertEqual(self.check_line_data.y_end, 180,
                         "ending y-coordinate for axis: 180")
        self.assertEqual(self.check_line_data.len_x, 1390-610,
                         "length of x-axis should be 780")
        self.assertEqual(self.check_line_data.len_y, 960-180,
                         "length of x-axis should be 780")

    def test_hist_pie_data_values(self):
        self.assertEqual(self.check_hist_data.x_line_x_start, 600,
                         "starting x-coordinate for x-line should be 600")
        self.assertEqual(self.check_hist_data.x_line_x_end, 1400,
                         "ending x-coordinate for x-line should be 1400")
        self.assertEqual(self.check_hist_data.x_line_y, 970,
                         "coordinate for y in x-line should be 970")
        self.assertEqual(self.check_pie_data.y_line_y_start, 970,
                         "starting y-coordinate for y-line should be 970")
        self.assertEqual(self.check_pie_data.y_line_y_end, 180,
                         "ending y-coordinate for y-line should be 180")
        self.assertEqual(self.check_pie_data.y_line_x, 600,
                         "coordinate for x in y-line should be 600")

    #  tests method that goes through file
    def test_go_through_file(self):
        self.assertIsInstance(self.check_line_data.count_max_min(), LinkedList,
                              "line data as file should be stored as data structure LinkedList")
        self.assertIsInstance(self.check_hist_data.go_through_file(self.check_hist_data.data), dict,
                              "hist data as file should be stored as data structure dictionary")

    #  tests method that goes through input
    def test_go_through_input(self):
        self.assertIsInstance(self.check_line_data_input.count_max_min_input(), LinkedList,
                              "line data as input should be stored as data structure LinkedList")
        self.assertEqual(self.check_hist_data_input.go_through_input(self.check_hist_data_input.data), {'suomi': 4.0, 'ruotsi': 3.0, 'norja': 6.0},
                         "hist data as input should be stored as data structure dictionary")
        self.assertIsInstance(self.check_pie_data_input.go_through_input(self.check_pie_data_input.data), dict,
                              "pie data as file should be stored as data structure dictionary")

    # test mean and median for histogram
    def test_mean_hist(self):
        self.assertEqual(self.check_hist_data_input.calc_mean(), 4.33,
                         "mean for this histogram data should be 4.33")
        self.assertEqual(self.check_hist_data_input.calc_median(), 4.0,
                         "median for this histogram data should be 4.0")
        self.assertEqual(self.check_hist_data.calc_mean(), 173,
                         "mean for this histogram data should be 173")
        self.assertEqual(self.check_hist_data.calc_median(), 174,
                         "median for this histogram data should be 174")

    # test linedata get as list
    def test_get_as_list(self):
        self.assertIsInstance(self.check_line_data_input.get_as_list(), list,
                              "line data as list should be data structure list")

    # test round num method
    def test_round_num(self):
        self.assertEqual(self.check_line_data_input.round_num(3.72456), 3.72,
                         "rounding 3.72456 should equal 3.72 (3 significant number)")
        self.assertEqual(self.check_line_data_input.round_num(2618.76), 2619,
                         "rounding 2618.76 should equal 2619 (4 significant number)")
        self.assertEqual(self.check_line_data_input.round_num(0.00034568), 0.000346,
                         "rounding 0.00034568 should equal 0.000346 (3 significant number)")

    # test len num method
    def test_len_num(self):
        self.assertEqual(self.check_line_data.num_length('362.946'), 7,
                         "length of number 362.946 should be 7")

    # check standard deviations
    def test_calc_sd_xy(self):
        self.assertEqual(self.check_line_data.calc_sd_xy(), 268.73249999999996,
                         "standard deviation for x should not be rounded and equals in this case 268.73249999999996")
        self.assertEqual(self.check_line_data.calc_sd_x(), 11.554220008291344,
                         "standard deviation for x and y should not be rounded and equals in this case 11.554220008291344")

    # test slope
    def test_slope(self):
        self.assertEqual(self.check_line_data_input.calc_lin_reg_line_slope(), 1,
                         "slope should be 1 for this data")

    # test intercept
    def test_intercept(self):
        self.assertEqual(self.check_line_data_input.calc_lin_reg_line_intercept(), 1,
                         "intercept should be 1 for this data")

    # test linear model points
    def test_lin_reg_points(self):
        self.assertEqual(self.check_line_data.calc_lin_reg_points(), [[1390.00, 257.94], [624.50, 960.00]],
                         "starting and ending points for linear model for this data should be [1390, 257.9401055339689], [624.5014093940972, 960]")

    # histpie_input
    # test if data is a list
    def test_hist_pie_input_data(self):
        self.assertIsInstance(self.check_hist_pie_input.get_data_list(), list,
                              "data should be retured as data structure list")
    # test button
    def test_hist_pie_input_button(self):
        self.assertEqual(self.check_hist_pie_input.ok_button.text(), 'OK',
                         "hist/pie input windows ok button should contain text OK")

    # info_window_hist_pie
    # check values
    def test_info_window_hist_pie(self):
        self.assertEqual(self.check_info_window_hist_pie.type, 2,
                         "Info windows type for this data should be 2")
        self.assertEqual(self.check_info_window_hist_pie.data_len, 4,
                         "Info windows data length for this data should be 4")
        self.assertEqual(self.check_info_window_hist_pie.max_values, 'suomi',
                         "Info windows maximum value for this data should be: suomi")
        self.assertEqual(self.check_info_window_hist_pie.min_values, 'ruotsi',
                         "Info windows minimum value for this data should be: ruotsi")
        self.assertEqual(self.check_info_window_hist_pie.max_y, 6,
                         "Info windows maximum y-value for this data should be: 6")
        self.assertEqual(self.check_info_window_hist_pie.min_y, 3,
                         "Info windows minimum y-value for this data should be: 3")
        self.assertEqual(self.check_info_window_hist_pie.mean, 5,
                         "Info windows mean for this data should be: 5")
        self.assertEqual(self.check_info_window_hist_pie.median, 4.5,
                         "Info windows median for this data should be: 4.5")
        self.assertEqual(self.check_info_window_hist_pie.data_sum, 16,
                         "Info windows data sum for this data should be 16")

    # info_window_line
    # check values
    def test_info_window_line(self):
        self.assertEqual(self.check_info_window_line.max_y, 10,
                         "Info windows maximum y-value for this data should be: 10")
        self.assertEqual(self.check_info_window_line.min_y, 5,
                         "Info windows minimum y-value for this data should be: 5")
        self.assertEqual(self.check_info_window_line.len_data, 5,
                         "Info windows data length for this data should be 5")
        self.assertEqual(self.check_info_window_line.mean, 7,
                         "Info windows mean for this data should be: 7")
        self.assertEqual(self.check_info_window_line.median, 8,
                         "Info windows median for this data should be: 8")

    # line_input
    # check values
    def test_line_input(self):
        self.assertIsInstance(self.check_line_input.main_layout, QtWidgets.QHBoxLayout,
                              "line inputs main layout should be QHBoxLayout")
        self.assertEqual(self.check_line_input.ok_button.text(), 'OK',
                         "line input windows ok button should contain text OK")
        self.assertIsInstance(self.check_line_input.data, list,
                              "line input should be stored in data structure list")

    # linkedlist and listnode
    def test_list_node(self):
        self.assertEqual(self.check_list_node.value, 3,
                         "value of this node should be 3")
        self.assertEqual(self.check_list_node.next, None,
                         "next node should be None")
        self.assertEqual(self.check_list_node.prev, None,
                         "previous node should be None")

    def test_linked_list(self):
        self.assertEqual(self.check_linked_list.get_size(), 0,
                         "Size of this linked list should be zero")
        self.assertEqual(self.check_linked_list.get_at_position(0), None,
                         "Node at position 0 in this linked list should be None")

    # nameaxis
    # name axis line
    def test_name_axis_line(self):
        self.assertIsInstance(self.check_name_axis_line.headline, QtWidgets.QLineEdit,
                              "Naming space for headline should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_line.x_edit, QtWidgets.QLineEdit,
                              "Naming space for x-axis should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_line.y_edit, QtWidgets.QLineEdit,
                              "Naming space for y-axis should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_line.x_label, QtWidgets.QLabel,
                              "Text for naming x-axis should be QLabel")
        self.assertIsInstance(self.check_name_axis_line.y_label, QtWidgets.QLabel,
                              "Text for naming y-axis should be QLabel")
    # name axis histogram
    def test_name_axis_hist(self):
        self.assertIsInstance(self.check_name_axis_hist.headline, QtWidgets.QLineEdit,
                              "Naming space for headline should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_hist.y_edit, QtWidgets.QLineEdit,
                              "Naming space for y-axis should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_hist.y_label, QtWidgets.QLabel,
                              "Text for naming y-axis should be QLabel")

    def test_name_axis_pie(self):
        self.assertIsInstance(self.check_name_axis_pie.headline, QtWidgets.QLineEdit,
                              "Naming space for headline should be QLineEdit")
        self.assertIsInstance(self.check_name_axis_pie.ok_button, QtWidgets.QPushButton,
                              "Naming headline windows ok button should be QPushButton")

    # show_data
    # show data line
    def test_show_data_line(self):
        self.assertIsInstance(self.check_show_data_line.data, list,
                              "Window show data variable data should be data structure list")
        self.assertIsInstance(self.check_show_data_line.main_layout, QtWidgets.QHBoxLayout,
                              "Show data line should have QHBoxLayout as main layout")

    # show data hist/pie
    def test_show_data_hist_pie(self):
        self.assertIsInstance(self.check_show_data_hist_pie.data, dict,
                              "Window show data variable data should be data structure list")
        self.assertIsInstance(self.check_show_data_hist_pie.main_layout, QtWidgets.QVBoxLayout,
                              "Show data hist/pie should have QVBoxLayout as main layout")


if __name__ == '__main__':

    unittest.main()