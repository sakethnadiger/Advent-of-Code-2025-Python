lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(list(line.strip()))

beams = {lines[0].index("S")}

# Part 1
count = 0

for l in lines:
    if "^" not in l:
        continue
    
    for i in range(len(l)):
        if i in beams and l[i] == "^":
            count += 1
            beams.remove(i)
            beams.add(i + 1)
            beams.add(i - 1)
    
    print(sorted(beams))
    

print(count)

# Part 2

# Holds all the splitters and their parent splitters

beams = [(0, lines[0].index("S"))]
splitters = {}

def checkVal(list, val):
    for i in list:
        if i[1] == val:
            return True
    return False

scores = {}

for x, l in enumerate(lines):
    if "^" not in l:
        continue
    
    for i in range(len(l)):
        if l[i] == "^":
            if x == 2:
                scores[(x, i)] = 1
            splitters[(x, i)] = []
            counter = 0
            flag = True
            while flag == True:
                try:
                    
                    if i == beams[counter][1]:
                        for s in splitters.keys():
                            if s[0] >= beams[counter][0] and abs(s[1] - i) == 1:
                                splitters[(x, i)].append(s)
                        beams.remove(beams[counter])
                        if not checkVal(beams, i + 1):
                            beams.append((x, i + 1))
                            
                        if not checkVal(beams, i - 1):
                            beams.append((x, i - 1))
                        flag = False
                    counter += 1
                except:
                    flag = False



for k in splitters.keys():
    if k not in scores.keys():        
        total = 0
        for n in splitters[k]:
            total += scores[n]
        scores[k] = total
    


ends = []

for b in beams:
    for s in splitters.keys():
        if s[0] >= b[0] and abs(s[1] - b[1]) <= 1:
            ends.append(s)
            
timelines = 0

for e in ends:
    timelines += scores[e]
    
print(timelines)