class Rope:
    def __init__(self, tail_rope = None):
        self.head_pos = (0, 0)
        self.tail_pos = (0, 0)
        self.tail_posns = {self.tail_pos}
        self.tail_rope = tail_rope

    def adjust_tail(self):
        if self.tail_pos[1] == self.head_pos[1]:
            if self.head_pos[0] - self.tail_pos[0] >= 2:
                # don't want to overlap
                self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1])
            elif self.tail_pos[0] - self.head_pos[0] >= 2:
                # don't want to overlap
                self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1])
        elif self.tail_pos[0] == self.head_pos[0]:
            if self.head_pos[1] - self.tail_pos[1] >= 2:
                # don't want to overlap
                self.tail_pos = (self.tail_pos[0], self.tail_pos[1]+1)
            elif self.tail_pos[1] - self.head_pos[1] >= 2:
                # don't want to overlap
                self.tail_pos = (self.tail_pos[0], self.tail_pos[1]-1)
        else:
            # if they're not touching
            if (
                self.head_pos[0] not in (self.tail_pos[0] - 1, self.tail_pos[0], self.tail_pos[0] + 1)
                or self.head_pos[1] not in (self.tail_pos[1] - 1, self.tail_pos[1], self.tail_pos[1] + 1)
            ):
                if self.head_pos[1] < self.tail_pos[1] and self.head_pos[0] > self.tail_pos[0]:
                    # up and to the right
                    self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]-1)
                elif self.head_pos[1] > self.tail_pos[1] and self.head_pos[0] > self.tail_pos[0]:
                    # down and to the right
                    self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]+1)
                elif self.head_pos[1] < self.tail_pos[1] and self.head_pos[0] < self.tail_pos[0]:
                    # up and to the left
                    self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]-1)
                elif self.head_pos[1] > self.tail_pos[1] and self.head_pos[0] < self.tail_pos[0]:
                    # down and to the left
                    self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]+1)
        self.tail_posns.add(self.tail_pos)
        if self.tail_rope is not None:
            self.tail_rope.head_pos = self.tail_pos
            self.tail_rope.adjust_tail()

    def move_right(self, n):
        for i in range(n):
            self.head_pos = (self.head_pos[0]+1, self.head_pos[1])
            # if self.tail_pos[1] == self.head_pos[1]:
            #     if self.head_pos[0] - self.tail_pos[0] >= 2:
            #         # don't want to overlap
            #         self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1])
            # else:
            #     # if they're not touching
            #     if (
            #         self.head_pos[0] not in (self.tail_pos[0] - 1, self.tail_pos[0], self.tail_pos[0] + 1)
            #         or self.head_pos[1] not in (self.tail_pos[1] - 1, self.tail_pos[1], self.tail_pos[1] + 1)
            #     ):
            #         if self.head_pos[1] < self.tail_pos[1]:
            #             # up and to the right
            #             self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]-1)
            #         elif self.head_pos[1] > self.tail_pos[1]:
            #             # down and to the right
            #             self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]+1)
            #         else:
            #             print("this shouldn't happen")
            # self.tail_posns.add(self.tail_pos)
            self.adjust_tail()

    def move_up(self, n):
        for i in range(n):
            self.head_pos = (self.head_pos[0], self.head_pos[1]-1)
            # if self.tail_pos[0] == self.head_pos[0]:
            #     if self.tail_pos[1] - self.head_pos[1] >= 2:
            #         # don't want to overlap
            #         self.tail_pos = (self.tail_pos[0], self.tail_pos[1]-1)
            # else:
            #     # if they're not touching
            #     if (
            #         self.head_pos[0] not in (self.tail_pos[0] - 1, self.tail_pos[0], self.tail_pos[0] + 1)
            #         or self.head_pos[1] not in (self.tail_pos[1] - 1, self.tail_pos[1], self.tail_pos[1] + 1)
            #     ):
            #         if self.head_pos[0] < self.tail_pos[0]:
            #             # up and to the left
            #             self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]-1)
            #         elif self.head_pos[0] > self.tail_pos[0]:
            #             # up and to the right
            #             self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]-1)
            #         else:
            #             print("this shouldn't happen")
            # self.tail_posns.add(self.tail_pos)
            self.adjust_tail()

    def move_left(self, n):
        for i in range(n):
            self.head_pos = (self.head_pos[0]-1, self.head_pos[1])
            # if self.tail_pos[1] == self.head_pos[1]:
            #     if self.tail_pos[0] - self.head_pos[0] >= 2:
            #         # don't want to overlap
            #         self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1])
            # else:
            #     # if they're not touching
            #     if (
            #         self.head_pos[0] not in (self.tail_pos[0] - 1, self.tail_pos[0], self.tail_pos[0] + 1)
            #         or self.head_pos[1] not in (self.tail_pos[1] - 1, self.tail_pos[1], self.tail_pos[1] + 1)
            #     ):
            #         if self.head_pos[1] < self.tail_pos[1]:
            #             # up and to the left
            #             self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]-1)
            #         elif self.head_pos[1] > self.tail_pos[1]:
            #             # down and to the left
            #             self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]+1)
            #         else:
            #             print("this shouldn't happen")
            # self.tail_posns.add(self.tail_pos)
            self.adjust_tail()

    def move_down(self, n):
        for i in range(n):
            self.head_pos = (self.head_pos[0], self.head_pos[1]+1)
            # if self.tail_pos[0] == self.head_pos[0]:
            #     if self.head_pos[1] - self.tail_pos[1] >= 2:
            #         # don't want to overlap
            #         self.tail_pos = (self.tail_pos[0], self.tail_pos[1]+1)
            # else:
            #     # if they're not touching
            #     if (
            #         self.head_pos[0] not in (self.tail_pos[0] - 1, self.tail_pos[0], self.tail_pos[0] + 1)
            #         or self.head_pos[1] not in (self.tail_pos[1] - 1, self.tail_pos[1], self.tail_pos[1] + 1)
            #     ):
            #         if self.head_pos[0] < self.tail_pos[0]:
            #             # down and to the left
            #             self.tail_pos = (self.tail_pos[0]-1, self.tail_pos[1]+1)
            #         elif self.head_pos[0] > self.tail_pos[0]:
            #             # down and to the right
            #             self.tail_pos = (self.tail_pos[0]+1, self.tail_pos[1]+1)
            #         else:
            #             print("this shouldn't happen")
            # self.tail_posns.add(self.tail_pos)
            self.adjust_tail()


    def __str__(self):
        return "head={}, tail={}".format(self.head_pos, self.tail_pos)



