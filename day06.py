lines = []

with open("day06.in") as f:
    buffer = f.readline().strip()


for i in range(3, len(buffer)):
    if len({
        buffer[i], buffer[i - 1], buffer[i - 2], buffer[i - 3],
    }) == 4:
        print(i + 1)
        break

for i in range(13, len(buffer)):
    if len({buffer[j] for j in range(i-14, i)}) == 14:
        print(i)
        break
