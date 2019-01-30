# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Tue Jan 29 21:22:07 2019
#      by: pyside2-uic  running on PySide2 5.12.1a1.dev1549512584
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(640, 480)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.event_list = EventList(self.splitter)
        self.event_list.setObjectName("event_list")
        self.object_tree = ObjectTree(self.splitter)
        self.object_tree.setObjectName("object_tree")
        self.hex_viewer = HexViewer(self.splitter)
        self.hex_viewer.setMinimumSize(QtCore.QSize(0, 0))
        self.hex_viewer.setObjectName("hex_viewer")
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setObjectName("action_open")
        self.menu_file.addAction(self.action_open)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtWidgets.QApplication.translate("main_window", "Packet Analyzer", None, -1))
        self.menu_file.setTitle(QtWidgets.QApplication.translate("main_window", "File", None, -1))
        self.action_open.setText(QtWidgets.QApplication.translate("main_window", "Open", None, -1))

from packet_analyzer.ui.widgets.hex_viewer import HexViewer
from packet_analyzer.ui.views.event_list import EventList
from packet_analyzer.ui.views.object_tree import ObjectTree
