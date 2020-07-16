# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from packet_analyzer.ui.views.object_tree import ObjectTree
from packet_analyzer.ui.widgets.hex_viewer import HexViewer
from packet_analyzer.ui.views.network_event_list import NetworkEventList
from packet_analyzer.ui.views.message_list import MessageList


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(640, 480)
        self.action_open = QAction(main_window)
        self.action_open.setObjectName(u"action_open")
        self.list_view_selector = QActionGroup(main_window)
        self.list_view_selector.setObjectName(u"list_view_selector")
        self.action_view_network_event_list = QAction(self.list_view_selector)
        self.action_view_network_event_list.setObjectName(u"action_view_network_event_list")
        self.action_view_network_event_list.setCheckable(True)
        self.action_view_network_event_list.setChecked(True)
        self.action_view_message_list = QAction(self.list_view_selector)
        self.action_view_message_list.setObjectName(u"action_view_message_list")
        self.action_view_message_list.setCheckable(True)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.central_widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.list_view_stacked = QStackedWidget(self.splitter)
        self.list_view_stacked.setObjectName(u"list_view_stacked")
        self.network_event_list_page = QWidget()
        self.network_event_list_page.setObjectName(u"network_event_list_page")
        self.verticalLayout_3 = QVBoxLayout(self.network_event_list_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.network_event_list = NetworkEventList(self.network_event_list_page)
        self.network_event_list.setObjectName(u"network_event_list")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_event_list.sizePolicy().hasHeightForWidth())
        self.network_event_list.setSizePolicy(sizePolicy)
        self.network_event_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.network_event_list.setRootIsDecorated(False)
        self.network_event_list.setUniformRowHeights(True)
        self.network_event_list.setItemsExpandable(False)
        self.network_event_list.setAllColumnsShowFocus(True)
        self.network_event_list.setExpandsOnDoubleClick(False)
        self.network_event_list.header().setMinimumSectionSize(20)
        self.network_event_list.header().setDefaultSectionSize(35)

        self.verticalLayout_3.addWidget(self.network_event_list)

        self.list_view_stacked.addWidget(self.network_event_list_page)
        self.message_list_page = QWidget()
        self.message_list_page.setObjectName(u"message_list_page")
        self.verticalLayout_4 = QVBoxLayout(self.message_list_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.message_list = MessageList(self.message_list_page)
        self.message_list.setObjectName(u"message_list")
        self.message_list.setRootIsDecorated(False)
        self.message_list.setUniformRowHeights(True)
        self.message_list.setItemsExpandable(False)
        self.message_list.setAllColumnsShowFocus(True)
        self.message_list.setExpandsOnDoubleClick(False)
        self.message_list.header().setMinimumSectionSize(20)
        self.message_list.header().setDefaultSectionSize(39)

        self.verticalLayout_4.addWidget(self.message_list)

        self.list_view_stacked.addWidget(self.message_list_page)
        self.splitter.addWidget(self.list_view_stacked)
        self.object_tree = ObjectTree(self.splitter)
        self.object_tree.setObjectName(u"object_tree")
        self.object_tree.setStyleSheet(u"")
        self.object_tree.setUniformRowHeights(True)
        self.object_tree.setAnimated(True)
        self.object_tree.setAllColumnsShowFocus(True)
        self.splitter.addWidget(self.object_tree)
        self.hex_viewer = HexViewer(self.splitter)
        self.hex_viewer.setObjectName(u"hex_viewer")
        self.hex_viewer.setMinimumSize(QSize(0, 0))
        self.splitter.addWidget(self.hex_viewer)

        self.verticalLayout_2.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widget)

        main_window.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menu_file.addAction(self.action_open)
        self.menuView.addAction(self.action_view_network_event_list)
        self.menuView.addAction(self.action_view_message_list)

        self.retranslateUi(main_window)

        self.list_view_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Packet Analyzer", None))
        self.action_open.setText(QCoreApplication.translate("main_window", u"Open", None))
        self.action_view_network_event_list.setText(QCoreApplication.translate("main_window", u"Network event list", None))
        self.action_view_message_list.setText(QCoreApplication.translate("main_window", u"Message list", None))
        self.menu_file.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("main_window", u"View", None))
    # retranslateUi

