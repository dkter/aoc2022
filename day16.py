from collections import deque
from itertools import product
import random

flow_rates = {}
tunnels = {}

with open("day16.in") as f:
    for line in f:
        words = line.split()
        flow_rates[words[1]] = int(words[4][5:-1])
        tunnels[words[1]] = []
        for tunnel in words[9:]:
            if tunnel[-1] == ",":
                tunnels[words[1]].append(tunnel[:-1])
            else:
                tunnels[words[1]].append(tunnel)

print(flow_rates)
print(tunnels)


def shortest_paths(start):
    # copy from day 12 lol
    shortest_paths = {}
    calculated_shortest_paths = set()
    for tunnel in tunnels:
        shortest_paths[tunnel] = -1
    shortest_paths[start] = 0

    while len(calculated_shortest_paths) != len(tunnels):
        # pick shortest distance
        closest_tunnel = None
        shortest_distance = -1
        for tunnel, distance in shortest_paths.items():
            if tunnel is None or distance == -1 or tunnel in calculated_shortest_paths:
                continue
            if shortest_distance == -1 or distance < shortest_distance:
                shortest_distance = distance
                closest_tunnel = tunnel

        if closest_tunnel == None:
            raise ValueError()

        calculated_shortest_paths.add(closest_tunnel)
        for connected_tunnels in tunnels[closest_tunnel]:
            if shortest_paths[connected_tunnels] == -1 or shortest_distance + 1 < shortest_paths[connected_tunnels]:
                shortest_paths[connected_tunnels] = shortest_distance + 1
    return shortest_paths

# we can just calculate everything and throw away the function lol
shortest_paths = {tunnel: shortest_paths(tunnel) for tunnel in tunnels}
shortest_paths_minus_zeros = {tunnel: {k: v for k, v in shortest_paths[tunnel].items() if flow_rates[k] > 0} for tunnel in tunnels}
n_nonzero = len(shortest_paths_minus_zeros["AA"])


valve = "AA"


# when you open a valve, you get (flow rate) * (30 - current_minute)

# gonna start by calculating the best i can do by opening One valve. see where that gets me


def get_best(starting_tunnel, current_minute):
    best = {}
    for tunnel, distance in shortest_paths[starting_tunnel].items():
        best[tunnel] = (30 - distance - current_minute) * flow_rates[tunnel]
    return best

print(get_best("AA", 1))


# well now that I know how to do that, I can't think of anything better than just a search


def part1():
    best_path = None
    best_pressure = 0
    queue = deque([(("AA",), 0, 0, (0,))])
    paths_visited = set()

    best_at_minute_and_place = {}

    while queue:
        path, current_minute, pressure, timestamps = queue.pop()
        paths_visited.add(path)

        if (
            (current_minute, path[-1]) in best_at_minute_and_place
            and best_at_minute_and_place[(current_minute, path[-1])] > pressure
        ):
            continue

        # best = get_best(path[-1], current_minute)
        for next_tunnel_candidate, distance_candidate in shortest_paths[path[-1]].items():
            if next_tunnel_candidate not in path:
                new_minute = current_minute + distance_candidate + 1
                if new_minute > 30:
                    if pressure > best_pressure:
                        best_pressure = pressure
                        best_path = path
                    # go back and update best_at_minute_and_place
                    historic_pressure = pressure
                    for tunnel, timestamp in zip(reversed(path), reversed(timestamps)):
                        key = timestamp, tunnel
                        if (
                            key not in best_at_minute_and_place or
                            best_at_minute_and_place[key] < historic_pressure
                        ):
                            best_at_minute_and_place[key] = historic_pressure
                        #historic_pressure -= (30 - timestamp) * flow_rates[tunnel]


                    continue
                new_pressure = pressure + (30 - new_minute) * flow_rates[next_tunnel_candidate]
                new_path = path + (next_tunnel_candidate,)
                new_timestamps = timestamps + (new_minute,)
                if new_path not in paths_visited and new_pressure > 0:
                    queue.append((new_path, new_minute, new_pressure, new_timestamps))

    print(best_path, best_pressure)
    # print(best_at_minute_and_place)


