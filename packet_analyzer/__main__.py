import sys

from PySide2.QtWidgets import QApplication
from packet_analyzer.ui import MainWindow


if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_window = MainWindow()

    application.setStyle("fusion")

    main_window.show()
    application.exec_()