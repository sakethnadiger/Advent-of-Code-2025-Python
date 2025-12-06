from operator import mul
from functools import reduce

lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line) # --> Was line.strip() for part 1


allLines = [l.split() for l in lines]

operations = list(zip(*allLines))

# Part 1 - only works with line.strip()

total = 0

for x in range(len(operations)):
    
    operations[x] = list(map(int, operations[x][:-1])) + [operations[x][-1]]
    
    if operations[x][-1] == "*":
        total += reduce(mul, operations[x][:-1])
    else:
        total += sum(operations[x][:-1])

print(total)

# Part 2

# Find the common space indices so we can separate operations and add placeholders

sets = []

for x, l in enumerate(lines):
    spaces = set()
    for c in range(len(l)):
        if l[c] == " ":
            spaces.add(c)
    sets.append(spaces)
    lines[x] = list(l)
    if "\n" in lines[x]:
        lines[x].pop()
    
intersectSet = set.intersection(*sets)

separations = sorted(intersectSet)

# Now we go through each line and replace a space which isn't in operation separations with a x placeholder

for x, l in enumerate(lines):
    for k in range(len(l)):
        if l[k] == " " and k not in separations:
            l[k] = "x"
        elif l[k] != " " and l[k] not in ["+", "*"]:
            l[k] = l[k]
    
    lines[x] = "".join(lines[x])

    
allLines = [l.split() for l in lines]

operations = list(zip(*allLines))

total = 0

for x in range(len(operations)):
    maxLen = len(max(operations[x]))
    newNums = []
    for i in range(maxLen):
        num = ""
        for n in operations[x][:-1]:
            if n[i] != "x": 
                num += n[i]
        newNums.append(int(num))
    if operations[x][-1][0] == "*":
        total += reduce(mul, newNums)
    else:
        total += sum(newNums)

print(total)