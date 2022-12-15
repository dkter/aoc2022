import time

sensors = []
beacons = []

with open("day15.in") as f:
    for line in f:
        words = line.split(" ")
        x1, y1, x2, y2 = words[2], words[3], words[-2], words[-1]
        x1, y1, x2, y2 = (int(i[2:-1]) for i in (x1, y1, x2, y2))
        sensors.append((x1, y1))
        beacons.append((x2, y2))



row_y = 10
row_x_positions = set()
for (sx, sy), (bx, by) in zip(sensors, beacons):
    max_distance = abs(by - sy) + abs(bx - sx)
    max_x = max_distance - abs(row_y - sy)
    for x2 in range(sx - max_x, sx + max_x + 1):
        if x2 != bx or row_y != by:
            row_x_positions.add(x2)


print(len(row_x_positions))


search_space_max = 4_000_000
# possible_coords = set()
# for y in range(0, search_space_max + 1):
#     for x in range(0, search_space_max + 1):
#         possible_coords.add((x, y))

# for (sx, sy), (bx, by) in zip(sensors, beacons):
#     # local_possible_coords = set()
#     max_distance = abs(by - sy) + abs(bx - sx)
#     # max_x = max_distance - abs(search_space_max - sy)
#     # for x2 in range(sx - max_x, sx + max_x + 1):
#     #     if x2 != bx or search_space_max != by:
#     #         row_x_positions.add(x2)

#     # search x, y from 0 to search_space_max, within the diamond
#     min_x = max(0, sx - max_distance)
#     max_x = min(search_space_max, sx + max_distance)
#     min_y = max(0, sy - max_distance)
#     max_y = min(search_space_max, sy + max_distance)

    

#     for y in range(min_y, max_y + 1):
#         for x in range(
#             max(0, sx - abs(max_distance - abs(sy - y))),
#             min(search_space_max, sx + abs(max_distance - abs(y - sy))) + 1,
#         ):
#             # ok this is gonna be too slow
#             if (x, y) in possible_coords:
#                 possible_coords.remove((x, y))

#     #print(local_possible_coords, sx, sy, bx, by)
#     # if possible_coords is None:
#     #     possible_coords = local_possible_coords
#     # else:
#     #     possible_coords &= local_possible_coords

#     # we are looking for intersections of rectangles
#     # might be easier to turn this 45 degrees


# print(len(possible_coords))
# print(possible_coords)

# calculate as much as possible beforehand
nums = []
for (sx, sy), (bx, by) in zip(sensors, beacons):
    max_distance = abs(by - sy) + abs(bx - sx)
    min_y = max(0, sy - max_distance)
    max_y = min(search_space_max, sy + max_distance)
    nums.append((max_distance, min_y, max_y))


for y in range(0, search_space_max + 1):
    #for x in range(0, search_space_max + 1):
    #start_time = time.time_ns()
    x_set = (1 << search_space_max) - 1
    for (sx, sy), (max_distance, min_y, max_y) in zip(sensors, nums):
        # max_distance = abs(by - sy) + abs(bx - sx)
        # min_y = max(0, sy - max_distance)
        # max_y = min(search_space_max, sy + max_distance)
        if y < min_y or y > max_y:
            continue
        # for y2 in range(min_y, max_y + 1):
        min_x = max(0, sx - abs(max_distance - abs(sy - y)))
        max_x = min(search_space_max, sx + abs(max_distance - abs(y - sy)))
        # if min_x <= x <= max_x:
        #     break
        x_range = ((1 << (max_x - min_x + 1)) - 1) << min_x
        x_set &= ~x_range
    # else:
    #     print(x, y)
    if x_set:
        for x in range(0, search_space_max + 1):
            if not (x_set & ~(1<<x)):

                print(x, y)
                print(x * 4_000_000 + y)
                break
    #end_time = time.time_ns()
    #print("Last loop took {} ns".format(end_time - start_time))

