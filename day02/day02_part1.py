import copy
import os
import re
from pathlib import Path

import parse

pathfile = "test.txt"
with open(os.getcwd() + "/" + pathfile) as fp:
    lines = fp.read().split("\n")

max_red = 12
max_blue = 14
max_green = 13

valid_games = []

for line in lines:
    id_line = line.split(":")[0]
    cubes_line = line.split(":")[1:][0]
    # print(cubes_line)
    game_id = int(parse.parse("Game {id}", id_line)["id"])

    # Cube pattern
    pattern = r"(?:\d+\s\w)"
    individual_cubes = re.findall(pattern, cubes_line)
    possible = True

    for cube in individual_cubes:
        # print(cube)
        # Red cubes
        if cube.endswith("r"):
            cube_num = int(parse.parse("{d} r", cube)["d"])
            possible = cube_num <= max_red

        # Blue cubes
        elif cube.endswith("b"):
            cube_num = int(parse.parse("{d} b", cube)["d"])
            possible = cube_num <= max_blue

        # Green cubes
        elif cube.endswith("g"):
            cube_num = int(parse.parse("{d} g", cube)["d"])
            possible = cube_num <= max_green

        else:
            print("Something wrong")

        if not possible:
            break

    # print(f"Game {game_id} is {possible}")
    if possible:
        valid_games.append(game_id)

print(valid_games)
print(sum(valid_games))
