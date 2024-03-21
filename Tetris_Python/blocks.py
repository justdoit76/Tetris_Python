from abc import ABC, abstractmethod
from enum import Enum

class BType(Enum):
    O = 0
    I = 1
    S = 2
    Z = 3
    L = 4
    J = 5
    T = 6

class Block(ABC):
    
    Size = 4
        
    @abstractmethod
    def __init__(self, type):
        super().__init__()        
        self.type = type
        self.arr = []
        self.idx = 0        
    
    def rotate_r(self):
        size = len(self.arr)
        
        if self.idx>=size-1:
            self.idx = 0
        else:
            self.idx += 1        
    
    def rotate_l(self):
        size = len(self.arr)
        
        if self.idx<=0:
            self.idx = size-1
        else:
            self.idx -= 1     

    def findTail(self):
        block = self.arr[self.idx]
        U = self.findUpperTail(block)
        D = self.findLowerTail(block)
        L = self.findLeftTail(block)
        R = self.findRightTail(block)
        
        return U, D, L, R
        
    def findUpperTail(self, block):        
        for r in range(Block.Size):
            for c in range(Block.Size):                            
                if block[r][c]:
                    return r
                
    def findLowerTail(self, block):        
        for r in range(Block.Size-1, -1, -1):
            for c in range(Block.Size):                            
                if block[r][c]:
                    return r
                
    def findLeftTail(self, block):        
        for c in range(Block.Size):
            for r in range(Block.Size):                            
                if block[r][c]:
                    return c
                
    def findRightTail(self, block):        
        for c in range(Block.Size-1, -1, -1):
            for r in range(Block.Size):                            
                if block[r][c]:
                    return c
        
    def print(self):        
        print('-'*Block.Size)            
        for r in range(Block.Size):
            for c in range(Block.Size):
                if self.arr[self.idx][r][c]:
                    print('■', end='')
                else:
                    print('□', end='')
            print()
        print('-'*Block.Size)

class BO(Block):    
    def __init__(self):
        super().__init__(BType.O)
        self.color = (255,255,0,255)
        # 0
        temp = [ [False, False, False, False] for _ in range(Block.Size) ]
        for r in range(1, 3):
            for c in range(1, 3):
                temp[r][c] = True
        self.arr.append(temp)

class BI(Block):    
    def __init__(self):
        super().__init__(BType.I)
        self.color = (115,251,253,255)
        # 0
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        for c in range(Block.Size):            
            temp[1][c] = True
        self.arr.append(temp)
        
        # 1
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]
        for r in range(Block.Size):
            temp[r][2] = True
        self.arr.append(temp)            
            
class BS(Block):    
    def __init__(self):
        super().__init__(BType.S)    
        self.color = (0,255,0,255)
        # 0
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]
        temp[1][2] = True
        temp[1][3] = True
        temp[2][1] = True
        temp[2][2] = True
        self.arr.append(temp)
        
        # 1
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]
        temp[0][2] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][3] = True
        self.arr.append(temp)
        
class BZ(Block):    
    def __init__(self):
        super().__init__(BType.Z)     
        self.color = (0,255,0,255)
        # 0
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]
        temp[2][2] = True
        temp[2][3] = True
        temp[1][1] = True
        temp[1][2] = True
        self.arr.append(temp)
        
        # 1
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]
        temp[0][3] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][2] = True
        self.arr.append(temp)       
        
class BL(Block):    
    def __init__(self):        
        super().__init__(BType.L)        
        self.color = (255,168,76,255)
        # 0        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][1] = True
        self.arr.append(temp)
        
        # 1        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[1][2] = True
        temp[2][2] = True
        temp[2][3] = True
        self.arr.append(temp)
        
        # 2        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][3] = True
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        self.arr.append(temp)
        
        # 4        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][1] = True
        temp[0][2] = True
        temp[1][2] = True
        temp[2][2] = True
        self.arr.append(temp)
        
class BJ(Block):    
    def __init__(self):
        super().__init__(BType.J)
        self.color = (0,0,255,255)
        # 0        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][3] = True
        self.arr.append(temp)
        
        # 1        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[0][3] = True
        temp[1][2] = True
        temp[2][2] = True
        self.arr.append(temp)
        
        # 2        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][1] = True
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        self.arr.append(temp)
        
        # 4        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[1][2] = True
        temp[2][1] = True
        temp[2][2] = True
        self.arr.append(temp)
        
class BT(Block):    
    def __init__(self):
        super().__init__(BType.T)
        self.color = (255,0,255,255)
        # 0        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][2] = True
        self.arr.append(temp)
        
        # 1        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[1][2] = True
        temp[1][3] = True
        temp[2][2] = True
        self.arr.append(temp)
        
        # 2        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[1][1] = True
        temp[1][2] = True
        temp[1][3] = True
        self.arr.append(temp)
        
        # 4        
        temp =  [ [False, False, False, False] for _ in range(Block.Size) ]        
        temp[0][2] = True
        temp[1][1] = True
        temp[1][2] = True
        temp[2][2] = True
        self.arr.append(temp)      