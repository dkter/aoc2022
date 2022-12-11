from dataclasses import dataclass
from typing import Optional
from itertools import cycle, repeat
from operator import itemgetter


class CoolNumber:
    def __init__(self, value: int):
        self.value = value
        self.remainders = {}

    def __iadd__(self, x):
        #self.value += x
        for num in self.remainders:
            self.remainders[num] += x
            while self.remainders[num] >= num:
                self.remainders[num] -= num
        return self
           

    def __imul__(self, x):
        if x == self:
            #self.value *= self.value
            for num in self.remainders:
                self.remainders[num] = (self.remainders[num] ** 2) % num
        else:
            #self.value *= x
            for num in self.remainders:
                if num == x:
                    self.remainders[num] = 0
                else:
                    self.remainders[num] *= (x % num)
                    self.remainders[num] %= num

        return self


    def __eq__(self, other):
        return isinstance(other, CoolNumber)# and self.value == other.value


    def __mod__(self, x):
        if x in self.remainders:
            # if self.remainders[x] != self.value % x:
            #     print("BAD BAD BAD")
            #     print(self.value, x, self.remainders, self.value % x)
            return self.remainders[x]
        else:
            self.remainders[x] = self.value % x
            return self.remainders[x]

    def __repr__(self):
        return repr(self.value)


class Operation:
    def __init__(self, string):
        self.lhs, self.rhs = string.split(" = ")
        symbols = self.rhs.split()
        self.optype = symbols[1]
        self.a = symbols[0]
        self.b = symbols[2]

    def eval(self, old):
        #return eval(self.rhs, {"old": old})
        if self.a == "old" and self.b == "old" and self.optype == "*":
            old *= old
            return old
        elif self.a == "old" and self.optype == "+":
            old += int(self.b)
            return old
        elif self.a == "old" and self.optype == "*":
            old *= int(self.b)
            return old
        else:
            raise ValueError("unknown operator type")


class Monkey:
    items: list[int]
    operation: Operation

    def __init__(self):
        self.inspections = 0
        self.item_divisibilities = []

    def __repr__(self):
        #return f"{self.items} -> {self.inspections}"
        return repr(self.inspections)

    def eval_and_test(self, index):
        #return eval(self.rhs, {"old": old})
        old = self.items[index]
        if self.a == "old" and self.b == "old" and self.optype == "*":
            ret = old
        elif self.a == "old" and self.optype == "+":
            ret = old + int(self.b)
        elif self.a == "old" and self.optype == "*":
            ret = old * int(self.b)
        else:
            raise ValueError("unknown operator type")


monkeys = []

with open("day11.in") as f:
    for line in f:
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        else:
            if "Starting" in line:
                monkeys[-1].items = [int(i) for i in line.split(":")[-1].split(", ")]
            elif "Operation" in line:
                monkeys[-1].operation = Operation(line.strip().split(": ")[-1])
            elif "Test" in line:
                monkeys[-1].test_div = int(line.split("by ")[-1])
            elif "If true" in line:
                monkeys[-1].iftrue = int(line.split("monkey ")[-1])
            elif "If false" in line:
                monkeys[-1].iffalse = int(line.split("monkey ")[-1])



i = 0
for monkey in cycle(monkeys):
    new_items = []
    for item in monkey.items:
        new_item = monkey.operation.eval(item)
        new_item //= 3
        if new_item % monkey.test_div == 0:
            monkeys[monkey.iftrue].items.append(new_item)
        else:
            monkeys[monkey.iffalse].items.append(new_item)
        monkey.inspections += 1
    monkey.items = []

    i += 1
    if i == 20 * len(monkeys):
        break


prod = 1
for monkey in list(sorted(monkeys, key=lambda m: m.inspections))[-2:]:
    prod *= monkey.inspections

print(prod)


monkeys = []

with open("day11.in") as f:
    for line in f:
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        else:
            if "Starting" in line:
                monkeys[-1].items = [CoolNumber(int(i)) for i in line.split(":")[-1].split(", ")]
            elif "Operation" in line:
                monkeys[-1].operation = Operation(line.strip().split(": ")[-1])
            elif "Test" in line:
                monkeys[-1].test_div = int(line.split("by ")[-1])
            elif "If true" in line:
                monkeys[-1].iftrue = int(line.split("monkey ")[-1])
            elif "If false" in line:
                monkeys[-1].iffalse = int(line.split("monkey ")[-1])


# this is set up really badly. need to do this to initialize the table
for monkey in monkeys:
    for monkey2 in monkeys:
        for item in monkey.items:
            item % monkey2.test_div


i = 0
for monkey in cycle(monkeys):
    new_items = []
    for item in monkey.items:
        new_item = monkey.operation.eval(item)
        if new_item % monkey.test_div == 0:
            monkeys[monkey.iftrue].items.append(new_item)
        else:
            monkeys[monkey.iffalse].items.append(new_item)
        monkey.inspections += 1
    monkey.items = []

    i += 1
    #print(monkeys)
    if i == 10000 * len(monkeys):
        break


print(monkeys)
prod = 1
for monkey in list(sorted(monkeys, key=lambda m: m.inspections))[-2:]:
    prod *= monkey.inspections

print(prod)
