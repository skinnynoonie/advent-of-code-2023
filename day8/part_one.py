input = [i.strip("\n") for i in open("input.txt").readlines()]

steps_allowed = input[0]

nodes = {}
for line in input[2:]:
    nodes[line.split(" = ")[0]] = line.split(" = (")[1].strip(")").split(", ")

steps_count = 0
current_node = "AAA"
while True:

    for step in steps_allowed:

        index = 0
        if step == "R":
            index = 1
        current_node = nodes[current_node][index]
        steps_count += 1

        if current_node == "ZZZ":
            print(f"Result: {steps_count}")
            exit()
