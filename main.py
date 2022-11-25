import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5.QtCore import Qt
from random import randint
from math import factorial, sqrt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(589, 520)
        self.label.setPixmap(canvas)

    def circle(self):
        x = random.randint(10, 480)
        y = random.randint(10, 420)
        d = random.randint(10, 80)
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, d, d)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())