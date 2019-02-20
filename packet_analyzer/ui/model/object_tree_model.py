import PySide2
from PySide2.QtCore import Qt, QModelIndex, QAbstractItemModel


class ObjectTreeModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super(ObjectTreeModel, self).__init__(parent)
        self.root = None

    def set_root(self, root):
        self.root = root
        self.modelReset.emit()

    def get_index_from_node(self, node):
        parent_node = node.parent
        row = parent_node.parent.children.index(parent_node)
        return self.createIndex(row, 0, node)

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Object tree"

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...):
        if not index.isValid():
            return None

        node = index.internalPointer()
        if role == Qt.DisplayRole:
            if node.is_leaf:
                return "{}: {}".format(node.name, node.value)
            else:
                return "{} [{}]".format(node.name, node.class_name)

        return None

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...):
        return 1

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...):
        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()

        return len(parent_node.children)

    def index_from_node(self, node):
        r = node.parent.children.index(node)
        return self.createIndex(r, 0, node)

    def index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...):
        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()

        child_node = parent_node.children[row]
        return self.createIndex(row, column, child_node)

    def parent(self, index):
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
