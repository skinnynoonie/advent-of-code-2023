import re

input = open("input.txt").readlines()

beggining_match_regex = "^(\d{1}|one|two|three|four|five|six|seven|eight|nine)"
word_to_number = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for i in range(1, 10):
    word_to_number[str(i)] = i

def get_match_from_beggining(line):
    return re.match(pattern=beggining_match_regex, string=line)

def get_matches_ordered(line):
    matches = []
    for i in range(len(line)):
        possible_match = get_match_from_beggining(line[i:])
        if possible_match != None:
            matches.append(possible_match[0])
    return matches

def transform_list_to_numbers(list_to_transform):
    for i in range(len(list_to_transform)):
        list_to_transform[i] = word_to_number[list_to_transform[i]]

result = 0
for line in input:
    matches = get_matches_ordered(line)
    transform_list_to_numbers(matches)
    # To combine two, and only two numbers would follow this process (example):
    #   Two numbers to combine: 2 and 4 to get 24
    #   2 * 10 = 20, 20 + 4 = 24
    result += matches[0] * 10 + matches[-1]

print("Result: " + str(result))
