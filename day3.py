lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())


# Part 1
total = 0
for bank in lines:
    largest = 0
    for i in range(len(bank)):
        if int(bank[i]) > int(str(largest)[0]):
            rem = [int(c) for c in bank[i + 1:]]
            rem.sort(reverse=True)
            rem = [str(c) for c in rem]
            if rem:
                if int(bank[i] + rem[0]) > largest:
                    largest = int(bank[i] + rem[0])
                
            
    total += largest
    
# print(total)


# Part 2

def findLargest(string, final, dist):
    if len(final) == 12:
        return final
    
    big = max([int(c) for c in string[:len(string) - dist + 1]])
    bigPos = string.find(str(big))
    return findLargest(string[bigPos + 1:], final + str(big), dist - 1)


# Find largest first digit which is not less than 12 digits away from end - prioritise first occurence
# Find largest second digit which is not less than 11 digits away from end - prioritise first occurence
# ... 
# Find largest 12th digit which is before the last digit of the whole string

total = 0

for bank in lines:
    total += int(findLargest(bank, "", 12))
    
print(total)