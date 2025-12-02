from functools import reduce

lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())
        
ranges = []

for line in lines:
    splitLine = line.split(",")
    for r in splitLine:
        if r:
            ranges.append(r)

total = []

# Part 1

# for seq in ranges:
#     start, end = seq.split("-")[0], seq.split("-")[1]
#     for num in range(int(start), int(end) + 1):
#         if len(str(num)) % 2 == 1:
#             continue
#         else:
#             stringNum = str(num)
#             halfStart, halfEnd = stringNum[:len(stringNum)//2], stringNum[len(stringNum)//2:]
#             if halfStart == halfEnd:
#                 total += num

# Part 2

# def allFactors(n):
#     return set(factor for i in range(1, int(n**0.5) + 1) if n % i == 0 for factor in (i, n//i))

# def splitString(s, n):
#     return [s[i:i + n] for i in range(0, len(s), n)]

# for seq in ranges:
#     start, end = seq.split("-")[0], seq.split("-")[1]
#     for num in range(int(start), int(end) + 1):
#         length = len(str(num))
#         factors = allFactors(length)
#         for n in factors:
#             split = splitString(str(num), len(str(num)) // n)
#             if len(set(split)) == 1 and len(split) > 1:
#                 if num not in total:
#                     total.append(num)
                


# print(sum(total))