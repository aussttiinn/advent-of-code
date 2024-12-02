import os
import re
import json
import math
from enum import Enum
import logging
from abc import ABC, abstractmethod
from typing import Any

class Solution(ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    class InputFormat(Enum):
        txt = "txt"
        json = "json"

    def __load_input(self, format:InputFormat=InputFormat.txt):
        file_name = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", f"{self.year}_{self.day}_{self.part}.{format.value}"))
        with open(file_name) as f:
            if format == self.InputFormat.json:
                data = json.loads(f)
            elif format == self.InputFormat.txt:
                data = [s.strip() for s in f.readlines()]
            else:
                self.logger.error(f"Format ``{format}`` is not supported.")
        return data  
            
    def __init__(self, year:int, day:int, part:int): 
        self.year, self.day, self.part = year, day, part
        self.input = self.__load_input(format=Solution.InputFormat.txt)

    @abstractmethod
    def run(self) -> Any:
        pass
        
class Day1Part1(Solution):
    def __init__(self):
        super().__init__(2024, 1, 1)

    def run(self):
        left = [int(re.split("\\s+", s)[0]) for s in self.input]
        right = [int(re.split("\\s+", s)[1]) for s in self.input]
        left.sort()
        right.sort()

        return sum([abs(left[i]-right[i]) for i in range(len(left))])
    
class Day1Part2(Solution):
    def __init__(self):
        super().__init__(2024,1,2)

    def countOccurences(self, arr:list, obj:Any) -> int:
        """Count the number of a occurences of a given object inside a list"""
        occurences = 0
        for o in arr:
            if o == obj:
                occurences += 1
        return occurences 
    
    def run(self):
        left = [int(re.split("\\s+", s)[0]) for s in self.input]
        right = [int(re.split("\\s+", s)[1]) for s in self.input]

        similarity = 0 
        for o in left:
            similarity += o*self.countOccurences(right, o)
        return similarity





