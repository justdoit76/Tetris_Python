from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from game import Tetris
import sys

# from PyQt5.QtCore import Qt
# QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ocean Coding School')
        self.setFixedSize(400,800)
        self.tetris = Tetris(self)        
        
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.tetris.draw(qp)
        qp.end()
        
    def keyPressEvents(self, e):
        pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
