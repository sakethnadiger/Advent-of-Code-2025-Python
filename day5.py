ranges = []
fruits = []

with open("input.txt") as f:
    for line in f:
        if "-" in line:
           lower, upper = line.split("-")
           ranges.append([int(lower), int(upper)])
        elif line != "\n":
            fruits.append(int(line.strip())) 

# Part 1

for i, r in enumerate(ranges):
    lower, upper = r.split("-")
    ranges[i] = range(int(lower), int(upper) + 1)

total = 0

for f in fruits:
    counter = 0
    for k in ranges:
        if f in k:
            counter += 1
    if counter > 0:
        total += 1

print(total)

# Part 2

# Union of (10, 14) and (12, 18) = (10, 18)
# Union of (10, 14) and (12, 18) and (16, 20) = union of (10, 18) and (16, 20) = (10, 20)
# Union of (a, b) and (c, d) exists if c <= b <= d or a <= d <= b and is equal to (min(a, c), max(b, d))

ranges.sort()

def union(r1, r2):
    a = r1[0]
    b = r1[1]
    c = r2[0]
    d = r2[1]
    
    if c <= b <= d or a <= d <= b:
        return [min(a, c), max(b, d)]
    
    return False

# print(union(union([10, 14], [12, 18]), [16, 20]))


pos = 0

while pos < len(ranges):
    flag = True
    while flag == True:
        if pos != len(ranges) - 1:
            unionList = union(ranges[pos], ranges[pos + 1])
            if unionList == False:
                flag = False
            else:
                ranges[pos] = unionList
                del ranges[pos + 1]
                
        else:
            flag = False
    pos += 1


total = 0
for k in ranges:
    total += k[1] - k[0] + 1
    
print(total)
