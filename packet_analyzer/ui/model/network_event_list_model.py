import PySide2
from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex

from anytree import Resolver


class NetworkEventListModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super(NetworkEventListModel, self).__init__(parent)
        self.name_resolver = Resolver('name')

        self.root = None

    def set_root(self, node):
        self.root = node
        self.modelReset.emit()

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Timestamp"
            elif section == 1:
                return "Server address"
            elif section == 2:
                return "Source"
            elif section == 3:
                return "No. packets"

    def index_from_node(self, node):
        r = node.parent.children.index(node)
        return self.createIndex(r, 0, node.parent)

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...):
        if not index.isValid():
            return None

        node = index.internalPointer()
        if role == Qt.DisplayRole:
            column = index.column()
            if column == 0:
                return node.value.timestamp
            elif column == 1:
                return node.value.server
            elif column == 2:
                return node.value.source
            elif column == 3:
                return len(node.value.packets)

    def index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...):
        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()

        child_node = parent_node.children[row]
        return self.createIndex(row, column, child_node)

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...):
        return 4

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...):
        if not parent.isValid():
            return len(self.root.children)

        return 0

    def parent(self, index: PySide2.QtCore.QModelIndex):
        if not index.isValid:
            return QModelIndex()

        child_node = index.internalPointer()
        if not child_node:
            return QModelIndex()

        parent_node = child_node.parent
        if parent_node == self.root:
            return QModelIndex()

        row = parent_node.parent.children.index(parent_node)
        return self.createIndex(row, 0, parent_node)
