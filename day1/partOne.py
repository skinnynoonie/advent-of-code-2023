input = open("input.txt").readlines()

result = 0
for line in input:
    first_found_value = None
    last_found_value = None
    for char in line:
        if char.isdigit():
            if first_found_value == None:
                first_found_value = int(char)
            last_found_value = int(char)
    result = result + int(str(first_found_value) + str(last_found_value))

print("Result: " + str(result))
