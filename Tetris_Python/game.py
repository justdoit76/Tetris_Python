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

        self.size = self.inrect.height() / Tetris.Row
        
        # create block
        self.initBlock()
        
        # logical map (0:None, 1:Move block, 2:Stacked block)
        self.before = []
        self.maps = [[0 for _ in range(Tetris.Col)] for _ in range(Tetris.Row)] 
        
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
            
        
        # signal
        self.update_signal.connect(w.update)
        
        # thread
        self.t = Thread(target = self.threadFunc)
        self.run = True
        self.t.start()   
        
    def initBlock(self):
         # block        
        n = randint(BType.O.value, BType.T.value)
        print('Block Type:', n)
        self.block = Tetris.Blocks[n]()
        
        # standard row, col        
        self.strow = -1
        self.stcol = Tetris.Col//2-self.block.Size//2
        
    def draw(self, qp):
        self.drawBackground(qp)
        self.drawBlock(qp)
        
        # for debug        
        b = QBrush(QColor(0,0,200))
        qp.setBrush(b)
        if self.strow>=0 and self.strow<Tetris.Row:
            qp.drawEllipse(self.rects[self.strow][self.stcol])
        print(self.strow, self.stcol)
        
    def drawBackground(self, qp):
        x = self.inrect.left()        
        y = self.inrect.top()
        
        x2 = self.inrect.right()
        y2 = self.inrect.top()
        
        x3 = self.inrect.left()
        y3 = self.inrect.bottom()
        
        for i in range(Tetris.Row+1):
            qp.drawLine(x, y+i*self.size, x2, y2+i*self.size)
            if i<Tetris.Col+1:
                qp.drawLine(x+i*self.size, y, x3+i*self.size, y3)
    
    def drawBlock(self, qp):
        b = QBrush(QColor(255,0,0))
        qp.setBrush(b)
                   
        for r in range(Tetris.Row):
            for c in range(Tetris.Col):
                if self.maps[r][c]!=0:
                    qp.drawRect(self.rects[r][c])
                    qp.drawText(self.rects[r][c], Qt.AlignCenter, f'{self.maps[r][c]}')

    def keyDown(self, key):
        if key==Qt.Key_Left:
            if self.stcol>0:
                self.stcol-=1
                self.blockUpdate()
                self.update_signal.emit()
        elif key==Qt.Key_Right:
            if self.stcol<Tetris.Col-1:
                self.stcol+=1
                self.blockUpdate()
                self.update_signal.emit()
        elif key==Qt.Key_Up:
            self.block.rotate_r()
            self.blockUpdate()
            self.update_signal.emit()            
        elif key==Qt.Key_Down:
            if self.strow<Tetris.Row-1:
                self.strow+=1
                self.blockUpdate()
                self.update_signal.emit()
            
        
    def blockUpdate(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size        
        
        # delete before blocks
        for r, c in self.before:
            self.maps[r][c] = 0
        self.before.clear()
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:
                    if self.strow-r>=0:
                        self.maps[self.strow-r][c+self.stcol]=1
                        # remember current blocks
                        self.before.append( (self.strow-r, c+self.stcol) )
                        
    def isMoveDown(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:                    
                    if self.strow - r + 1 > Tetris.Row-1:
                        self.before.clear()
                        return False                    
                    elif self.strow-r >= 0:
                        if self.maps[self.strow-r+1][c+self.stcol]==2:                            
                            self.before.clear() 
                            return False
        return True
    
    def stackBlock(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size  
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:                
                    self.maps[self.strow-r][c+self.stcol]=2
                

    def threadFunc(self):
        while self.run:             
            time.sleep(0.5)
            self.blockUpdate()
            if not self.isMoveDown():
                self.stackBlock()
                self.initBlock()
            
            self.strow+=1            
            self.update_signal.emit()
        print('thread finished...')