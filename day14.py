import itertools

paths = []

with open("day14.in") as f:
    for line in f:
        paths.append([(int(a), int(b)) for a, b in [j.split(",") for j in line.split(" -> ")]])


def is_rock(x, y):
    for path in paths:
        for (x1, y1), (x2, y2) in itertools.pairwise(path):
            if (
                (x1 <= x <= x2 or x2 <= x <= x1)
                and (y1 <= y <= y2 or y2 <= y <= y1)
            ):
                return True
    return False


# it's gonna be faster to just make a set
rock = set()
for path in paths:
    for (x1, y1), (x2, y2) in itertools.pairwise(path):
        max_x = max(x1, x2)
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        if x1 == x2:
            for y in range(min_y, max_y + 1):
                rock.add((x1, y))
        elif y1 == y2:
            for x in range(min_x, max_x + 1):
                rock.add((x, y1))

sand = set()
sand_start = (500, 0)

lowest_rock_y = 0
for path in paths:
    for x1, y1 in path:
        if y1 > lowest_rock_y:
            lowest_rock_y = y1



def next_sand_pos():
    x, y = sand_start
    resting = False
    while not resting:
        y_below = y + 1
        if (x, y_below) in sand or (x, y_below) in rock: #is_rock(x, y_below):
            if (x-1, y_below) in sand or (x-1, y_below) in rock: #is_rock(x-1, y_below):
                if (x+1, y_below) in sand or (x+1, y_below) in rock: #is_rock(x+1, y_below):
                    resting = True
                else:
                    x += 1
                    y += 1
            else:
                x -= 1
                y += 1
        else:
            y += 1
        if y > lowest_rock_y:
            return x, y
    return x, y


while True:
    pos = next_sand_pos()
    if pos[1] > lowest_rock_y:
        break
    sand.add(pos)



print(len(sand))

lowest_rock_y += 2

def next_sand_pos2():
    x, y = sand_start
    resting = False
    while not resting:
        y_below = y + 1
        if y_below == lowest_rock_y or (x, y_below) in sand or (x, y_below) in rock:
            if y_below == lowest_rock_y or (x-1, y_below) in sand or (x-1, y_below) in rock:
                if y_below == lowest_rock_y or (x+1, y_below) in sand or (x+1, y_below) in rock:
                    resting = True
                else:
                    x += 1
                    y += 1
            else:
                x -= 1
                y += 1
        else:
            y += 1
        if y == 0:
            return x, y
    return x, y

while True:
    pos = next_sand_pos2()
    if pos[1] == 0:
        break
    sand.add(pos)

print(len(sand) + 1)
