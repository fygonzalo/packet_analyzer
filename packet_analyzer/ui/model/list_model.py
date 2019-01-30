import PySide2
from PySide2.QtCore import Qt, QAbstractProxyModel, QModelIndex, QIdentityProxyModel, QSortFilterProxyModel

from packet_analyzer.ui.model.node import NetworkEventNode


class ListModel(QIdentityProxyModel):
    
    def __init__(self, parent=None):
        super(ListModel, self).__init__(parent)

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Timestamp"
            elif section == 1:
                return "Server address"
            elif section == 2:
                return "Source"
            elif section == 3:
                return "No. packets"

    def data(self, proxyIndex:PySide2.QtCore.QModelIndex, role:int=...):
        if not proxyIndex.isValid():
            return None

        node = proxyIndex.internalPointer()
        if role == Qt.DisplayRole:
            column = proxyIndex.column()
            if column == 0:
                return node.value.timestamp
            elif column == 1:
                return node.value.server
            elif column == 2:
                return node.value.source
            elif column == 3:
                return node.value.packet_count

    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...):
        return 4