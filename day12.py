grid = []

with open("day12.in") as f:
    for y, line in enumerate(f):
        row = []
        for x, ch in enumerate(line.strip()):
            if ch == "S":
                row.append(0)
                startpos = (x, y)
            elif ch == "E":
                row.append(26)
                endpos = (x, y)
            else:
                row.append(ord(ch) - 97)
        grid.append(row)


max_y = len(grid) - 1
max_x = len(grid[0]) - 1


def surrounding(x, y):
    if x != 0:
        # if y != 0:
        #     yield (x-1, y-1)
        yield (x-1, y)
        # if y != max_y:
        #     yield (x-1, y+1)

    if y != 0:
        yield (x, y-1)
    if y != max_y:
        yield (x, y+1)

    if x != max_x:
        # if y != 0:
        #     yield (x+1, y-1)
        yield (x+1, y)
        # if y != max_y:
        #     yield (x+1, y+1)


# ok make it a graph
graph = {}
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if (x, y) not in graph:
            graph[(x, y)] = list()
        for (x2, y2) in surrounding(x, y):
            if grid[y2][x2] != -1 and grid[y2][x2] - cell <= 1:
                graph[(x, y)].append((x2, y2))
graph[endpos] = []

# dijkstra?
shortest_paths = {}
calculated_shortest_paths = set()
for coords in graph:
    shortest_paths[coords] = -1
shortest_paths[startpos] = 0

while len(calculated_shortest_paths) != (max_x + 1) * (max_y + 1):
    # pick shortest distance
    shortest_coords = None
    shortest_distance = -1
    for coords, distance in shortest_paths.items():
        if coords is None or distance == -1 or coords in calculated_shortest_paths:
            continue
        if shortest_distance == -1 or distance < shortest_distance:
            shortest_distance = distance
            shortest_coords = coords

    if shortest_coords == None:
        raise ValueError()

    calculated_shortest_paths.add(shortest_coords)
    for adjacent_coords in graph[shortest_coords]:
        if shortest_paths[adjacent_coords] == -1 or shortest_distance + 1 < shortest_paths[adjacent_coords]:
            shortest_paths[adjacent_coords] = shortest_distance + 1



print(shortest_paths[endpos])


# pt2
shortest_paths = {}
calculated_shortest_paths = set()
for coords in graph:
    shortest_paths[coords] = -1
shortest_paths[startpos] = 0

while len(calculated_shortest_paths) != (max_x + 1) * (max_y + 1):
    # pick shortest distance
    shortest_coords = None
    shortest_distance = -1
    for coords, distance in shortest_paths.items():
        if coords is None or distance == -1 or coords in calculated_shortest_paths:
            continue
        if shortest_distance == -1 or distance < shortest_distance:
            shortest_distance = distance
            shortest_coords = coords

    if shortest_coords == None:
        raise ValueError()

    calculated_shortest_paths.add(shortest_coords)
    for adjacent_coords in graph[shortest_coords]:
        if grid[adjacent_coords[1]][adjacent_coords[0]] == 0 and grid[shortest_coords[1]][shortest_coords[0]] == 0:
            shortest_paths[adjacent_coords] = 0
        elif shortest_paths[adjacent_coords] == -1 or shortest_distance + 1 < shortest_paths[adjacent_coords]:
            shortest_paths[adjacent_coords] = shortest_distance + 1

print(shortest_paths[endpos])
