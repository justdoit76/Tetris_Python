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
        
        
        
    
    def rotate_l(self):
        pass        
        
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
        # 0
        temp = [ [False, False, False, False] for _ in range(Block.Size) ]
        for r in range(1, 3):
            for c in range(1, 3):
                temp = True
        self.arr.append(temp)

class BI(Block):    
    def __init__(self):
        super().__init__(BType.I)
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