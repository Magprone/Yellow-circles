import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter, QBrush
from UI import Ui_Form
import random


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.board = Board(self)
        self.layout().addWidget(self.board)
        self.add_circle_button.clicked.connect(self.board.add_circle)


class Board(QWidget):
    draw_circle = False

    def add_circle(self):
        self.draw_circle = True
        width, height = self.width(), self.height()
        self.size = random.randrange(min(width, height))
        self.x, self.y = random.randrange(width - self.size), random.randrange(height - self.size)
        self.update()

    def paintEvent(self, event):
        if self.draw_circle:
            color = QColor(random.randrange(255), random.randrange(255), random.randrange(255))
            brush = QBrush(color)
            painter = QPainter(self)
            painter.setBrush(brush)
            painter.drawEllipse(
                self.x, self.y,
                self.size, self.size
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
