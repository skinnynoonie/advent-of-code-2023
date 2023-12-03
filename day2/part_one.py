input = open("input.txt").readlines()

result = 0
for line in input:
    line = line.strip("\n")
    game_id = int(line.split(": ")[0].strip("Game "))
    groups = line.split(": ")[1].split("; ")

    valid_game = False

    for group in groups:

        colors = {"red": 0, "green": 0, "blue": 0}

        cubes = group.split(", ")
        for cube in cubes:
            quantity = int(cube.split(" ")[0])
            color = cube.split(" ")[1]
            colors[color] = quantity

        valid_game = colors["red"] <= 12 and colors["green"] <= 13 and colors["blue"] <= 14
        
        if not valid_game:
            break

    if valid_game:
        result += game_id

print("Result: " + str(result))
