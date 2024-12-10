import os 

class Directions:
    NORTH = (-1, 0)         # Up
    SOUTH = (1, 0)         # Down
    EAST = (0, 1)          # Right
    WEST = (0, -1)         # Left
    NORTHEAST = (-1, 1)    # Diagonal up-right
    NORTHWEST = (-1, -1)   # Diagonal up-left
    SOUTHEAST = (1, 1)     # Diagonal down-right
    SOUTHWEST = (1, -1)    # Diagonal down-left
    
    ALL = [NORTH, SOUTH, EAST, WEST, NORTHEAST, 
                NORTHWEST, SOUTHEAST, SOUTHWEST]
    
    NO_DIAGONAL = [NORTH, SOUTH, EAST, WEST]

class Input:
    BASE_DIR = os.path.join(os.path.dirname(__file__), "resources")

    @classmethod
    def read(cls, year:int, day:int, test_data:bool=False) -> list[str]:
        path = f"{year}_{day}_test.txt" if test_data else f"{year}_{day}.txt"
        with open(os.path.join(cls.BASE_DIR, path)) as f:
            return [line.strip() for line in f.readlines()]

class Matrix:
    def _isRectangular(self, arr:list[list]):
        if not all(len(arr[i])==len(arr) for i in arr):
            raise Exception("Only rectangular matrices allowed.")

    def __init__(self, arr:list[list]):
        self.arr=arr
        self.size=(len(arr),len(arr[0]))
    
    def _inBounds(self, i, j) -> bool:
        return (0<=i<self.size[0]) and (0<=j<self.size[1])

    def getElement(self, i, j, default=None): 
        if self._inBounds(i, j):
            return self.arr[i][j]
        return default

    def getAdjacent(self, i, j, directions:list) -> list: 
        if not self._inBounds(i, j):
            return []
        
        adj = []        
        for d in directions: 
            row, col = i+d[0], j+d[1]
            if self._inBounds(row, col):
                adj.append((row, col))
        return adj

    def prettyPrint(self):
        for row in self.arr:
            print(" ".join(f"{element:4}" for element in row)) 