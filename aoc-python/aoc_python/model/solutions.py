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
                # data = f.read()
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

    def safeRow(self, row:list[int]) -> bool:
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
    
class Day2Part2(Solution):
    def __init__(self):
        super().__init__(2024, 2, 2, self.InputFormat.txt)

    def safeRow(self, row:list[int]) -> bool:
        """
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
        """
        all_inc_or_dec = sorted(row.copy(), reverse=False) == row or sorted(row.copy(), reverse=True) == row
        for i in range(len(row)-1):
            if not all_inc_or_dec or not (abs(row[i]-row[i+1])>=1 and abs(row[i]-row[i+1])<=3):
                return False
        return True
    
    def safeRowOneRemoved(self, row:list[int]) -> bool:
        """A row is safe if removing any given element is safe."""
        for i in range(len(row)):
            i_removed = row[:i]+row[i+1:]
            if self.safeRow(i_removed):
                return True
        return False

    def run(self): 
        array = [[int(i) for i in re.split("\\s+", s)] for s in self.input]
        return [self.safeRowOneRemoved(row) for row in array].count(True)

class Day1Part2_2023(Solution):
    def __init__(self):
        super().__init__(2023, 1, 2, self.InputFormat.txt)

    def extract(self, line:str) -> list:
        def word_to_int(word:str) -> int:
            valid = {
                "one": 1, 
                "two": 2, 
                "three": 3, 
                "four": 4, 
                "five": 5, 
                "six": 6, 
                "seven": 7, 
                "eight": 8, 
                "nine": 9, 
                "zero": 0
            }
            return valid.get(word)
        
        def get_all_substrings(string:str, length:int) -> list[str]:
            substrings = []
            for j in range(len(string)-length):
                for i in range(len(string)-length):
                    sub = string[i:i+length]
                    substrings.append(sub)
            return substrings
         
        def get_all_substrings_v2(string:str, min_length: int, max_length:int):
            substrings = []
            for i in range(min_length, max_length):
                substrings.extend(get_all_substrings(string, i))
            return substrings

        substrings:list[str] = get_all_substrings_v2(line, 3, 8)
        for s in substrings:
            if s.isalpha():
                print(s)

    def run(self):
        self.extract(self.input[0])

import re 
class Day3Part1(Solution):
    def __init__(self):
        super().__init__(2024, 3, 1, self.InputFormat.txt)
    
    def get_nums(self, match:str) -> tuple[int, int]:
        return (
            int(match.lower().split(",")[0].replace("mul(","").replace(")","")),
            int(match.lower().split(",")[-1].replace("mul(","").replace(")",""))
        )

    def run(self):
        pattern = r"(mul\([0-9]*,[0-9]*\))"
        matches:list[str] = re.findall(pattern, self.input)
        nums = [self.get_nums(s) for s in matches]
        
        result = 0 
        for pair in nums:
            result += pair[0]*pair[1]
        print(result)
        return result
    
class Day3Part2(Solution):
    def __init__(self):
        super().__init__(2024, 3, 2, self.InputFormat.txt)
    
    def run(self):
        def get_nums(match:str) -> tuple[int, int]:
            return (
                int(match.lower().split(",")[0].replace("mul(","").replace(")","")),
                int(match.lower().split(",")[-1].replace("mul(","").replace(")",""))
            )

        complete_pattern = r"(mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\))"
        mul_pattern = r"(mul\([0-9]*,[0-9]*\))"
        matches:list[str] = re.findall(complete_pattern, self.input)

        sdf = []
        applyNext=True
        for i in range(len(matches)):
            if re.search(mul_pattern, matches[i]) and applyNext:
                sdf.append(matches[i])
            if matches[i].lower() == "don't()":
                applyNext=False
            elif matches[i].lower() == "do()":
                applyNext=True
        
        sdf = [get_nums(s) for s in sdf]
        result = 0 
        for i in sdf:
            result += i[0]*i[1]
        print(result)
        return result
    
class Day4Part1(Solution):
    class Matrix:
        def __init__(self, arr:list[list], parent=None, parent_loc=None):
            self.arr:list[list] = arr
            self.parent:Day4Part1.Matrix = parent
            self.parent_loc:tuple=parent_loc
        
        def getElement(self, i, j):
            if i<0 or j<0:
                return None
            return self.arr[i][j]

        def __str__(self):
            return str(self.arr)
        
        def getNeighbors(self, i, j):
            arr = [
                [self.getElement(i-1, j-1), self.getElement(i-1, j), self.getElement(i-1, j+1)],
                [self.getElement(i, j-1), self.getElement(i, j), self.getElement(i, j+1)],
                [self.getElement(i+1, j-1), self.getElement(i+1, j), self.getElement(i+1, j+1)],
            ]
            return Day4Part1.Matrix(arr, parent=self, parent_loc=(i, j))

    def __init__(self):
        super().__init__(2024, 4, 1, self.InputFormat.txt)
    
    def run(self):
        arr = [list(s) for s in self.input]
        m = self.Matrix(arr)
        print(str(m.getNeighbors(0,0)))

if __name__ == "__main__":
    Day4Part1().run()



