import os
import re
import json

from enum import Enum
from abc import ABC, abstractmethod
from typing import Any

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





