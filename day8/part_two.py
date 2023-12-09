import math

input = [i.strip("\n") for i in open("input.txt").readlines()]

steps_allowed = input[0]

nodes = {}
for line in input[2:]:
    nodes[line.split(" = ")[0]] = line.split(" = (")[1].strip(")").split(", ")

def search(current_node):
    steps_count = 0
    while True:

        for step in steps_allowed:

            index = 0
            if step == "R":
                index = 1
            current_node = nodes[current_node][index]
            steps_count += 1

            if current_node[2] == "Z":
                return steps_count
            
results = []
for i in nodes:
    if i[2] == "A":
        results.append(search(i))

print(math.lcm(*results))
