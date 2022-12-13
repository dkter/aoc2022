from itertools import zip_longest
from functools import cmp_to_key

pairs = [[]]

with open("day13.in") as f:
    for line in f:
        if line.strip():
            pairs[-1].append(eval(line.strip()))
        else:
            pairs.append([])



def compare(packet1, packet2):
    for item1, item2 in zip_longest(packet1, packet2):
        if item2 is None:
            return False
        elif item1 is None:
            return True
        elif isinstance(item1, list) and isinstance(item2, list):
            result = compare(item1, item2)
            if result is not None:
                if not result:
                    return False
                elif result:
                    return True
        elif isinstance(item1, list):
            result = compare(item1, [item2])
            if result is not None:
                if not result:
                    return False
                elif result:
                    return True
        elif isinstance(item2, list):
            result = compare([item1], item2)
            if result is not None:
                if not result:
                    return False
                elif result:
                    return True
        else:
            if item1 > item2:
                return False
            elif item1 < item2:
                return True
    return None


index_sum = 0
for index, (packet1, packet2) in enumerate(pairs):
    if compare(packet1, packet2):
        index_sum += index + 1

print(index_sum)


packets = [x[0] for x in pairs] + [x[1] for x in pairs]
packets.append([[2]])
packets.append([[6]])

@cmp_to_key
def key(packet1, packet2):
    result = compare(packet1, packet2)
    if result is None:
        return 0
    elif not result:
        return 1
    else:
        return -1

packets.sort(key=key)



dividers = (
    (packets.index([[2]]) + 1)
    * (packets.index([[6]]) + 1)
)

print(dividers)
