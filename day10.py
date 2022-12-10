from pprint import pprint

instrs = []

with open("day10.in") as f:
    for line in f:
        params = line.strip().split()
        if len(params) == 2:
            a, b = params
        else:
            b = 0
            a = params[0]
        instrs.append((a, int(b)))



strengths = []
cycle_number = 1
x = 1
for instr, arg in instrs:
    if (cycle_number - 20) % 40 == 0:
        strengths.append(x * cycle_number)
    if instr == "noop":
        cycle_number += 1
    elif instr == "addx":
        cycle_number += 1
        if (cycle_number - 20) % 40 == 0:   
            strengths.append(x * cycle_number)
        cycle_number += 1
        x += arg

print(sum(strengths))


strengths = []
cycle_number = 0
x = 1
row_number = 0
rows = []
for instr, arg in instrs:
    xpos = cycle_number % 40
    if xpos == 0:
        rows.append([])
    if xpos in (x-1, x, x+1):
        rows[-1].append("#")
    else:
        rows[-1].append(".")
    
    if instr == "noop":
        cycle_number += 1
    elif instr == "addx":
        cycle_number += 1
        xpos = cycle_number % 40
        if xpos == 0:
            rows.append([])
        if xpos in (x-1, x, x+1):
            rows[-1].append("#")
        else:
            rows[-1].append(".")
        cycle_number += 1
        x += arg

for row in rows:
    print(''.join(row))