def part2_old():
    # best_path = None
    # best_pressure = 0
    paths = {}
    queue = deque([(("AA",), 0, 0, (0,))])
    paths_visited = set()

    best_at_minute_and_place = {}

    while queue:
        path, current_minute, pressure, timestamps = queue.pop()
        paths_visited.add(path)

        if (
            (current_minute, path[-1]) in best_at_minute_and_place
            and best_at_minute_and_place[(current_minute, path[-1])] > pressure
        ):
            continue

        # best = get_best(path[-1], current_minute)
        for next_tunnel_candidate, distance_candidate in shortest_paths[path[-1]].items():
            if next_tunnel_candidate not in path:
                new_minute = current_minute + distance_candidate + 1
                if new_minute > 30:
                    # if pressure > best_pressure:
                    #     best_pressure = pressure
                    #     best_path = path
                    paths[path] = pressure
                    # go back and update best_at_minute_and_place
                    historic_pressure = pressure
                    for tunnel, timestamp in zip(reversed(path), reversed(timestamps)):
                        key = timestamp, tunnel
                        if (
                            key not in best_at_minute_and_place or
                            best_at_minute_and_place[key] < historic_pressure
                        ):
                            best_at_minute_and_place[key] = historic_pressure
                        #historic_pressure -= (30 - timestamp) * flow_rates[tunnel]


                    continue
                new_pressure = pressure + (30 - new_minute) * flow_rates[next_tunnel_candidate]
                new_path = path + (next_tunnel_candidate,)
                new_timestamps = timestamps + (new_minute,)
                if new_path not in paths_visited and new_pressure > 0:
                    queue.append((new_path, new_minute, new_pressure, new_timestamps))

    print(paths)


    # try to find the max 2 with none in common
    # actually this wouldn't work probably :(
    # could try it anyway since it would be easy (?)


    max_combined = 0
    for (path1, pressure1), (path2, pressure2) in product(paths.items(), repeat=2):
        if len(set(path1[1:]) & set(path2[1:])) == 0:
            if pressure1 + pressure2 > max_combined:
                max_combined = pressure1 + pressure2
    print(max_combined)

    # this definitely does not work
    # I think I need to keep track of elephant positions in the regular search

    # print(best_at_minute_and_place)



def part2():
    # best_path = None
    best_pressure = 0
    paths = {}
    queue = deque([(("AA",), ("AA",), 0, 0, 0, (0,), (0,))])
    paths_visited = set()
    elephant_paths_visited = set()

    best_at_minute_and_place = {}
    elephant_best_at_minute_and_place = {}

    while queue:
        path, elephant_path, current_minute, elephant_minute, pressure, timestamps, elephant_timestamps = queue.pop()

        paths_visited.add(path)

        # you_key = (current_minute, path[-1])
        # elephant_key = (elephant_minute, elephant_path[-1])
        # if (
        #     you_key in best_at_minute_and_place
        #     and best_at_minute_and_place[you_key] > pressure
        #     and elephant_key in best_at_minute_and_place
        #     and best_at_minute_and_place[elephant_key] > pressure
        # ):
        #     continue

        # # go back and update best_at_minute_and_place
        # historic_pressure = pressure
        # for tunnel, timestamp in zip(reversed(path), reversed(timestamps)):
        #     key = timestamp, tunnel
        #     if (
        #         key not in best_at_minute_and_place or
        #         best_at_minute_and_place[key] < historic_pressure
        #     ):
        #         best_at_minute_and_place[key] = historic_pressure
        #     #historic_pressure -= (26 - timestamp) * flow_rates[tunnel]
        # historic_pressure = pressure
        # for tunnel, timestamp in zip(reversed(elephant_path), reversed(elephant_timestamps)):
        #     key = timestamp, tunnel
        #     if (
        #         key not in best_at_minute_and_place or
        #         best_at_minute_and_place[key] < historic_pressure
        #     ):
        #         best_at_minute_and_place[key] = historic_pressure
        #     #historic_pressure -= (26 - timestamp) * flow_rates[tunnel]


        if pressure > best_pressure:
            best_pressure = pressure
            print(best_pressure, path, elephant_path)


        # best = get_best(path[-1], current_minute)
        for next_tunnel_candidate, distance_candidate in (list(shortest_paths_minus_zeros[path[-1]].items())):
            if next_tunnel_candidate not in path and next_tunnel_candidate not in elephant_path:
                for elephant_tunnel, elephant_distance in (list(shortest_paths_minus_zeros[elephant_path[-1]].items())):
                    if elephant_tunnel != next_tunnel_candidate and elephant_tunnel not in path and elephant_tunnel not in elephant_path:
                        new_minute = current_minute + distance_candidate + 1
                        new_elephant_minute = elephant_minute + elephant_distance + 1
                        if new_minute > 26 and new_elephant_minute > 26:
                            if pressure > best_pressure:
                                best_pressure = pressure
                            #     best_path = path
                            paths[path] = pressure
                            


                            continue
                        if new_minute <= 26:
                            you_pressure = (26 - new_minute) * flow_rates[next_tunnel_candidate]
                            new_path = path + (next_tunnel_candidate,)
                            new_timestamps = timestamps + (new_minute,)
                        else:
                            you_pressure = 0
                            new_path = path
                            new_timestamps = timestamps
                        if new_elephant_minute <= 26:
                            elephant_pressure = (26 - new_elephant_minute) * flow_rates[elephant_tunnel]
                            new_elephant_path = elephant_path + (elephant_tunnel,)
                            new_elephant_timestamps = elephant_timestamps + (new_elephant_minute,)
                        else:
                            elephant_pressure = 0
                            new_elephant_path = elephant_path
                            new_elephant_timestamps = elephant_timestamps
                        new_pressure = pressure + you_pressure + elephant_pressure
                        #print(new_pressure)
                        if new_pressure > pressure:
                            queue.appendleft((new_path, new_elephant_path, new_minute, new_elephant_minute, new_pressure, new_timestamps, new_elephant_timestamps))

    #print(paths)
    print(best_pressure)


part2()
