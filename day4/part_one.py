import math

input = open("input.txt").readlines()

result = 0
for line in input:
    line_fixed = line.strip("\n").split(": ")[1].replace("  ", " ")
    winning_numbers = line_fixed.split(" | ")[0].split(" ")
    contestant_numbers = line_fixed.split(" | ")[1].split(" ")

    winning_numbers_count = 0
    for contestant_number in contestant_numbers:
        if contestant_number in winning_numbers:
            winning_numbers_count += 1

    result += math.floor(2 ** (winning_numbers_count - 1))

print("Result: " + str(result))
