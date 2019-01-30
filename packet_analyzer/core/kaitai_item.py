from kaitaistruct import KaitaiStruct


class KaitaiItem:

    def __init__(self, name, value, start=None, end=None, parent=None):
        self.name = name
        self.value = value

        self.parent = parent

        self.start = start
        self.end = end

        self._members = []

        self._expanded = False

    def _expand(self):
        if not self._expanded:
            if isinstance(self.value, KaitaiStruct):
                if self.value._root is self.value:
                    self.value._read()

                public_members = [(k, v) for k, v in self.value.__dict__.items() if not k.startswith("_")]
                for name, value in public_members:
                    start = self.value._debug[name]["start"]
                    end = self.value._debug[name]["end"]

                    member = KaitaiItem(name, value, start, end, self)
                    self._members.append(member)

                # TODO implement instances
            elif isinstance(self.value, list):
                for idx, el in enumerate(self.value):
                    # May put access to [name][arr] before entering for loop
                    start = self.parent.value._debug[self.name]["arr"][idx]["start"]
                    end = self.parent.value._debug[self.name]["arr"][idx]["end"]

                    member = KaitaiItem(str(idx), el, start, end, self)
                    self._members.append(member)

        self._expanded = True

    @property
    def members(self):
        self._expand()
        return self._members