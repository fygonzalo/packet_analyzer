from PySide2.QtCore import Qt, QObject, Slot, QModelIndex
from PySide2.QtWidgets import QTreeView, QAbstractItemView, QHeaderView


class EventList(QTreeView):
    
    def __init__(self, parent=None):
        super(EventList, self).__init__(parent)

        self.setRootIsDecorated(False)
        self.setUniformRowHeights(True)
        self.setItemsExpandable(False)
        #self.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.setSortingEnabled(True)
        #self.activated.connect(self.network_event_selected)
        #self.header().hideSection(4)


    @Slot(QModelIndex)
    def network_event_selected(self, index):
        network_event = index.internalPointer()
        #self.main_controller.on_network_event_selected(network_event)
        self.header().setStretchLastSection(True)