import re

input = open("input.txt").readlines()

number_ranges = []
starting_ranges = input[0].split(": ")[1].split(" ")
for i in range(0, len(starting_ranges), 2):
    start = int(starting_ranges[i])
    end = start + int(starting_ranges[i + 1]) - 1
    number_ranges.append([start, end])

filter_pattern = re.compile("\d+ \d+ \d+\n")
maps = []
currentMap = []
for line in input:
    if "map:" in line and len(currentMap) > 0:
        maps.append(currentMap)
        currentMap = []
        continue
    if filter_pattern.match(line) != None:
        filter_split = line.split(" ")
        destination = int(filter_split[0])
        start = int(filter_split[1])
        end = start + int(filter_split[2]) - 1
        currentMap.append([destination, start, end])
maps.append(currentMap)

for map in maps:

    for number_range in number_ranges.copy():
        
        number_ranges.remove(number_range)
        unfiltered_number_ranges = [number_range]
        while len(unfiltered_number_ranges) > 0:
            unfiltered_number_range = unfiltered_number_ranges[0]
            range_min = unfiltered_number_range[0]
            range_max = unfiltered_number_range[1]

            number_out_of_bounds = False
            for filter in map:
                number_out_of_bounds = False
                filter_destination = filter[0]
                filter_min = filter[1]
                filter_max = filter[2]

                if range_min >= filter_min and range_max <= filter_max:
                    unfiltered_number_ranges.remove(unfiltered_number_range)
                    number_ranges.append([filter_destination + range_min - filter_min, filter_destination + range_max - filter_min])
                    break

                if range_min > filter_max or range_max < filter_min:
                    number_out_of_bounds = True
                    continue

                if range_min < filter_min and range_max > filter_max:
                    unfiltered_number_ranges.remove(unfiltered_number_range)
                    unfiltered_number_ranges.append([range_min, filter_min - 1])
                    number_ranges.append([filter_destination, filter_destination + filter_max - filter_min])
                    unfiltered_number_ranges.append([filter_max + 1, range_max])
                    break

                if range_min < filter_min:
                    unfiltered_number_ranges.remove(unfiltered_number_range)
                    unfiltered_number_ranges.append([range_min, filter_min - 1])
                    number_ranges.append([filter_destination, filter_destination + range_max - filter_min])
                    break

                if range_max > filter_max:
                    unfiltered_number_ranges.remove(unfiltered_number_range)
                    number_ranges.append([filter_destination + range_min - filter_min, filter_destination + filter_max - filter_min])
                    unfiltered_number_ranges.append([filter_max + 1, range_max])
                    break
                
            if number_out_of_bounds:
                unfiltered_number_ranges.remove(unfiltered_number_range)
                number_ranges.append(unfiltered_number_range)

result = number_ranges[0][0]
for number_range in number_ranges:
    if number_range[0] < result:
        result = number_range[0]

print(f"Result: {result}")
