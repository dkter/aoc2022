from itertools import combinations
from collections import deque

cubes = []

with open("day18.in") as f:
    for line in f:
        cubes.append(tuple(int(i) for i in line.strip().split(",")))

cubeset = set(cubes)


def adjacent(x1, y1, z1, x2, y2, z2):
    return (
        (x1 == x2 and y1 == y2 and abs(z1 - z2) == 1)
        or (x1 == x2 and z1 == z2 and abs(y1 - y2) == 1)
        or (z1 == z2 and y1 == y2 and abs(x1 - x2) == 1)
    )


def adjacent_sides(x1, y1, z1):
    yield from (
        (x1+1, y1, z1),
        (x1-1, y1, z1),
        (x1, y1+1, z1),
        (x1, y1-1, z1),
        (x1, y1, z1+1),
        (x1, y1, z1-1),
    )


n_sides = 6 * len(cubes)
for (x1, y1, z1), (x2, y2, z2) in combinations(cubes, 2):
    if adjacent(x1, y1, z1, x2, y2, z2):
        n_sides -= 2

print(n_sides)


# for group in combinations(cubes, 6):
#     for side in adjacent_sides(*group[0]):
#         if side not in cubeset and all(adjacent(*side, *cube) for cube in group[1:]):
#             n_sides -= 6
# lol there are 94,497,365,599,073,647 of these


cubes_surrounding_pockets = set()
pocket_spaces = set()
for cube in cubes:
    for side in adjacent_sides(*cube):
        if side not in cubeset and side not in pocket_spaces:
            queue = deque([side])
            cubes_surrounding = []
            spaces = {side}
            found_pocket = True
            while queue:
                c = queue.pop()
                if (
                    c[0] > 20 or c[1] > 20 or c[2] > 20
                    or c[0] < 0 or c[1] < 0 or c[2] < 0
                ):
                    found_pocket = False
                    break
                for adj in adjacent_sides(*c):
                    if adj in cubeset:
                        cubes_surrounding.append(adj)
                    else:
                        if adj not in spaces:
                            spaces.add(adj)
                            queue.append(adj)
            if found_pocket:
                pocket_spaces |= spaces
                n_sides -= len(cubes_surrounding)


print(n_sides)
