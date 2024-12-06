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

class Input:
    BASE_DIR = os.path.join(os.path.dirname(__file__), "resources")

    @classmethod
    def read(cls, year:int, day:int) -> list[str]:
        with open(os.path.join(cls.BASE_DIR, f"{year}_{day}.txt")) as f:
            return [line.strip() for line in f.readlines()]
    