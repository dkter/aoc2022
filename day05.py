from itertools import count
from copy import deepcopy

stacks = []
instrs = []
max_stacks = 0

with open("day05.in") as f:
    for line in f:
        if not line.strip():
            break
        if '[' in line:
            for i, c in zip(range(1, len(line), 4), count()):
                if c >= len(stacks):
                    stacks.append(list())
                if line[i].strip():
                    stacks[c].append(line[i])
        max_stacks += 1
    max_stacks -= 1

    for i in range(len(stacks)):
        stacks[i].reverse()

    for line in f:
        space_sep = line.split()
        instrs.append([int(space_sep[1]), int(space_sep[3]), int(space_sep[5])])


stacks1 = deepcopy(stacks)
for q, src, dest in instrs:
    for i in range(q):
        stacks1[dest-1].append(stacks1[src-1].pop())



for s in stacks1:
    print(s[-1], end="")
print()


for q, src, dest in instrs:
    lst = []
    for i in range(q):
        lst.append(stacks[src-1].pop())
    lst.reverse()
    stacks[dest-1].extend(lst)


for s in stacks:
    print(s[-1], end="")
print()
