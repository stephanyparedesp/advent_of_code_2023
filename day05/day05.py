import re

import pandas as pd
from tqdm import tqdm

fn = "data.txt"

data = open(fn).read().split("\n\n")
seeds = [int(a) for a in re.findall("\d+", data[0].split(":")[1])]
cats = {}

# Parse input
for i, block in enumerate(data[1:]):
    ranges_line = block.split("\n")[1:]
    cat_ranges = []
    for r in ranges_line:  # param a , param b, range
        line_range = tuple([int(a) for a in re.findall("\d+", r)])
        cat_ranges.append(line_range)
    cats[i] = cat_ranges


# Find the destination on one map
def find_destination(search_value, category):
    range_list = cats[category]
    search_success = False
    for elem in range_list:
        boundary = elem[1]
        range_bound = elem[2]
        # If the value is within the range
        if search_value in range(boundary, boundary + range_bound):
            counting = search_value - boundary
            end_value = elem[0] + counting
            search_success = True
            break
    # If not mapped, return the same number
    if search_success:
        rval = end_value
    else:
        rval = search_value

    return rval


def look_in_pipeline(seeds):
    minimum = 1e1000
    for seed in seeds:
        soil = find_destination(search_value=seed, category=0)
        fertilizer = find_destination(search_value=soil, category=1)
        water = find_destination(search_value=fertilizer, category=2)
        light = find_destination(search_value=water, category=3)
        temperature = find_destination(search_value=light, category=4)
        humidity = find_destination(search_value=temperature, category=5)
        location = find_destination(search_value=humidity, category=6)
        if location < minimum:
            minimum = location
    return minimum


# Part 1:
print(f"Part 1:\n {look_in_pipeline(seeds)}")

# For part 2
# Break into parts and see where it is smartest to look in

total_seeds = []
for i in range(0, len(seeds), 2):
    se = (seeds[i], seeds[i] + seeds[i + 1])
    total_seeds.append(se)

total_seeds = sorted(total_seeds)

# Find the likely pair where you find the solution
min_loc = 1e1000
likely_pair = 0
for i, pair in enumerate(total_seeds):
    last_loc = look_in_pipeline(pair)
    if last_loc < min_loc:
        min_loc = last_loc + 0
        likely_pair = i + 0

# Now that we narrowed down a range, lets split it into smaller pieces for the search
groups = 10000
lb = total_seeds[likely_pair][0]
ub = total_seeds[likely_pair][1]
new_range_seeds = list(range(lb, ub, int((ub - lb) / groups)))
group_locs = []

for seed in new_range_seeds:
    group_locs.append((seed, look_in_pipeline([seed])))
df = pd.DataFrame(data=group_locs, columns=["Seed", "Location"])

# Choose which group we want to explore
lb_idx = int(df.iloc[df["Location"].idxmin() - 1].Seed)
up_idx = int(df.iloc[df["Location"].idxmin()].Seed)

print(f"Part 2:\n {look_in_pipeline(range(lb_idx,up_idx+1))}")
