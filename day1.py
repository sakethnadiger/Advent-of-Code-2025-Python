# Part 1

lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())
        
        
directions = []
steps = []

for inst in lines:
    directions.append(inst[0])
    steps.append(int(inst[1:]))
    
pointer = 50

passwordCounter = 0

for pos in range(len(lines)):
    if directions[pos] == "L":
        pointer -= steps[pos]
        pointer = pointer % 100
    else:
        pointer += steps[pos]
        pointer = pointer % 100
    if pointer == 0:
        passwordCounter += 1
    #print(pointer)

print(passwordCounter)

# Part 2

pointer = 50

passwordCounter = 0

for pos in range(len(lines)):
    if directions[pos] == "L":
        for step in range(steps[pos]):
            pointer -= 1
            pointer = pointer % 100
            if pointer == 0:
                passwordCounter += 1
    else:
        for step in range(steps[pos]):
            pointer += 1
            pointer = pointer % 100
            if pointer == 0:
                passwordCounter += 1
    
print(passwordCounter)