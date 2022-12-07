print(
    ''.join([
        a[-1] for a in
        list(__import__("itertools").accumulate(
            __import__("itertools").zip_longest(
                [
                    [int(line.split()[1]), int(line.split()[3]), int(line.split()[5])]
                    for line in open("day05.in")
                    if "move" in line
                ],
                [],
                fillvalue=[
                    list(reversed([letter for letter in lst if letter != ' ']))
                    for lst in list(__import__("itertools").accumulate(
                        [
                            [line[i] for i in range(1, len(line), 4)]
                            for line in open("day05.in")
                            if "[" in line
                        ],
                        lambda lst1, lst2: [
                            (lst1[i] + [lst2[i]] if i < len(lst1) else [lst2[i]])
                            for i in range(len(lst2))
                        ],
                        initial=[]
                    ))[-1]
                ],
            ),
            lambda oldstate, newstate: [
                (0, 0, 0),
                [
                    (
                        (
                            item
                            if index != newstate[0][1] - 1 else
                            item[:-newstate[0][0]]
                        )
                        if index != newstate[0][2] - 1 else
                        item + oldstate[1][newstate[0][1]-1][-newstate[0][0]:]
                    )
                    for index, item in enumerate(oldstate[1])
                ]
            ] if oldstate != [] else [
                (0, 0, 0),
                [
                    (
                        (
                            item
                            if index != newstate[0][1] - 1 else
                            item[:-newstate[0][0]]
                        )
                        if index != newstate[0][2] - 1 else
                        item + newstate[1][newstate[0][1]-1][-newstate[0][0]:]
                    )
                    for index, item in enumerate(newstate[1])
                ]
            ],
            initial=[]
        ))[-1][1]
    ])
)