input = open("input.txt").readlines()

instances = [1] * len(input)
for card_number, line in enumerate(input):
    line_fixed = line.strip("\n").split(": ")[1].replace("  ", " ")
    winning_numbers = line_fixed.split(" | ")[0].split(" ")
    contestant_numbers = line_fixed.split(" | ")[1].split(" ")
    
    winning_numbers_count = 0
    for contestant_number in contestant_numbers:
        if contestant_number in winning_numbers:
            winning_numbers_count += 1
    for i in range(0, winning_numbers_count):
        try:
            instances[card_number + i + 1] += 1 * instances[card_number]
        except IndexError:
            break

resultDisplay = str(sum(instances))
print("Result: " + resultDisplay)
