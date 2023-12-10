input = [i.strip("\n") for i in open("input.txt").readlines()]

def calc_derivative_set(set):
    derivative = []
    for num in range(1, len(set)):
        derivative.append(set[num] - set[num - 1])
    return derivative

result = 0
for line in input:
    derivatives = []
    derivatives.append([int(i) for i in line.split(" ")])
    while True:
        if len(derivatives[-1]) == 1:
            break
        derivatives.append(calc_derivative_set(derivatives[-1]))
    derivatives.reverse()

    recent_integral = 0
    for i in range(len(derivatives) - 1):
        recent_integral += derivatives[i + 1][-1]
    result += recent_integral

print(f"Result: {result}")
