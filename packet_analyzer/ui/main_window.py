import os

from PySide2.QtCore import Slot, QModelIndex
from PySide2.QtWidgets import QMainWindow, QFileDialog

from packet_analyzer.ui.resources.main_window import Ui_main_window
from packet_analyzer.ui.model.base_model import BaseModel
from packet_analyzer.ui.model.list_model import ListModel
from packet_analyzer.ui.model.tree_model import TreeModel

from packet_analyzer.ui.model.node import Node, NetworkEventNode
from packet_analyzer.core.game_session import GameSession


class MainWindow(QMainWindow, Ui_main_window):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.window_title = self.windowTitle()

        self._setup_slots()

    def _setup_slots(self):
        # MenuBar
        self.action_open.triggered.connect(self.on_file_open_clicked)
        self.event_list.activated.connect(self.on_event_list_activated)
        self.object_tree.clicked.connect(self.on_object_tree_clicked)

    def on_file_open_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(self)

        if os.path.isfile(file_path):
            game_session = GameSession.from_file(file_path)

            self.setWindowTitle(file_path + " - " + self.window_title)

            root_node = Node(None)
            for network_event in game_session.network_events:
                network_event_node = NetworkEventNode(network_event)
                root_node.add_child(network_event_node)

            model = BaseModel(self)
            model.set_root_node(root_node)

            list_model = ListModel(self)
            list_model.setSourceModel(model)
            self.event_list.setModel(list_model)

            tree_model = TreeModel(self)
            tree_model.setSourceModel(model)
            self.object_tree.setModel(tree_model)
            self.object_tree.setRootIndex(tree_model.index(0, 0, QModelIndex()))

            self.on_object_tree_clicked(self.object_tree.rootIndex().child(0, 0))


    @Slot(QModelIndex)
    def on_event_list_activated(self, index: QModelIndex):
        base_model_idx = self.event_list.model().mapToSource(index)
        tree_model_idx = self.object_tree.model().mapFromSource(base_model_idx)
        self.object_tree.setRootIndex(tree_model_idx)

        self.on_object_tree_clicked(self.object_tree.rootIndex().child(0, 0))

    @Slot(QModelIndex)
    def on_object_tree_clicked(self, index: QModelIndex):
        base_model_idx = self.object_tree.model().mapToSource(index)

        element = base_model_idx.internalPointer()
        kaitai_struct = element.value.value

        if kaitai_struct._root is kaitai_struct:
            last_pos = kaitai_struct._io._io.tell()
            kaitai_struct._io._io.seek(0)

            self.hex_viewer.set_data(kaitai_struct._io.read_bytes_full())

            kaitai_struct._io._io.seek(last_pos)

