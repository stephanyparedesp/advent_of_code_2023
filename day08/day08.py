import numpy as np
from cycler import cycle

fn = "data.txt"
file = open(fn).read()

ins = file.split("\n\n")[0]
dirs = file.split("\n\n")[1].split("\n")

pos = {"R": 1, "L": 0}

coor = {}
for line in dirs:
    c = line.split(" =")[0]
    x, y = line.split(" = ")[1].split(",")
    x = x[1:].strip()
    y = y[:-1].strip()
    coor.update({c: (x, y)})

start = "AAA"
dest = "ZZZ"
steps = 1

# Part 1
for i in cycle(ins):
    nexts = coor[start]
    end = nexts[pos[i]]
    if end == dest:
        break
    start = end
    steps += 1

print(steps)

# Part 2
start = [a for a in coor.keys() if a.endswith("A")]
all_steps = []
for n in start:
    steps = 1
    for i in cycle(ins):
        # print(n)
        nexts = coor[n]
        end = nexts[pos[i]]
        # print(end)
        if end.endswith("Z"):
            break
        n = end
        steps += 1

    all_steps.append(steps)

print(np.lcm.reduce(all_steps))
