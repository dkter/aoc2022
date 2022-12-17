from dataclasses import dataclass
from itertools import cycle


with open("day17.in") as f:
    pattern = f.read().strip()


rocks = [
    ["####"],
    [
        ".#.",
        "###",
        ".#.",
    ],
    [
        "..#",
        "..#",
        "###",
    ],
    [
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "##",
        "##",
    ],
]


@dataclass
class FallenRock:
    rock: list[str]
    left_pos: int
    bottom_pos: int

    @property
    def top_pos(self):
        return self.bottom_pos + len(self.rock)

    @property
    def right_pos(self):
        return self.left_pos + len(self.rock[0])


rocknum = 0
rocks_fallen = []
pattern_index = 0
for n_rocks, rock in enumerate(cycle(rocks)):
    if rocks_fallen == []:
        y = 3
    else:
        if len(rocks_fallen) > 7:
            # only need to check the last 7 things that fell to find
            # the uppermost y position
            y = max([r.top_pos for r in rocks_fallen[-7:]]) + 3
        else:
            y = max([r.top_pos for r in rocks_fallen]) + 3
    x = 2

    while True:
        ch = pattern[pattern_index]
        # print(ch)
        if ch == ">":
            if x + len(rock[0]) != 7:
                found_right_collision = False
                for fallen_rock in reversed(rocks_fallen):
                    # check rightward collision
                    # can probably exit from this early if we've checked all 7 x positions
                    if (
                        fallen_rock.top_pos >= y + 1
                        and fallen_rock.bottom_pos <= y + len(rock)
                        and fallen_rock.right_pos >= x
                        and fallen_rock.left_pos <= x + len(rock[0]) - 1
                    ):
                        for rock_y, row in enumerate(fallen_rock.rock):
                            for rock_x, cell in enumerate(row):
                                absolute_fallen_y = fallen_rock.top_pos - rock_y
                                absolute_fallen_x = fallen_rock.left_pos + rock_x
                                rel_y_to_right = absolute_fallen_y - y - 1
                                rel_x_to_right = absolute_fallen_x - x - 1
                                if rel_x_to_right > len(rock[0]) - 1:
                                    break
                                if rel_x_to_right < 0:
                                    continue
                                if rel_y_to_right < 0:
                                    break
                                if rel_y_to_right > len(rock) - 1:
                                    continue
                                if (
                                    cell == "#"
                                    and rock[-rel_y_to_right - 1][rel_x_to_right] == "#"
                                ):
                                    found_right_collision = True
                                    break
                            if found_right_collision:
                                break
                    if found_right_collision:
                        break
                if not found_right_collision:
                    x += 1
        elif ch == "<":
            if x != 0:
                found_left_collision = False
                for fallen_rock in reversed(rocks_fallen):
                    # check leftward collision
                    # can probably exit from this early if we've checked all 7 x positions
                    if (
                        fallen_rock.top_pos >= y + 1
                        and fallen_rock.bottom_pos <= y + len(rock)
                        and fallen_rock.right_pos >= x
                        and fallen_rock.left_pos <= x + len(rock[0]) - 1
                    ):
                        for rock_y, row in enumerate(fallen_rock.rock):
                            for rock_x, cell in enumerate(row):
                                absolute_fallen_y = fallen_rock.top_pos - rock_y
                                absolute_fallen_x = fallen_rock.left_pos + rock_x
                                rel_y_to_left = absolute_fallen_y - y - 1
                                rel_x_to_left = absolute_fallen_x - x + 1
                                if rel_x_to_left > len(rock[0]) - 1:
                                    break
                                if rel_x_to_left < 0:
                                    continue
                                if rel_y_to_left < 0:
                                    break
                                if rel_y_to_left > len(rock) - 1:
                                    continue

                                #breakpoint()
                                if (
                                    cell == "#"
                                    and rock[-rel_y_to_left - 1][rel_x_to_left] == "#"
                                ):
                                    found_left_collision = True
                                    break
                            if found_left_collision:
                                break
                    if found_left_collision:
                        break
                if not found_left_collision:
                    x -= 1

        pattern_index += 1
        if pattern_index >= len(pattern):
            pattern_index = 0
        # print(y)

        if y == 0:
            rocks_fallen.append(FallenRock(rock, x, y))
            break
        else:
            found_collision = False
            for fallen_rock in reversed(rocks_fallen):
                # check collision
                # can probably exit from this early if we've checked all 7 x positions
                if fallen_rock.top_pos >= y:
                    pass
                    # print(x, fallen_rock.left_pos, fallen_rock.right_pos)
                if (
                    fallen_rock.top_pos >= y
                    and fallen_rock.bottom_pos <= y + len(rock)
                    and fallen_rock.right_pos >= x
                    and fallen_rock.left_pos <= x + len(rock[0])
                ):
                    for rock_y, row in enumerate(fallen_rock.rock):
                        for rock_x, cell in enumerate(row):
                            absolute_fallen_y = fallen_rock.top_pos - rock_y
                            absolute_fallen_x = fallen_rock.left_pos + rock_x
                            rel_y_above = absolute_fallen_y - y
                            rel_x_above = absolute_fallen_x - x
                            if rel_x_above > len(rock[0]) - 1:
                                break
                            if rel_x_above < 0:
                                continue
                            if rel_y_above < 0:
                                break
                            if rel_y_above > len(rock) - 1:
                                continue
                            # if len(rocks_fallen) == 2:
                            #     breakpoint()
                            if (
                                cell == "#"
                                and rock[-rel_y_above - 1][rel_x_above] == "#"
                            ):
                                # block can stop
                                found_collision = True
                                break
                        if found_collision:
                            break
                if found_collision:
                    break
            if found_collision:
                rocks_fallen.append(FallenRock(rock, x, y))
                break
            else:
                y -= 1


    if len(rocks_fallen) == 2022:
        break

    # print(rocks_fallen)


max_top = 0
for rock in rocks_fallen:
    if rock.top_pos > max_top:
        max_top = rock.top_pos

print(max_top)
