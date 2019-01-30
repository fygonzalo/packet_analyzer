import PySide2
from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex

from packet_analyzer.ui.model.node import Node, NetworkEventNode, KaitaiNode


class BaseModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super(BaseModel, self).__init__(parent)
        self.root_node = Node(None)

    def set_root_node(self, root_node):
        self.root_node = root_node

    def index(self, row:int, column:int, parent:PySide2.QtCore.QModelIndex=...):
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()

        child_node = parent_node.child(row)
        return self.createIndex(row, column, child_node)

    def data(self, index:PySide2.QtCore.QModelIndex, role:int=...):
        if not index.isValid():
            return None

        node = index.internalPointer()
        if role == Qt.DisplayRole:
            column = index.column()
            if column <= 3:
                if isinstance(node, NetworkEventNode):
                    if column == 0:
                        return node.value.timestamp
                    elif column == 1:
                        return node.value.server
                    elif column == 2:
                        return node.value.source
                    elif column == 3:
                        return node.value.packet_count
                else:
                    return None
            elif column == 4:
                if isinstance(node, KaitaiNode):
                    return node.value.name
                else:
                    return None

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...):

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Timestamp"
            elif section == 1:
                return "Server"
            elif section == 2:
                return "Source"
            elif section == 3:
                return "No. packets"
            elif section == 4:
                return "Packets"

    def rowCount(self, parent:PySide2.QtCore.QModelIndex=...):
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()

        return parent_node.child_count()

    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...):
        return 1

    def parent(self, index):
        if not index.isValid:
            return QModelIndex()

        child_node = index.internalPointer()
        if not child_node:
            return QModelIndex()

        parent_node = child_node.parent()
        if parent_node == self.root_node:
            return QModelIndex()

        return self.createIndex(parent_node.row(), 0, parent_node)