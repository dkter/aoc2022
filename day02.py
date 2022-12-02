guide = []

with open("day02.in") as f:
    for line in f:
        p1, p2 = line.strip().split()
        guide.append((p1, p2))


score = 0
for p1, p2 in guide:
    round_score = 0
    if (
        (p1 == 'A' and p2 == 'Y')
        or (p1 == 'B' and p2 == 'Z')
        or (p1 == 'C' and p2 == 'X')
    ):
        round_score += 6
    elif (
        (p1 == 'A' and p2 == 'X')
        or (p1 == 'B' and p2 == 'Y')
        or (p1 == 'C' and p2 == 'Z')
    ):
        round_score += 3
    if p2 == 'X':
        round_score += 1
    if p2 == 'Y':
        round_score += 2
    if p2 == 'Z':
        round_score += 3
    score += round_score

print(score)


score = 0
for p1, p2 in guide:
    round_score = 0
    if p2 == 'X':
        # lose
        if p1 == 'A':
            round_score += 3
        if p1 == 'B':
            round_score += 1
        if p1 == 'C':
            round_score += 2
    elif p2 == 'Y':
        # draw
        if p1 == 'A':
            round_score += 1
        if p1 == 'B':
            round_score += 2
        if p1 == 'C':
            round_score += 3
        round_score += 3
    elif p2 == 'Z':
        # win
        if p1 == 'A':
            round_score += 2
        if p1 == 'B':
            round_score += 3
        if p1 == 'C':
            round_score += 1
        round_score += 6
    score += round_score

print(score)
