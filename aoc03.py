import re

f = open('inputs/input03.txt', 'r')
parseFunc = lambda line: [int(parsedElem) for parsedElem in list(re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).group(1, 2, 3, 4, 5))]
input = [parseFunc(line) for line in f]

fieldSize = 1000
fabricField = [[[] for item in range(0, fieldSize)] for item in range(0, fieldSize)]
def prepareField():
    for (id, x, y, width, height) in input:
        for i in range(x, x+width):
            for j in range(y, y+ height):
                fabricField[i][j].append(id)

def problem1():
    return sum(map(lambda line: sum(1 for x in line if len(x) > 1), fabricField))

def problem2():
    ids = set([x[0] for x in input])
    for i in range(0, fieldSize):
        for j in range(0, fieldSize):
            if len(fabricField[i][j]) > 1:
                for overlapping in fabricField[i][j]:
                    ids.discard(overlapping)
    return ids.pop()

prepareField()
print(problem1())
print(problem2())