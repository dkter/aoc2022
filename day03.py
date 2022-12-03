lines = []

with open("day03.in") as f:
    for line in f:
        lines.append(line.strip())


rucksacks = []
for l in lines:
    halflen = len(l) // 2
    rucksacks.append([l[:halflen], l[halflen:]])


priority_sum = 0
for c1, c2 in rucksacks:
    common = list(set(c1) & set(c2))[0]
    if ord(common) < 97:
        # uppercase
        priority_sum += ord(common) - 64 + 26
    else:
        priority_sum += ord(common) - 96

print(priority_sum)



rucksacks2 = [[]]
for index, l in enumerate(lines):
    if index // 3 >= len(rucksacks2):
        rucksacks2.append(list())
    rucksacks2[-1].append(l)

priority_sum = 0
for c1, c2, c3 in rucksacks2:
    common = list(set(c1) & set(c2) & set(c3))[0]
    if ord(common) < 97:
        # uppercase
        priority_sum += ord(common) - 64 + 26
    else:
        priority_sum += ord(common) - 96

print(priority_sum)

