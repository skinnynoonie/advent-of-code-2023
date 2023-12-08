import re

input = open("input.txt").readlines()

time = int(re.sub(" {1,}", "", input[0].strip('\n')).split(":")[1])
distance = int(re.sub(" {1,}", "", input[1].strip('\n')).split(":")[1])

possible_times_held = 0
for time_held in range(time + 1):
    if (time - time_held) * time_held > distance:
        possible_times_held += 1

print(f"Result: {possible_times_held}")
