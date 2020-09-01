import PySide2
from PySide2.QtWidgets import QAbstractScrollArea, QApplication
from PySide2.QtGui import QTextLayout, QPainter, QFontMetrics, QFont, QFontDatabase
from PySide2.QtCore import QRect, QPointF


# --- Util
import re
from itertools import chain
concatenated = chain(range(30), range(2000, 5002))
all_chars = (chr(i) for i in range(0x110000))

control_chars = ''.join(map(chr, chain(range(0,32), range(126,160))))
control_chars_re = re.compile('[%s]' % re.escape(control_chars))


def remove_control_chars(s):
    return control_chars_re.sub('.', s)


class HexViewer(QAbstractScrollArea):

    def __init__(self, parent=None):
        super(HexViewer, self).__init__(parent)

        # Local
        self.data = None
        self.layout = QTextLayout()

        # Properties
        self.row_width = 16

        # Calculated
        self.font_width = None
        self.line_height = None

        # Initialization
        self.layout.setCacheEnabled(True)
        self._set_font()

    def _set_font(self):
        mono_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        mono_font.setStyleStrategy(QFont.ForceIntegerMetrics)
        mono_font.setFixedPitch(True)
        mono_font.setPointSize(9)

        font_metrics = QFontMetrics(mono_font)

        self.font_width = font_metrics.width("M")

        self.setFont(mono_font)
        self.layout.setFont(mono_font)
        self.viewport().setFont(mono_font)

        self.line_height = self.fontMetrics().height()

        self.viewport().update()

    def _offset_width_chars(self, include_padding=True):
        padding = 2 if include_padding else 0
        if self.data and len(self.data) > 0xffff:
            return 8 + padding
        return 4 + padding

    def _offset_width_pixels(self):
        zeroes = '0' * self._offset_width_chars()
        return self.fontMetrics().width(zeroes)

    def _hex_width_pixels(self):
        zeroes = '0' * (self.row_width * 2 + 3)
        return self.fontMetrics().width(zeroes)

    def _ascii_width_pixels(self):
        zeroes = '0' * (self.row_width * 2 + 2)
        return self.fontMetrics().width(zeroes)

    def _total_width_pixels(self):
        return self._offset_width_pixels() + self._hex_width_pixels() + self._ascii_width_pixels()

    def update_scroll_bars(self):
        if not self.data:
            return

        data_len = len(self.data)
        all_lines_height = data_len / self.row_width + ((2 if (data_len % self.row_width ) else 0) - self.viewport().height() / self.line_height)

        self.verticalScrollBar().setRange(0, max(0, all_lines_height + 1))
        self.horizontalScrollBar().setRange(0, max(0, int((self._total_width_pixels() - self.viewport().width())) / self.font_width))

    def resizeEvent(self, arg__1:PySide2.QtGui.QResizeEvent):
        self.update_scroll_bars()

    def _draw_row(self, painter, offset, row_y):
        if not self.data:
            return

        # Row build
        row_offset = " {:04X} ".format(offset)

        row_raw_hex = self.data[offset:offset + self.row_width].hex()
        if len(row_raw_hex) < self.row_width * 2:
            row_raw_hex += ' ' * (self.row_width * 2 - len(row_raw_hex))
        row_hex = ' '.join([row_raw_hex[i:i+2] for i in range(0, len(row_raw_hex), 2)])

        row_raw_ascii = self.data[offset:offset + self.row_width].decode("ascii", "replace").replace(u"\ufffd", ".")
        row_ascii = remove_control_chars(row_raw_ascii)

        row = row_offset + " " + row_hex + "  " + row_ascii

        # Paint
        self.layout.clearLayout()
        self.layout.setText(row)
        self.layout.beginLayout()
        line = self.layout.createLine()
        line.setLineWidth(1000)
        line.setLeadingIncluded(True)
        self.layout.endLayout()
        self.layout.draw(painter, QPointF(0.0, row_y))

    def set_data(self, data):
        self.data = data
        self.update_scroll_bars()
        self.viewport().update()

    def paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent):
        painter = QPainter(self.viewport())
        painter.translate(-self.horizontalScrollBar().value() * self.font_width, 0)

        # Pixel offset of this row
        row_y = 0

        # Starting byte offset
        offset = self.verticalScrollBar().value() * self.row_width

        painter.fillRect(self.viewport().rect(), self.palette().base())

        offset_rect = QRect(self.viewport().rect())
        offset_rect.setWidth(self._offset_width_pixels())
        painter.fillRect(offset_rect, self.palette().window())


        ascii_rect = QRect(self.viewport().rect())
        ascii_rect.setX(ascii_rect.x() + self._offset_width_pixels() + self._hex_width_pixels() + 96)
        ascii_rect.setWidth(2)
        painter.fillRect(ascii_rect, self.palette().window())

        if not self.data:
            return None

        widget_height = self.height()
        leading = self.fontMetrics().leading()

        painter.save()

        while row_y + self.line_height < widget_height and offset < len(self.data):
            self._draw_row(painter, offset, row_y)
            offset += self.row_width
            row_y += self.line_height + leading

        painter.restore()
