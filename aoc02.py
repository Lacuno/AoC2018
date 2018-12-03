from itertools import starmap
   
f = open('inputs/input02.txt', 'r')
input = [list(line) for line in f]

def problem1():
    occuranceExcatly2 = 0
    occuranceExcatly3 = 0
    for line in input:
        lookup = {}
        for char in line:
            if char in lookup:
                lookup[char]+=1
            else:
                lookup[char]=1
        for char in lookup:
            if lookup[char] == 2:
                occuranceExcatly2+=1
                break
        for char in lookup:
            if lookup[char] == 3:
                occuranceExcatly3+=1
                break
    return occuranceExcatly2 * occuranceExcatly3

def problem2():
    for idx, line1 in enumerate(input):
        for line2 in input[idx+1:]:
            errors = 0
            compareList = list(zip(line1, line2))
            for elemOfList1, elemOfList2 in compareList:
                if not elemOfList1 == elemOfList2:
                    errors+=1
            if errors == 1:
                removeNonMatchingChars = lambda elem1, elem2: elem1 if elem1==elem2 else ""
                return ''.join(starmap(removeNonMatchingChars, compareList))

print(problem1())
print(problem2())