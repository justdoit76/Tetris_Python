from PyQt5.QtCore import Qt, QRectF, QObject, pyqtSignal
from PyQt5.QtGui import QBrush, QColor
from blocks import BO,BI,BS,BZ,BL,BJ,BT, BType
from threading import Thread, Lock
from random import randint
import time

class Tetris(QObject):
    
    Row = 20
    Col = 10
    Blocks = (BO, BI, BS, BZ, BL, BJ, BT)
    update_signal = pyqtSignal()
    gameover_signal = pyqtSignal()
    
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
        
        # create map
        self.initMap()
        
        # signal
        self.update_signal.connect(w.update)
        self.gameover_signal.connect(w.gameOver)
        
        # thread
        self.cs = Lock()
        self.t = Thread(target = self.threadFunc)
        self.run = True
        self.t.start()   
        
    def initBlock(self):
         # block        
        n = randint(BType.O.value, BType.T.value)
        print('Block Type:', n)
        self.block = Tetris.Blocks[n]()
        
        # standard row, col        
        self.cy = -1
        self.cx = Tetris.Col//2-self.block.Size//2
        
    def initMap(self):
        # color map
        self.cmaps = [[(0,0,0,0) for _ in range(Tetris.Col)] for _ in range(Tetris.Row)] 

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
        
    def draw(self, qp):
        self.drawBackground(qp)
        self.drawBlock(qp)
        
        # for debug        
        # b = QBrush(QColor(0,0,200))
        # qp.setBrush(b)
        # if self.cy>=0 and self.cy<Tetris.Row:
        #     qp.drawEllipse(self.rects[self.cy][self.cx])        
        
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
                   
        for r in range(Tetris.Row):
            for c in range(Tetris.Col):
                if self.maps[r][c]!=0:
                    if self.maps[r][c]==1:
                        R, G, B, A = self.block.color
                        b = QBrush(QColor(R,G,B,A))
                        qp.setBrush(b)
                    else:
                        R, G, B, A = self.cmaps[r][c]
                        b = QBrush(QColor(R,G,B,A))                        
                        qp.setBrush(b)
                else:
                    qp.setBrush(Qt.NoBrush)                    

                qp.drawRect(self.rects[r][c])
                qp.drawText(self.rects[r][c], Qt.AlignCenter, f'{self.maps[r][c]}')

    def keyDown(self, key):
        self.cs.acquire()
        
        # find tail of blocks
        U, D, L, R = self.block.findTail()        

        if key==Qt.Key_Left:
            if self.cx>0-L:
                self.cx-=1
                self.blockUpdate()                
        elif key==Qt.Key_Right:
            if self.cx<Tetris.Col-1-R:
                self.cx+=1
                self.blockUpdate()                
        elif key==Qt.Key_Up:
            self.block.rotate_r()
            U, D, L, R = self.block.findTail()
            if self.cx<0-L or self.cx>Tetris.Col-1-R:
                self.block.rotate_l()
            self.blockUpdate()   
            self.block.print()
        elif key==Qt.Key_Down:            
            if self.cy-D<Tetris.Row-2:
                self.cy+=1
                self.blockUpdate()
                
        self.cs.release()
        
    def blockUpdate(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size        
        
        # delete before blocks
        for r, c in self.before:
            self.maps[r][c] = 0
        self.before.clear()
        
        # set current blocks
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:
                    if self.cy-r>=0:
                        self.maps[self.cy-r][c+self.cx]=1
                        # remember current blocks
                        self.before.append( (self.cy-r, c+self.cx) )
               
        # stack or not
        if not self.isMoveDown():
            if self.cy<=1:
                return False
            self.stackBlock()
            self.removeBlock()
            self.initBlock()
        
        self.update_signal.emit()        
        return True
                        
    def isMoveDown(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:                   
                    # bottom of map
                    if self.cy - r + 1 > Tetris.Row-1:
                        self.before.clear()
                        return False                    
                    elif self.cy-r >= 0:
                        # found stacked block
                        if self.maps[self.cy-r+1][c+self.cx]==2:                            
                            self.before.clear() 
                            return False
        return True
    
    def stackBlock(self):
        bl = self.block.arr[self.block.idx]
        size = self.block.Size  
        color = self.block.color
        
        for r in range(size):            
            for c in range(size):
                if bl[size-1-r][c]:                
                    self.maps[self.cy-r][c+self.cx]=2
                    self.cmaps[self.cy-r][c+self.cx]=color
                    
    def removeBlock(self):        
        # find remove line
        lines = []        
        for r in range(Tetris.Row):
            cnt = 0
            for c in range(Tetris.Col):
                if self.maps[r][c]==2:
                    cnt+=1
                else:
                    break

            if cnt == Tetris.Col:
                lines.append(r)
                
        if lines:            
            # remove line        
            for r in lines:
                for c in range(Tetris.Col):
                    self.maps[r][c] = 0
                
                self.update_signal.emit()
                time.sleep(0.2)               
                
                # fall blocks                
                for rr in range(r-1, -1, -1):
                    for cc in range(Tetris.Col):
                        if self.maps[rr][cc]==2:
                            self.maps[rr+1][cc] = 2
                            self.maps[rr][cc] = 0
                            
                            self.update_signal.emit()
                            time.sleep(0.1)
                time.sleep(0.2)               
                

    def threadFunc(self):
        while self.run:                            
            self.cs.acquire()
            self.cy+=1       
            if not self.blockUpdate():
                self.gameover_signal.emit()
                break
            #self.cy+=1       
            self.cs.release()
            time.sleep(0.5)            
        print('thread finished...')