cmds = []

with open("day09.in") as f:
    for line in f:
        a, b = line.strip().split()
        cmds.append((a, int(b)))



rope = Rope()
for cmd, arg in cmds:
    if cmd == "R":
        rope.move_right(arg)
    elif cmd == "U":
        rope.move_up(arg)
    elif cmd == "L":
        rope.move_left(arg)
    elif cmd == "D":
        rope.move_down(arg)

print(len(rope.tail_posns))


# ropes = [Rope() for i in range(9)]
# for cmd, arg in cmds:
#     prev_posns = [r.tail_pos for r in ropes]
#     if cmd == "R":
#         ropes[0].move_right(arg)
#     elif cmd == "U":
#         ropes[0].move_up(arg)
#     elif cmd == "L":
#         ropes[0].move_left(arg)
#     elif cmd == "D":
#         ropes[0].move_down(arg)

#     cur_posns = [r.tail_pos for r in ropes]
#     for index, p in enumerate(cur_posns):
#         if index != 8:
#             if p[0] < prev_posns[index][0]:
#                 ropes[index+1].move_left(prev_posns[index][0] - p[0])
#             if p[0] > prev_posns[index][0]:
#                 ropes[index+1].move_right(p[0] - prev_posns[index][0])
#             if p[1] < prev_posns[index][1]:
#                 ropes[index+1].move_up(prev_posns[index][1] - p[1])
#             if p[1] < prev_posns[index][1]:
#                 ropes[index+1].move_down(p[1] - prev_posns[index][1])


ropes = []
for i in range(9):
    ropes.append(Rope())
    if i != 0:
        ropes[-2].tail_rope = ropes[-1]

for cmd, arg in cmds:
    if cmd == "R":
        ropes[0].move_right(arg)
    elif cmd == "U":
        ropes[0].move_up(arg)
    elif cmd == "L":
        ropes[0].move_left(arg)
    elif cmd == "D":
        ropes[0].move_down(arg)

    # for index, rope in enumerate(ropes[:-1]):
    #     ropes[index + 1].head_pos = rope.tail_pos
    #     ropes[index + 1].adjust_tail()

    # for index, rope in enumerate(ropes):
    #     print(f"Rope {index}: {rope}")


print(len(ropes[8].tail_posns))
