from kaitaistruct import KaitaiStruct


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

        self._parent = None

    def add_child(self, child):
        self.children.append(child)
        child._parent = self

    def child_count(self):
        return len(self.children)

    def child(self, row):
        return self.children[row]

    def row(self):
        if self._parent:
            return self._parent.children.index(self)

    def has_child(self):
        return self.child_count() > 0

    def parent(self):
        return self._parent


class NetworkEventNode(Node):

    def __init__(self, value):
        super(NetworkEventNode, self).__init__(value)
        self._expanded = False

    def _expand(self):
        if not self._expanded:
            for packet in self.value.packets:
                packet_node = KaitaiNode(packet)
                super(NetworkEventNode, self).add_child(packet_node)

        self._expanded = True

    def child_count(self):
        if self._expanded:
            return super(NetworkEventNode, self).child_count()
        else:
            return len(self.value.packets)

    def child(self, row):
        self._expand()
        return super(NetworkEventNode, self).child(row)


class KaitaiNode(Node):

    def __init__(self, value):
        super(KaitaiNode, self).__init__(value)

        self._expanded = False

    def _expand(self):
        if not self._expanded:
            for member in self.value.members:
                kaitai_node = KaitaiNode(member)
                super(KaitaiNode, self).add_child(kaitai_node)

        self._expanded = True

    def child_count(self):
        if self._expanded:
            return super(KaitaiNode, self).child_count()
        else:
            return len(self.value.members)

    def child(self, row):
        self._expand()
        return super(KaitaiNode, self).child(row)


