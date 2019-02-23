import PySide2
from PySide2.QtCore import Qt, QObject, Slot, QModelIndex
from PySide2.QtWidgets import QTreeView, QAbstractItemView, QHeaderView


class MessageList(QTreeView):

    def __init__(self, parent=None):
        super(MessageList, self).__init__(parent)

    def setModel(self, model:PySide2.QtCore.QAbstractItemModel):
        super(MessageList, self).setModel(model)
        self.header().resizeSections(QHeaderView.ResizeToContents)