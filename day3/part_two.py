input = open("input.txt").readlines()

for i in range(len(input)):
    input[i] = input[i].strip("\n")

length = len(input[0])
non_special_chars = list("1234567890.")
input_one_dimension = "".join(input)

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index

def getNodeAt(index):
    if index >= len(input_one_dimension) or index < 0:
        return Node(".", index)
    return Node(input_one_dimension[index], index)

def getNeighbours(index):
    neighbours = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if x_offset == 0 and y_offset == 0:
                continue
            offset_index = index + x_offset + y_offset * length
            neighbours.append(getNodeAt(offset_index))
    return neighbours

gears = {}
gears_temp = []
consecutive_numbers = ""
valid = False
for index, node in enumerate(input_one_dimension):
    if not node.isdigit():
        if valid:
            
            for gear_index in gears_temp:
                if gear_index not in gears:
                    gears[gear_index] = []
                gears[gear_index].append(int(consecutive_numbers))

            valid = False
        gears_temp = []
        consecutive_numbers = ""
        continue

    consecutive_numbers += node
    neighbours = getNeighbours(index)
    for neighbour in neighbours:
        if neighbour.value == "*" and neighbour.index not in gears_temp:
            gears_temp.append(neighbour.index)
            valid = True

result = 0
for gear_index in gears:
    neighbour_numbers = gears[gear_index]
    if len(neighbour_numbers) != 2:
        continue
    product = 1
    for number in neighbour_numbers:
        product *= number
    result += product

print("Result: " + str(result))
