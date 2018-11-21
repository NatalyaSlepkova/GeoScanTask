from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QLinearGradient, QBrush

class MyWidget(QtWidgets.QWidget):
    def __init__(self, ground, water):
        super().__init__()
        screen_width = 1366
        screen_height = 768
        self.block_default_side = 50
        self.block_count = len(ground)
        self.setGeometry(0,0,screen_width,screen_height)
        self.ground = ground
        self.water = water

        self.show()

    def paintEvent(self, event):
        side = min(self.width(), self.height()) / self.block_count  # scalable side blocks
        if side > self.block_default_side:
            side = self.block_default_side

        qp = QPainter()
        qp.begin(self)
        center_origin = (self.width() - side * self.block_count) / 2
        print("origin is " + str(self.width()))
        for i in range(self.block_count):
            h = self.ground[i]
            for k in range(self.ground[i] + self.water[i]):
                x = (i + 1) * side
                y = self.height() - (k + 1) * side
                type = 'ground'
                if k >= h: # ground is ended
                    type = 'water'
                self.draw_block(qp, x, y, side, type, center_origin)
        qp.end()

    @staticmethod
    def draw_block(qp, x, y, side_size, type, origin):  # drawing a block with alignment relative to the center of the image
        col = QColor(255, 255, 255)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        gradient = QLinearGradient(x + origin, y, x + origin + side_size, y + side_size)
        if type == 'ground':
            gradient.setColorAt(0.0, QColor(100, 60, 60))
            gradient.setColorAt(1.0, QColor(170, 150, 150))
        else:
            gradient.setColorAt(0.0, QColor(0, 13, 179))
            gradient.setColorAt(1.0, QColor(0, 255, 237))
        qp.setBrush(QBrush(gradient))
        qp.drawRect(x + origin - side_size , y, side_size, side_size)
