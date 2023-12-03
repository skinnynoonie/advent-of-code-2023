input = open("input.txt").readlines()

for i in range(len(input)):
    input[i] = input[i].strip("\n")

length = len(input[0])
non_special_chars = list("1234567890.")
input_one_dimension = "".join(input)

def getNodeAt(index):
    if index >= len(input_one_dimension) or index < 0:
        return "."
    return input_one_dimension[index]

def getNeighbours(index):
    neighbours = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if x_offset == 0 and y_offset == 0:
                continue
            neighbours.append(getNodeAt(index + x_offset + y_offset * length))
    return neighbours

result = 0
consecutive_numbers = ""
valid = False
for index, node in enumerate(input_one_dimension):
    if not node.isdigit():
        if valid:
            result += int(consecutive_numbers)
            valid = False
        consecutive_numbers = ""
        continue

    consecutive_numbers += node
    neighbours = getNeighbours(index)
    for neighbour in neighbours:
        if neighbour not in non_special_chars:
            valid = True

print("Result: " + str(result))
