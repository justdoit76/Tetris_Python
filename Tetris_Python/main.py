from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QCloseEvent, QKeyEvent, QPaintEvent, QPainter
from game import Tetris
import sys

from PyQt5.QtCore import Qt
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ocean Coding School')
        self.setFixedSize(340,640)
        self.tetris = Tetris(self)        
        
    def paintEvent(self, e) -> None:
        qp = QPainter()
        qp.begin(self)
        self.tetris.draw(qp)
        qp.end()
        return super().paintEvent(e)        
        
    def keyPressEvent(self, e) -> None:
        self.tetris.keyDown(e.key())
        return super().keyPressEvent(e)        
    
    def closeEvent(self, e) -> None:      
        self.tetris.run = False
        return super().closeEvent(e)    
    
    def gameOver(self):
        result = QMessageBox.information(self, 'Game Over!', 'Retry(Y), Exit(N)',
                                         QMessageBox.Yes| QMessageBox.No)
        
        if result==QMessageBox.Yes:
            del(self.tetris)
            self.tetris = Tetris(self)
        else:
            self.close()        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())