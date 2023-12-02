import copy
import os
import re
from pathlib import Path

import parse

pathfile = "data.txt"
with open(os.getcwd() + "/" + pathfile) as fp:
    lines = fp.read().split("\n")

max_red = 12
max_blue = 14
max_green = 13

cube_power = []

for line in lines:
    id_line = line.split(":")[0]
    cubes_line = line.split(":")[1:][0]
    # print(cubes_line)
    game_id = int(parse.parse("Game {id}", id_line)["id"])

    # Cube pattern
    pattern = r"(?:\d+\s\w)"
    individual_cubes = re.findall(pattern, cubes_line)
    possible = True

    # Make a list of the cubes
    red_cubes = []
    green_cubes = []
    blue_cubes = []

    for cube in individual_cubes:
        # print(cube)
        # Red cubes
        if cube.endswith("r"):
            cube_num = int(parse.parse("{d} r", cube)["d"])
            possible = cube_num <= max_red
            red_cubes.append(cube_num)

        # Blue cubes
        elif cube.endswith("b"):
            cube_num = int(parse.parse("{d} b", cube)["d"])
            possible = cube_num <= max_blue
            blue_cubes.append(cube_num)

        # Green cubes
        elif cube.endswith("g"):
            cube_num = int(parse.parse("{d} g", cube)["d"])
            possible = cube_num <= max_green
            green_cubes.append(cube_num)

        else:
            print("Something wrong")

    cube_power.append(max(red_cubes) * max(green_cubes) * max(blue_cubes))
    # print(cube_power)

# print(valid_games)
print(sum(cube_power))
