
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QPixmap


class Menu(QtWidgets.QWidget):
    def __init__(self):
        """Creates menu"""
        super().__init__()

        # create layouts
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.layout_up = QtWidgets.QVBoxLayout()
        self.layout_down = QtWidgets.QHBoxLayout()
        self.layout_photos = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.layout_up)
        self.layout.addLayout(self.layout_down)
        self.layout.addLayout(self.layout_photos)

        # Add headline
        self.layout_up.label = QLabel('\n\t\t\t   Welcome to Oona\'s data visualization library!\n\n'
                                      '\t\t\t        Choose the type of data visualization\n')

        self.layout_up.label.setFont(QFont('Arial', 25))
        self.layout_up.addWidget(self.layout_up.label)

        # create buttons
        self.buttonLineDiagram = QPushButton('Line diagram')
        self.buttonHistogram = QPushButton('Histogram')
        self.buttonPieDiagram = QPushButton('Pie diagram')

        self.buttonLineDiagram.setFont(QFont('Arial', 25))
        self.buttonHistogram.setFont(QFont('Arial', 25))
        self.buttonPieDiagram.setFont(QFont('Arial', 25))

        self.buttonLineDiagram.setStyleSheet('background-color: pink')
        self.buttonHistogram.setStyleSheet('background-color: orange')
        self.buttonPieDiagram.setStyleSheet('background-color: lightblue')

        self.buttonLineDiagram.setFixedSize(QtCore.QSize(500, 300))
        self.buttonHistogram.setFixedSize(QtCore.QSize(500, 300))
        self.buttonPieDiagram.setFixedSize(QtCore.QSize(500, 300))

        self.layout_down.addWidget(self.buttonLineDiagram)
        self.layout_down.addWidget(self.buttonHistogram)
        self.layout_down.addWidget(self.buttonPieDiagram)

        # add photos of diagrams

        self.photos_label_1 = QLabel(self)
        self.photos_label_2 = QLabel(self)
        self.photos_label_3 = QLabel(self)

        self.buttonLineDiagram_photo = QPixmap('small_photos/Y2linegraph.png')
        self.buttonHistogram_photo = QPixmap('small_photos/Y2histgraph.png')
        self.buttonPieDiagram_photo = QPixmap('small_photos/Y2piegraph.png')

        self.buttonLineDiagram_photo = self.buttonLineDiagram_photo.scaledToHeight(500)
        self.buttonHistogram_photo = self.buttonHistogram_photo.scaledToHeight(525)
        self.buttonPieDiagram_photo = self.buttonPieDiagram_photo.scaledToHeight(500)

        self.photos_label_1.setPixmap(self.buttonLineDiagram_photo)
        self.photos_label_2.setPixmap(self.buttonHistogram_photo)
        self.photos_label_3.setPixmap(self.buttonPieDiagram_photo)

        self.photos_label_1.show()
        self.photos_label_2.show()
        self.photos_label_3.show()

        self.layout_photos.addWidget(self.photos_label_1)
        self.layout_photos.addWidget(self.photos_label_2)
        self.layout_photos.addWidget(self.photos_label_3)
