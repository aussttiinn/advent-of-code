from model import Matrix, Input, Directions
from enum import Enum

input = Input.read(2024, 6, test_data=False)

class GuardPositions(Enum):
    """The GuardPositions is facing..."""
    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "v" 

    ANY = [LEFT, RIGHT, UP, DOWN]

    @classmethod
    def fromItem(cls, item):
        if item == cls.LEFT.value:
            return cls.LEFT
        if item == cls.RIGHT.value:
            return cls.RIGHT
        if item == cls.UP.value:
            return cls.UP
        if item == cls.DOWN.value:
            return cls.DOWN
        raise ValueError(f"Not a valid guard position. {item}")
    
    @classmethod
    def fromDirection(cls, dir: Directions):
        if dir == Directions.WEST:
            return cls.LEFT
        if dir == Directions.EAST: 
            return cls.RIGHT
        if dir == Directions.NORTH: 
            return cls.UP
        if dir == Directions.SOUTH:
            return cls.DOWN
        raise ValueError(f"Not a valid guard position ``{dir.name}``")
    
    def toDirection(self):
        if self == GuardPositions.LEFT:
            return Directions.WEST
        if self == GuardPositions.RIGHT:
            return Directions.EAST
        if self == GuardPositions.UP:
            return Directions.NORTH
        if self == GuardPositions.DOWN:
            return Directions.SOUTH
        
    def rotateDirection(self):
        """Rotate clockwise (right turn)."""
        d = self.toDirection()
        if d == Directions.NORTH:
            return Directions.EAST
        if d == Directions.EAST:
            return Directions.SOUTH
        if d == Directions.SOUTH:
            return Directions.WEST
        if d == Directions.WEST:
            return Directions.NORTH

class Lab(Matrix):
    def findGuardPositions(self, positions: list[GuardPositions] = GuardPositions.ANY) -> tuple:
        """Finds the FIRST occurrence of an item, starting top-to-bottom, left-to-right."""
        i, j = self.size
        for idx in range(i):
            for jdx in range(j):
                e = self.getElement(idx, jdx)
                if e in positions.value:
                    return (GuardPositions.fromItem(e), (idx, jdx))
        return None, (-1, -1)

class Guard: 
    def __init__(self, lab: Lab):
        self.lab = lab
        x, y = lab.findGuardPositions(GuardPositions.ANY)
        self.start_guardpos: GuardPositions = x
        self.start_loc = y
        self.curr_loc = self.start_loc
        self.curr_pos: GuardPositions = self.start_guardpos

    def move(self, d: Directions, states:set=set()) -> bool:
        i, j = self.curr_loc
        adj = self.lab.getAdjacent(i, j, [d])
        if adj:
            new_i, new_j = adj[0]
            x = ((new_i, new_j), GuardPositions.fromDirection(d))
            if x in states:
                return False, states
            if self.lab.getElement(new_i, new_j) in ["#", "O"]:
                return self.move(self.curr_pos.rotateDirection(), states=states)
            
            states.add(x)
            self.curr_loc = (new_i, new_j)
            self.curr_pos = GuardPositions.fromDirection(d)
            self.lab.arr[i][j], self.lab.arr[new_i][new_j] = self.lab.arr[new_i][new_j], self.lab.arr[i][j]
            self.lab.arr[new_i][new_j] = self.curr_pos.value
            return True, states
        return False, states

    def walk(self):
        """Loop over moves, performing patrols."""
        visited = set()
        visited.add(self.curr_loc) 
        while True:
            d = self.curr_pos.toDirection()
            keepGoing, states = self.move(d)
            visited.add(self.curr_loc)
            # print(f"Moved to {self.curr_loc}, facing {self.curr_pos.name}")
            if not keepGoing:
                break
        return visited, states

def part1():
    l = Lab([list(line) for line in input])
    g = Guard(l)

    visited, _ = g.walk()
    return len(visited)

def part2():
    

    return "not implemented"

if __name__ == "__main__": 
    print("Part1: ", part1())
    print("Part2: ", part2())

