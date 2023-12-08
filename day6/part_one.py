import re

input = open("input.txt").readlines()

times = [int(i) for i in re.sub(" {1,}", " ", input[0].strip('\n')).split(": ")[1].split(" ")]
distances = [int(i) for i in re.sub(" {1,}", " ", input[1].strip('\n')).split(": ")[1].split(" ")]

result = 1
for race_num in range(len(times)):
    possible_times_held = 0
    for time_held in range(times[race_num] + 1):
        if (times[race_num] - time_held) * time_held > distances[race_num]:
            possible_times_held += 1
    result *= possible_times_held

print(f"Result: {result}")
