import sys
from PyQt6.QtWidgets import QApplication

from MW_main_window import MainWindow


def main():
    """using this for running the program"""

    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()
