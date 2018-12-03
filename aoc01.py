def problem1():
    return sum(input)

def problem2():
    lookup = {}
    current = 0
    while True:
        for elem in input:
            if current in lookup:
                return current
            lookup[current] = True
            current += elem

f = open('inputs/input01.txt', 'r')
input = [int(line) for line in f]

print(problem1())
print(problem2())