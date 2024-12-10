from model import Input
from enum import Enum
import itertools

input = Input.read(2024, 7, test_data=False)

def transform_input(input:list[str]) -> dict[int, list[int]]:
    return {int(x.split(":")[0]): [int(i) for i in x.split(":")[-1].split(" ") if i != ""] for x in input}


class CalibrationEquation:
    ADD = "+"
    MULT = "*"

    def __init__(self, result:int, inputs:list[int]):
        self.result = result
        self.inputs = inputs

    def performOperation(self, operations: list[str]) -> int:
        result = self.inputs[0]
        for i in range(1, len(self.inputs)):
            op = operations[i-1] 
            if op == self.ADD:
                result += self.inputs[i]
            elif op == self.MULT:
                result *= self.inputs[i]
        return result

    def checkOperations(self, operations:list[tuple[str]]) -> bool:
        while operations: 
            op = operations.pop()
            if self.result == self.performOperation(op):
                return True
        return False

def part1(): 
    characters = ["+", "*"]
    transformed = transform_input(input)

    test_value_sum = 0
    for key, value in transformed.items():
        ce = CalibrationEquation(result=key, inputs=value)
        operations = list(itertools.product(characters, repeat=len(value)-1))
        test_value_sum += key if ce.checkOperations(operations) else 0
    return test_value_sum
        
if __name__ == "__main__": 
    print(f"Part1: ", part1())
