input = open("input.txt").readlines()

result = 0
for line in input:
    line = line.strip("\n")
    game_id = int(line.split(": ")[0].strip("Game "))
    groups = line.split(": ")[1].split("; ")

    colors_most = {"red": 0, "green": 0, "blue": 0}

    for group in groups:
        cubes = group.split(", ")
        for cube in cubes:
            quantity = int(cube.split(" ")[0])
            color = cube.split(" ")[1]

            if colors_most[color] < quantity:
                colors_most[color] = quantity

    result = result + colors_most["red"] * colors_most["green"] * colors_most["blue"]

print("Result: " + str(result))
