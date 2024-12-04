import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.clicked_pushButton)

    def clicked_pushButton(self):
        rad = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(color)
        if self.cur_figure == 'круг':
            qp.drawEllipse(QPointF(*self.center), rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    evaluator = Suprematism()
    evaluator.show()
    sys.exit(app.exec())
