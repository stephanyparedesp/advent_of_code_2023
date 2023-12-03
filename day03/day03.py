import re

fn = "data.txt"
lines = open(fn).read().split("\n")

pattern_numbers = r"(?:\d+)"  # greedy numbers
pattern_special = r"[^.\d]"  # except periods and digits


def find_patterns(pattern, lines):
    line_dict = {}
    for i, line in enumerate(lines):
        list_matches = []
        # Find digit matches and index
        for match in re.finditer(pattern, line):
            number = match.group()
            idx_start = match.start()
            idx_end = match.end()
            list_matches.append((number, idx_start, idx_end))
        line_dict.update({i: list_matches})

    return line_dict


# Get my numbers and special characters
number_list = find_patterns(pattern_numbers, lines)
pattern_list = find_patterns(pattern_special, lines)

part_numbers = []
for line_number, items in number_list.items():
    # For every number in that line, check if part
    for item in items:
        is_part_number = False
        number = int(item[0])
        pos_start = item[1]  # start of number true index
        pos_end = item[2]  # end of number true index

        # Adjust for when line is last and first
        if line_number != 0:
            line_above = pattern_list[line_number - 1]
        else:
            line_above = []
        line_same = pattern_list[line_number]
        if line_number != list(number_list.keys())[-1]:
            line_below = pattern_list[line_number + 1]
        else:
            line_below = []
        for l in [line_above, line_below, line_same]:
            # if line not empty and not yet classified as part
            if len(l) > 0 and not is_part_number:
                for tuple_char in l:
                    pos_char = tuple_char[1]  # position of special character
                    if pos_char in range(pos_start - 1, pos_end + 1):
                        is_part_number = True
        if is_part_number:
            part_numbers.append(number)

print(sum(part_numbers))
# %% Part 2
lines = open(fn).read().split("\n")
gear_pattern = r"[*]"
gears = find_patterns(gear_pattern, lines)
gear_values = []

for line_number, items in gears.items():
    if len(items) > 0:
        for item in items:
            gear_nums = []
            pos_char = item[1]
            # Adjust for when line is last and first
            if line_number != 0:
                # Special character lines in nearness
                line_above = number_list[line_number - 1]
            else:
                line_above = []

            line_same = number_list[line_number]

            if line_number != len(lines) + 1:
                line_below = number_list[line_number + 1]
            else:
                line_below = []

            for l in [line_above, line_below, line_same]:
                if len(l) > 0:
                    for tuple_number in l:
                        pos_start = tuple_number[1]
                        pos_end = tuple_number[2]
                        number = int(tuple_number[0])

                        if pos_char in range(pos_start - 1, pos_end + 1):
                            gear_nums.append(number)
            if len(gear_nums) == 2:
                gear_values.append(gear_nums[0] * gear_nums[1])

print(sum(gear_values))
