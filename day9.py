x = []
y = []

lines = []

with open("test.txt") as f:
    for line in f:
        lines.append([int(i) for i in line.strip().split(",")])
        xl, yl = line.strip().split(",")
        x.append(int(xl))
        y.append(int(yl))

# Part 1
# big = 0

# for i in lines:
#     x1, y1 = i[0], i[1]
#     for j in lines:
#         if i == j:
#             continue
#         x2, y2 = j[0], j[1]
#         A = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
#         if A > big:
#             big = A
            
# print(big)        
    
# Part 2

# Find minimum red tile and maximum red tile for the whole grid

minX, maxX = min(x), max(x)
minY, maxY = min(y), max(y)

print(minX, maxX, minY, maxY)
