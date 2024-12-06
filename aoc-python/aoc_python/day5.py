from model import Input
from abc import ABC, abstractmethod

input = Input.read(2024, 5)

def transform_input(input:list) -> tuple[list[tuple], list[list]]:
    first = [(int(x.split("|")[0]),int(x.split("|")[1])) for x in input if '|' in x]
    second = [list(map(int, x.split(','))) for x in input if '|' not in x and x != '']
    return first, second

class Page:
    def __init__(self, number:int):
        self.number=number

    def isBefore(self, num:int, within:list, default:bool=True) -> bool:
        try:
            return within.index(self.number) <= within.index(num)
        except ValueError as e:
            return default

class ManualUpdate:
    def __init__(self, update: list):
        self.update = update
    
    def getMiddleNumbers(self):
        if len(self.update) == 0:
            return None
        elif len(self.update) == 1:
            return self.update[0]
        else:
            return self.update[len(self.update)//2]

    def validate(self, rules=list[tuple]):
        for rule in rules:
            first, second = rule
            if not Page(first).isBefore(second, within=self.update):
                return False
        return True

    def enforceOrder(self, rules=list[tuple]):
        for i in range(len(rules)):
            rule = rules[i]
            first, second = rule
            if not Page(first).isBefore(second, within=self.update):
                i, j = self.update.index(first), self.update.index(second)
                self.update[i], self.update[j] = self.update[j], self.update[i]

        

def part1():
    rules, updates = transform_input(input)
    sum = 0     
    for update in updates:
        mu = ManualUpdate(update)
        if mu.validate(rules):
            sum += mu.getMiddleNumbers()
    return sum

def part2():
    rules, updates = transform_input(input)
    sum = 0     
    for update in updates:
        mu = ManualUpdate(update)
        if not mu.validate(rules=rules):
            mu.enforceOrder(rules)
            sum += mu.getMiddleNumbers()
    return sum


if __name__ == "__main__": 
    print(part2())

    