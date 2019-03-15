import PySide2
from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex

from anytree import Resolver


class MessageListModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super(MessageListModel, self).__init__(parent)
        self.message_list = []
        self.name_resolver = Resolver('name')

    def set_message_list(self, message_list):
        self.message_list = message_list

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Server"
            elif section == 1:
                return "Code"
            elif section == 2:
                return "Type"
            elif section == 3:
                return "Subtype"

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...):
        if not index.isValid():
            return None

        node = index.internalPointer()
        if role == Qt.DisplayRole:
            column = index.column()
            if column == 0:
                return self.name_resolver.get(node, '../../../../../../server').value
            elif column == 1:
                return node.value.code
            elif column == 2:
                return self.name_resolver.get(node, './content').class_name
            elif column == 3:
                return self.name_resolver.get(node, './content/content').class_name

    def index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...):
        return self.createIndex(row, column, self.message_list[row])

    def parent(self, index: PySide2.QtCore.QModelIndex):
        return QModelIndex()

    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...):
        return 4

    def rowCount(self, parent:PySide2.QtCore.QModelIndex=...):
        if not parent.isValid():
            return len(self.message_list)

        return 0