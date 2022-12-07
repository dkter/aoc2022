from pathlib import Path
from collections import deque

cmds = []

with open("day7.in") as f:
    for line in f:
        if line[0] == '$':
            cmds.append([line.strip()[2:], []])
        else:
            cmds[-1][1].append(line.strip())


dirs = {}
structure = {}
cwd = Path("/")
for cmd, output in cmds:
    if cmd.startswith("cd"):
        arg = cmd.split()[1]
        if arg == "..":
            cwd = cwd.parent
        elif arg == "/":
            cwd = Path("/")
        else:
            cwd = cwd / arg

    else:
        dirs[cwd] = []
        structure[cwd] = []
        for line in output:
            str_size, name = line.split()
            if str_size != "dir":
                size = int(str_size)
                structure[cwd].append(size)
            else:
                dirs[cwd].append(cwd/Path(name))



total_sizes = {}
queue = deque([Path("/")])
visited = set()
while queue:
    dir = queue.pop()
    done = True
    for subdir in dirs[dir]:
        if subdir not in total_sizes:
            if subdir not in queue:
                queue.appendleft(subdir)
            done = False
    if done:
        total_sizes[dir] = 0
        # add up the bytes
        for filesize in structure[dir]:
            total_sizes[dir] += filesize
        for subdir in dirs[dir]:
            total_sizes[dir] += total_sizes[subdir]
        visited.add(dir)
    else:
        queue.appendleft(dir)



p1 = 0
for k, v in total_sizes.items():
    if v < 100000:
        p1 += v
print(p1)


used_space = total_sizes[Path("/")]
space_needed = 30000000 - (70000000 - used_space)
sizes = sorted(total_sizes.values())

for s in sizes:
    if s > space_needed:
        print(s)
        break