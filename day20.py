from collections import deque
from copy import copy

number_list = []

with open("day20.in") as f:
    for line in f:
        number_list.append(int(line))

numbers = deque(number_list)


indices = deque(range(len(numbers)))
for i in range(len(numbers)):
    item = numbers.popleft()
    #print(item)
    index = indices.popleft()
    numbers.rotate(-item)
    indices.rotate(-item)
    numbers.appendleft(item)
    indices.appendleft(index)
    #print(numbers)
    #print(indices)
    # next index is i + 1
    # find index in indices, then rotate numbers by that much
    try:
        next_index = indices.index(i + 1)
        #print(next_index)
        numbers.rotate(-next_index)
        indices.rotate(-next_index)
    except ValueError:
        break


zero_index = numbers.index(0)
numbers.rotate(-zero_index)
#print(numbers)
numbers.rotate( - 1000)
a = numbers[0]
numbers.rotate(-1000)
b = numbers[0]
numbers.rotate(-1000)
c = numbers[0]

print(a, b, c)
print(a + b + c)



numbers2 = deque([i*811589153 for i in number_list])
indices2 = deque(range(len(numbers2)))

for _ in range(10):
    for i in range(len(numbers2)):
        next_index = indices2.index(i)
        numbers2.rotate(-next_index)
        indices2.rotate(-next_index)

        item = numbers2.popleft()
        index = indices2.popleft()
        numbers2.rotate(-item)
        indices2.rotate(-item)
        numbers2.appendleft(item)
        indices2.appendleft(index)


zero_index = numbers2.index(0)
numbers2.rotate(-zero_index)
numbers2.rotate( - 1000)
a = numbers2[0]
numbers2.rotate(-1000)
b = numbers2[0]
numbers2.rotate(-1000)
c = numbers2[0]

print(a, b, c)
print(a + b + c)
