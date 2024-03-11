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
        self.arr = [ [False, False, False, False] for _ in range(Block.Size) ]        
        
    def print(self):
        for r in range(Block.Size):
            for c in range(Block.Size):
                if self.arr[r][c]:
                    print('■', end='')
                else:
                    print('□', end='')
            print()

class BO(Block):    
    def __init__(self):
        super().__init__(BType.O)
        for r in range(1, 3):
            for c in range(1, 3):
                self.arr[r][c] = True

class BI(Block):    
    def __init__(self):
        super().__init__(BType.I)
        for c in range(Block.Size):            
            self.arr[1][c] = True
            
class BS(Block):    
    def __init__(self):
        super().__init__(BType.S)        
        self.arr[1][2] = True
        self.arr[1][3] = True
        self.arr[2][1] = True
        self.arr[2][2] = True
        
class BZ(Block):    
    def __init__(self):
        super().__init__(BType.Z)        
        self.arr[2][2] = True
        self.arr[2][3] = True
        self.arr[1][1] = True
        self.arr[1][2] = True
        
class BL(Block):    
    def __init__(self):
        super().__init__(BType.L)        
        self.arr[1][1] = True
        self.arr[1][2] = True
        self.arr[1][3] = True
        self.arr[2][1] = True
        
class BJ(Block):    
    def __init__(self):
        super().__init__(BType.J)        
        self.arr[1][1] = True
        self.arr[1][2] = True
        self.arr[1][3] = True
        self.arr[2][3] = True
        
class BT(Block):    
    def __init__(self):
        super().__init__(BType.T)        
        self.arr[1][1] = True
        self.arr[1][2] = True
        self.arr[1][3] = True
        self.arr[2][2] = True
