import PySide2
from PySide2.QtCore import Qt, QModelIndex, QIdentityProxyModel

from packet_analyzer.ui.model.node import KaitaiNode

from packet_analyzer.core.kaitai_item import KaitaiItem
from kaitaistruct import KaitaiStruct


NATIVE_OBJECT = "{}: {}"
COLLECTION = "{}"
KAITAI_OBJECT = "{} [{}]"


class TreeModel(QIdentityProxyModel):

    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Object tree"

    def data(self, proxyIndex:PySide2.QtCore.QModelIndex, role:int=...):
        if not proxyIndex.isValid():
            return None

        node = proxyIndex.internalPointer()
        if isinstance(node, KaitaiNode):
            kaitai_item = node.value
            if role == Qt.DisplayRole:
                if isinstance(kaitai_item.value, KaitaiStruct):
                    text = KAITAI_OBJECT.format(kaitai_item.name, kaitai_item.value.__class__.__name__)
                elif isinstance(kaitai_item.value, list):
                    text = COLLECTION.format(kaitai_item.name)
                elif isinstance(kaitai_item.value, bytes):
                    text = NATIVE_OBJECT.format(kaitai_item.name, (kaitai_item.value).hex())
                else:
                    text = NATIVE_OBJECT.format(kaitai_item.name, kaitai_item.value)

                return text

    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...):
        return 1