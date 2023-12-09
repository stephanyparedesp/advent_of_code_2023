import numpy as np

fn = "data.txt"
lines = open(fn).read().split("\n")
# Part 1
adds = 0
for line in lines:
    oasis = [int(a) for a in line.split()]
    diff_series = [oasis]
    diff = np.diff(oasis)
    while sum(diff) != 0:
        diff_series.append(diff)
        diff = np.diff(diff)
    # Now we have a list of differences
    sum_e = 0
    for e in diff_series:
        sum_e += e[-1]
    adds += sum_e

print(adds)
# Part 2
adds = 0
for line in lines:
    oasis = [int(a) for a in line.split()]
    diff_series = [oasis]
    diff = np.diff(oasis)
    while sum(diff) != 0:
        diff_series.append(diff)
        diff = np.diff(diff)
    # Now we have a list of differences
    vals = [0]
    diff_series.reverse()
    for e in diff_series:
        val = e[0] - vals[-1]
        vals.append(val)
    adds += vals[-1]

print(adds)
