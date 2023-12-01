import copy
import os
import re
from pathlib import Path

pathfile = "data_2.txt"
with open(os.getcwd() + "/" + pathfile) as fp:
    lines = fp.read().split("\n")
part1 = False


if part1:
    data = 0
    # Part 1
    for line in lines:
        digits = re.findall("\d", line)
        # int_digits = [int(a) for a in digits]
        if len(digits) == 0:
            continue
        two_digits = int(digits[0] + digits[-1])
        data += two_digits
        # print(two_digits)

    print(data)

# Part 2

# Find all digits and their start position in the string
# Find all string patterns and their start position
# Sort
# Then find first and last


def sort_tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


int_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

if not part1:
    data = 0

    for line in lines:
        # \d digits
        tuple_list = []

        # Find digit matches and index
        for match in re.finditer(r"\d", line):
            # print(match.group(), "start index", match.start())
            tuple_list.append((int(match.group()), match.start()))

        for num_string in int_mapping.keys():
            for match in re.finditer(num_string, line):
                # print(int_mapping[match.group()], "start index", match.start())
                tuple_list.append((int(int_mapping[match.group()]), match.start()))

        sorted_list = [a[0] for a in sort_tuple(tuple_list)]

        if len(sorted_list) == 0:
            continue
        two_digits = int(f"{sorted_list[0]}{sorted_list[-1]}")
        data += two_digits

    print(data)
    print("end")
