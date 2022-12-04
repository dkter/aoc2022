lines = []

with open("day04.in") as f:
    for line in f:
        stripped = line.strip()
        pair1, pair2 = stripped.split(",")
        a, b = (int(i) for i in pair1.split("-"))
        c, d = (int(i) for i in pair2.split("-"))
        lines.append(((a, b), (c, d)))


matches = 0
for (a, b), (c, d) in lines:
    if (
        (a <= c and b >= d)
        or (a >= c and b <= d)
    ):
        matches += 1

print(matches)




matches = 0
for (a, b), (c, d) in lines:
    if (
        (a <= c <= b)
        or (a <= d <= b)
        or (c <= a <= d)
        or (c <= b <= d)
    ):
        matches += 1

print(matches)
