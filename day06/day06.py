# The dumbest and bruteforcing solution ...
# pairs = {7: 9, 15: 40, 30: 200} # Test
# pairs = {59: 543, 68: 1020, 82: 1664, 74: 1022} # Data
pairs = {59688274: 543102016641022}  # Data part 2
multiplier = 1
for time, distance in pairs.items():
    ways = 0
    for speed in range(time):
        travelled = (time - speed) * speed
        if travelled > distance:
            ways += 1
    multiplier *= ways

print(multiplier)
