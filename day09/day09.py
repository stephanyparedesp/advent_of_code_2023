import numpy as np

fn = "data.txt"
lines = open(fn).read().split("\n")


def get_diffs(oasis, reversed=False):
    diff_series = [oasis]
    diff = np.diff(oasis)
    while sum(diff) != 0:
        diff_series.append(diff)
        diff = np.diff(diff)
    if reversed:
        diff_series.reverse()
    return diff_series


# Part 1
adds = 0
for line in lines:
    oasis = [int(a) for a in line.split()]
    sum_e = 0
    for e in get_diffs(oasis):
        sum_e += e[-1]
    adds += sum_e
print(adds)
# Part 2
adds = 0
for line in lines:
    oasis = [int(a) for a in line.split()]
    vals = [0]
    for e in get_diffs(oasis, reversed=True):
        val = e[0] - vals[-1]
        vals.append(val)
    adds += vals[-1]
print(adds)
