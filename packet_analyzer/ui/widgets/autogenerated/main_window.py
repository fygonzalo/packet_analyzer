# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Sat Feb 23 01:15:57 2019
#      by: pyside2-uic  running on PySide2 5.12.1
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
        self.list_view_stacked = QtWidgets.QStackedWidget(self.splitter)
        self.list_view_stacked.setObjectName("list_view_stacked")
        self.network_event_list_page = QtWidgets.QWidget()
        self.network_event_list_page.setObjectName("network_event_list_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.network_event_list_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.network_event_list = NetworkEventList(self.network_event_list_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_event_list.sizePolicy().hasHeightForWidth())
        self.network_event_list.setSizePolicy(sizePolicy)
        self.network_event_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.network_event_list.setRootIsDecorated(False)
        self.network_event_list.setUniformRowHeights(True)
        self.network_event_list.setItemsExpandable(False)
        self.network_event_list.setAllColumnsShowFocus(True)
        self.network_event_list.setExpandsOnDoubleClick(False)
        self.network_event_list.setObjectName("network_event_list")
        self.network_event_list.header().setDefaultSectionSize(35)
        self.network_event_list.header().setMinimumSectionSize(20)
        self.verticalLayout_3.addWidget(self.network_event_list)
        self.list_view_stacked.addWidget(self.network_event_list_page)
        self.message_list_page = QtWidgets.QWidget()
        self.message_list_page.setObjectName("message_list_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.message_list_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.message_list = MessageList(self.message_list_page)
        self.message_list.setRootIsDecorated(False)
        self.message_list.setUniformRowHeights(True)
        self.message_list.setItemsExpandable(False)
        self.message_list.setAllColumnsShowFocus(True)
        self.message_list.setExpandsOnDoubleClick(False)
        self.message_list.setObjectName("message_list")
        self.message_list.header().setDefaultSectionSize(39)
        self.message_list.header().setMinimumSectionSize(20)
        self.verticalLayout_4.addWidget(self.message_list)
        self.list_view_stacked.addWidget(self.message_list_page)
        self.object_tree = ObjectTree(self.splitter)
        self.object_tree.setStyleSheet("")
        self.object_tree.setUniformRowHeights(True)
        self.object_tree.setAnimated(True)
        self.object_tree.setAllColumnsShowFocus(True)
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
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setObjectName("action_open")
        self.list_view_selector = QtWidgets.QActionGroup(main_window)
        self.list_view_selector.setObjectName("list_view_selector")
        self.action_view_network_event_list = QtWidgets.QAction(self.list_view_selector)
        self.action_view_network_event_list.setCheckable(True)
        self.action_view_network_event_list.setChecked(True)
        self.action_view_network_event_list.setObjectName("action_view_network_event_list")
        self.action_view_message_list = QtWidgets.QAction(self.list_view_selector)
        self.action_view_message_list.setCheckable(True)
        self.action_view_message_list.setObjectName("action_view_message_list")
        self.menu_file.addAction(self.action_open)
        self.menuView.addAction(self.action_view_network_event_list)
        self.menuView.addAction(self.action_view_message_list)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(main_window)
        self.list_view_stacked.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtWidgets.QApplication.translate("main_window", "Packet Analyzer", None, -1))
        self.menu_file.setTitle(QtWidgets.QApplication.translate("main_window", "File", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("main_window", "View", None, -1))
        self.action_open.setText(QtWidgets.QApplication.translate("main_window", "Open", None, -1))
        self.action_view_network_event_list.setText(QtWidgets.QApplication.translate("main_window", "Network event list", None, -1))
        self.action_view_message_list.setText(QtWidgets.QApplication.translate("main_window", "Message list", None, -1))

from packet_analyzer.ui.widgets.hex_viewer import HexViewer
from packet_analyzer.ui.views.message_list import MessageList
from packet_analyzer.ui.views.object_tree import ObjectTree
from packet_analyzer.ui.views.network_event_list import NetworkEventList