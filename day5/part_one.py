import re

input = open("input.txt").readlines()
seed_values = input.pop(0).split("seeds: ")[1].split(" ")

maps = []
current_map = []
for line in input:
    if re.match("\d+ \d+ \d+", line) != None:
        current_map.append(line.split(" "))
    if "map:" in line:
        maps.append(current_map)
        current_map = []
maps.append(current_map)
maps.pop(0)

for seed_index, seed in enumerate(seed_values):
    seed = int(seed.strip("\n"))

    for map in maps:
        for number_range in map:
            destination_start = int(number_range[0])
            source_start = int(number_range[1])
            range_length = int(number_range[2].strip("\n"))

            if seed in range(source_start, source_start + range_length):
                seed = destination_start + seed - source_start
                break

    seed_values[seed_index] = seed

displayResult = str(min(seed_values))
print("Result: " + displayResult)
