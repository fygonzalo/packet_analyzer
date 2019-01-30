import PySide2
from PySide2.QtGui import QColor, QPalette
from PySide2.QtCore import Qt, QObject, Slot
from PySide2.QtWidgets import QTreeView, QAction, QActionGroup, QMenu, QFileDialog

from packet_analyzer.ui.model.node import KaitaiNode
from kaitaistruct import KaitaiStruct


class ObjectTree(QTreeView):
    
    def __init__(self, parent=None):
        super(ObjectTree, self).__init__(parent)

        self.menu = QMenu(parent=self)
        self.createContextMenu()

    def createContextMenu(self):
        self.action_export_bin = QAction("Export as binary file", self)
        self.action_export_hex = QAction("Export as hex string", self)
        self.menu.addAction(self.action_export_bin)
        self.menu.addAction(self.action_export_hex)

    def mouseReleaseEvent(self, event:PySide2.QtGui.QMouseEvent):
        if event.button() == Qt.RightButton:
            item = self.indexAt(event.pos())
            if item.isValid():
                kaitai_struct = item.internalPointer().value.value
                if isinstance(kaitai_struct, KaitaiStruct) and kaitai_struct == kaitai_struct._root:
                    selected = self.menu.exec_(self.mapToGlobal(event.pos()))
                    if selected:
                        file_path, _ = QFileDialog.getSaveFileName(self, "Save file")
                        if not file_path:
                            return

                        last_pos = kaitai_struct._io._io.tell()
                        kaitai_struct._io._io.seek(0)

                        data = kaitai_struct._io.read_bytes_full()

                        kaitai_struct._io._io.seek(last_pos)

                        if selected == self.action_export_bin:
                            file = open(file_path, "wb")
                            file.write(data)
                            file.close()
                        else:
                            file = open(file_path, "w")
                            file.write(data.hex())
                            file.close()

        else:
            super(ObjectTree, self).mouseReleaseEvent(event)