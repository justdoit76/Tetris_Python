from PyQt5.QtCore import Qt, QRectF
from blocks import BO,BI,BS,BZ,BL,BJ,BT
from threading import Thread
import time

class Tetris:
    
    Row = 20
    Col = 10   
    
    def __init__(self, w):
        self.parent = w
        self.rect = w.rect()
        
        self.inrect = QRectF(self.rect)
        gap = 20
        self.inrect.adjust(gap, gap, -gap, -gap)
        
        self.size = self.inrect.width() / (Tetris.Col-1)            
        
        self.bo = BT()
        self.bo.print()
        
        
    def draw(self, qp):
        self.drawBackground(qp)
        
    def drawBackground(self, qp):
        x = self.inrect.left()        
        y = self.inrect.top()
        
        x2 = self.inrect.right()
        y2 = self.inrect.top()
        
        x3 = self.inrect.left()
        y3 = self.inrect.bottom()
        
        for i in range(Tetris.Row):
            qp.drawLine(x, y+i*self.size, x2, y2+i*self.size)
            if i<Tetris.Col:
                qp.drawLine(x+i*self.size, y, x3+i*self.size, y3)
        
        
        
