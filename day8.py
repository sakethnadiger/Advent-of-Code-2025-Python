from itertools import combinations
import collections

lines = []

with open("input.txt") as f:
    for line in f:
        lines.append([int(i) for i in line.strip().split(",")])



combs = list(combinations(lines, 2))
unordereddistances = dict()

for p in combs:
    d = (p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2 + (p[0][2] - p[1][2])**2 
    unordereddistances[d] = [[lines.index(p[0])], [lines.index(p[1])]]
    
pairs = collections.OrderedDict(sorted(unordereddistances.items()))

distances = list(pairs.keys())



def merge(L, l1, l2):
    if not any(isinstance(el, list) for el in l1) and not any(isinstance(el, list) for el in l2):
        sum = [[l1] + [l2]]
    elif any(isinstance(el, list) for el in l1) and not any(isinstance(el, list) for el in l2):
        sum = [l1 + [l2]]
    elif any(isinstance(el, list) for el in l2) and not any(isinstance(el, list) for el in l1):
        sum = [l2 + [l1]]
    elif any(isinstance(el, list) for el in l2) and any(isinstance(el, list) for el in l1):
        sum = [l1 + l2]
    returnL = []
    for l in range(len(L)):
        if L[l] == l1 or L[l] == l2:
            continue
        returnL.append(L[l])
            
    return returnL + sum



circuits = [[i] for i in range(len(lines))]

part2ans = 1


#Iterations is either 10, 1000, or len(distances) depending on whether we are looking at example, input or part 2
iterations = len(distances)

for x in range(iterations):
    pair = pairs[distances[x]]
    #print(pair)
    # If both boxes are on their own
    if pair[0] in circuits and pair[1] in circuits:
        #print("on their own", pair)
        #print(pair[0], pair[1], [pair[0]] + [pair[1]])
        circuits = merge(circuits, pair[0], pair[1])
    # If one box is already in a circuit
    elif pair[0] in circuits and pair[1] not in circuits:
        for i in circuits:
            if pair[1] in i:
                #print(i, pair[0])
                circuits = merge(circuits, i, pair[0])
        #print("adding first to a circuit", pair)
    elif pair[1] in circuits and pair[0] not in circuits:
        for i in circuits:
            if pair[0] in i:
                #print(i, pair[0], i + [pair[0]])
                circuits = merge(circuits, i, pair[1])
        #print("adding second to a circuit", pair)
    # If both boxes are in a circuit
    elif pair[0] not in circuits and pair[1] not in circuits:
        # If both boxes are in the same circuit
        count = 0
        for i in circuits:
            #print(pair[0], pair[1], i, pair[0] in i, pair[1] in i)
            if pair[0] in i and pair[1] in i:
                #print("done nothing", pair)
                count += 1
        if count == 0:
            #print("merged two circuits", pair)
            for k in circuits:
                if len(k) == 1:
                    continue
                if pair[0] in k:
                    first = k
            for m in circuits:
                if len(k) == 1:
                    continue
                if pair[1] in m:
                    second = m
            
            
            circuits = merge(circuits, first, second)
    
    if len(circuits) == 1:
        print("this is the one", lines[pair[0][0]], lines[pair[1][0]])
        part2ans *= lines[pair[0][0]][0] * lines[pair[1][0]][0]
        break
            
answerList = sorted(circuits, key=len, reverse=True)
# print(answerList)
            
# ans = len(answerList[0]) * len(answerList[1]) * len(answerList[2])

# print(ans)

print(part2ans)
        
