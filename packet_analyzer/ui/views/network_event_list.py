import PySide2
from PySide2.QtCore import Qt, QObject, Slot, QModelIndex
from PySide2.QtWidgets import QTreeView, QAbstractItemView, QHeaderView


class NetworkEventList(QTreeView):

    def __init__(self, parent=None):
        super(NetworkEventList, self).__init__(parent)

    def setModel(self, model:PySide2.QtCore.QAbstractItemModel):
        super(NetworkEventList, self).setModel(model)
        self.header().resizeSections(QHeaderView.ResizeToContents)