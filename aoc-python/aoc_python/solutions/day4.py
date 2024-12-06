from aoc_python.model import Input

input = Input.read(2024, 4)

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
    
    @classmethod
    def fromCoord(cls, i, j):
        direction_map = {
            cls.NORTH: "NORTH",
            cls.SOUTH: "SOUTH",
            cls.EAST: "EAST",
            cls.WEST: "WEST",
            cls.NORTHEAST: "NORTHEAST",
            cls.NORTHWEST: "NORTHWEST",
            cls.SOUTHEAST: "SOUTHEAST",
            cls.SOUTHWEST: "SOUTHWEST"
        }
        return direction_map.get((i, j), "UNKNOWN DIRECTION")
    
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
            row, col = i+self.size[0], j+self.size[1]
            if self._inBounds(row, col):
                adj.append((row, col))
        return adj

    def getValidPath(self, start: tuple, direction: tuple, prev: str = None, path: list = None):
        if prev is None:
            prev = f"{self.getElement(*start)}"
        if path is None:
            path = [start]

        words = ['xmas', 'samx']
        i, j = start[0] + direction[0], start[1] + direction[1]

        if prev.lower() in words:
            return path
        elif not self._inBounds(i, j):
            return []
        elif not any([x.startswith(prev.lower()) for x in words]):
            return []
        elif len(prev) >= 4:
            return []

        prev += f"{self.getElement(i, j)}"
        path = path + [(i,j)]
        return self.getValidPath((i, j), direction, prev, path)

    def prettyPrint(self):
        for row in self.arr:
            print(" ".join(f"{element:4}" for element in row))

def part1(): 
    m = Matrix([list(line) for line in input])
    m.prettyPrint()
    count = 0
    paths = [] 
    for i in range(m.size[0]):
        for j in range(m.size[1]):
            for direction in Directions.ALL:
                path = m.getValidPath((i,j), direction)
                paths.append(path)
                
                copy = path.copy()
                copy.reverse()
                if copy not in paths:
                    count+=1
    print(count)

def part2():
    m = Matrix([list(line) for line in input])

    
if __name__ == "__main__": 
    part1()
