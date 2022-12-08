lines = []

with open("day08.in") as f:
    for line in f:
        lines.append([int(i) for i in line.strip()])



visible = 0
for y, row in enumerate(lines):
    for x, tree in enumerate(row):
        left = right = top = bottom = True
        # look left
        for y2 in range(0, y):
            if lines[y2][x] >= tree:
                top = False
                break
        for y2 in range(y+1, len(lines[0])):
            if lines[y2][x] >= tree:
                bottom = False
                break
        for x2 in range(0, x):
            if lines[y][x2] >= tree:
                left = False
                break
        for x2 in range(x+1, len(lines)):
            if lines[y][x2] >= tree:
                right = False
                break
        if left or right or top or bottom:
            visible += 1


print(visible)



scenic_score = 0
for y, row in enumerate(lines):
    for x, tree in enumerate(row):
        score = 0
        left = right = top = bottom = 0
        # look left
        for y2 in range(y-1, -1, -1):
            top += 1
            if lines[y2][x] >= tree:
                break
        for y2 in range(y+1, len(lines[0])):
            bottom += 1
            if lines[y2][x] >= tree:
                break
        for x2 in range(x-1, -1, -1):
            left += 1
            if lines[y][x2] >= tree:
                break
        for x2 in range(x+1, len(lines)):
            right += 1
            if lines[y][x2] >= tree:
                break
        score = left * right * top * bottom
        if score > scenic_score:
            scenic_score = score

print(scenic_score)

