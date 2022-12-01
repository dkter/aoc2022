elves = [[]]

with open("day01.in") as f:
    for line in f:
        if line == '\n':
            elves.append(list())
        else:
            elves[-1].append(int(line.strip()))

print(max(sum(e) for e in elves))

top = sorted([sum(e) for e in elves])[::-1]
print(top[0] + top[1] + top[2])
