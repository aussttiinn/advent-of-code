import os
import re
import json

from enum import Enum
from abc import ABC, abstractmethod
from typing import Any
from collections import Counter

class Solution(ABC):
    class InputFormat(Enum):
        txt = "txt"
        json = "json"

    def __load_input(self, format:InputFormat):
        file_name = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", f"{self.year}_{self.day}_{self.part}.{format.value}"))
        with open(file_name) as f:
            if format == self.InputFormat.json:
                data = json.loads(f)
            elif format == self.InputFormat.txt:
                data = [s.strip() for s in f.readlines()]
            else:
                self.logger.error(f"Format ``{format}`` is not supported.")
        return data  
            
    def __init__(self, year:int, day:int, part:int, input_format:InputFormat): 
        self.year, self.day, self.part, self.input_format = year, day, part, input_format
        self.input = self.__load_input(input_format)

    @abstractmethod
    def run(self) -> Any:
        pass
        
class Day1Part1(Solution):
    def __init__(self):
        super().__init__(2024, 1, 1, self.InputFormat.txt)

    def run(self):
        left = [int(re.split("\\s+", s)[0]) for s in self.input]
        right = [int(re.split("\\s+", s)[1]) for s in self.input]
        left.sort()
        right.sort()

        return sum([abs(left[i]-right[i]) for i in range(len(left))])
    
class Day1Part2(Solution):
    def __init__(self):
        super().__init__(2024,1,2,self.InputFormat.txt)

    def run(self):
        left = [int(re.split("\\s+", s)[0]) for s in self.input]
        right = [int(re.split("\\s+", s)[1]) for s in self.input]
        return sum([left[i]*right.count(left[i]) for i in range(len(left))])

class Day23Part1(Solution):
    def __init__(self):
        super().__init__(2023,23,1,self.InputFormat.txt)

    class Matrix:
        def __init__(self, array:list[list[str]]):
            self.array = array
        
        def __getitem__(self, item):
            return self.array[item]
        
        def getElement(self, i, j):
            if i<0 or j<0:
                return None
            return self.array[i][j]
        
        def getNeighbors(self, i, j):
            arr = [
                [self.getElement(i-1, j-1), self.getElement(i-1, j), self.getElement(i-1, j+1)],
                [self.getElement(i, j-1), self.getElement(i, j), self.getElement(i, j+1)],
                [self.getElement(i+1, j-1), self.getElement(i+1, j), self.getElement(i+1, j+1)],
            ]
            return Day23Part1.Matrix(arr)        
    
    def run(self):
        pass

class Day2Part1(Solution):
    def __init__(self):
        super().__init__(2024, 2, 1, self.InputFormat.txt)

    def safeRow(self, row:list[int]) -> True:
        """
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
        """
        all_inc_or_dec = sorted(row.copy(), reverse=False) == row or sorted(row.copy(), reverse=True) == row
        for i in range(len(row)-1):
            if not all_inc_or_dec or not (abs(row[i]-row[i+1])>=1 and abs(row[i]-row[i+1])<=3):
                return False
        return True
    
    def run(self): 
        array = [[int(i) for i in re.split("\\s+", s)] for s in self.input]
        return [self.safeRow(row) for row in array].count(True)

if __name__ == "__main__":
    print(Day2Part1().run())



