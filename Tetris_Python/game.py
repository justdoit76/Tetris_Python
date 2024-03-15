from PyQt5.QtCore import Qt, QRectF, QObject, pyqtSignal
from PyQt5.QtGui import QBrush, QColor
from blocks import BO,BI,BS,BZ,BL,BJ,BT, BType
from threading import Thread
from random import randint
import time

class Tetris(QObject):
    
    Row = 20
    Col = 10   
    Blocks = (BO, BI, BS, BZ, BL, BJ, BT)
    update_signal = pyqtSignal()
    
    def __init__(self, w):
        super().__init__()
        self.parent = w
        self.rect = w.rect()
        
        self.inrect = QRectF(self.rect)
        gap = 20
        self.inrect.adjust(gap, gap, -gap, -gap)        

        self.size = self.inrect.width() / (Tetris.Col-1) 
        
        # block        
        n = randint(BType.O.value, BType.T.value)
        print(n)
        self.block = Tetris.Blocks[n]()
        
        # logical map
        self.maps = [[False for _ in range(Tetris.Col)] for _ in range(Tetris.Row)] 
        
        # displayed map        
        self.rects = []
        x = self.inrect.left()        
        y = self.inrect.top()
        for r in range(Tetris.Row):
            temp = []
            for c in range(Tetris.Col):
                dx = x+c*self.size
                dy = y+r*self.size
                rect = QRectF(dx, dy, self.size, self.size)
                temp.append(rect)
            self.rects.append(temp)
            
        # standard row, col
        self.strow = 0
        self.stcol = Tetris.Col//2-self.block.Size//2
        
        # signal
        self.update_signal.connect(w.update)
        
        # thread
        self.t = Thread(target = self.threadFunc)
        self.run = True
        self.t.start()        
        
    def draw(self, qp):
        self.drawBackground(qp)
        self.drawBlock(qp)
        
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
    
    def drawBlock(self, qp):
        b = QBrush(QColor(255,0,0))
        qp.setBrush(b)
                   
        for r in range(Tetris.Row):
            for c in range(Tetris.Col):
                if self.maps[r][c]:
                    qp.drawRect(self.rects[r][c])

    def keyDown(self, key):
        if key==Qt.Key_Left:
            temp = self.block.rotate_l()
            self.block.print()
        elif key==Qt.Key_Right:
            temp = self.block.rotate_r()
            self.block.print()            
        elif key==Qt.Key_Up:
            pass
        elif key==Qt.Key_Down:
            pass
        
    def blockDown(self):
        bl = self.block.arr
        size = self.block.Size
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:
                    if self.strow-r>=0:
                        # delete before line
                        if self.strow-1>0:
                            for d in range(Tetris.Col):
                                self.maps[self.strow-r-1][d]=False
                        
                        self.maps[self.strow-r][c+self.stcol]=True
            

    def threadFunc(self):
        while self.run: 
            #print(self.strow, self.stcol)
            self.blockDown()
            
            if self.strow>=Tetris.Row-1:
                self.strow = 0
                self.stcol = Tetris.Col//2-self.block.Size//2
                
            self.strow+=1
            
            self.update_signal.emit()
            time.sleep(1)
        print('thread finished...')