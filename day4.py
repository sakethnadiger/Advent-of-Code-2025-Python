lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())

# Part 1

total = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == "@":
            count = 0
            
            # Find neighbouring addition in format (row, col)
            if row == 0 and col == 0:
                n = [(0, 1), (1, 0), (1, 1)] # checked
            elif row == 0 and col == len(lines[row]) - 1:
                n = [(0, -1), (1, 0), (1, -1)] # checked
            elif row == len(lines) - 1 and col == 0:
                n = [(0, 1), (-1, 0), (-1, 1)] # checked
            elif row == len(lines) - 1 and col == len(lines[row]) - 1:
                n = [(0, -1), (-1, 0), (-1, -1)] # checked - program worked from here
            elif row == 0:
                n = [(0, 1), (1, 0), (1, 1), (0, -1), (1, -1)]
            elif row == len(lines) - 1:
                n = [(0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1)]
            elif col == 0:
                n = [(1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)]
            elif col == len(lines[row]) - 1:
                n = [(1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1)]
            else:
                n = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
            
            for displacement in n:
                if lines[row + displacement[0]][col + displacement[1]] == "@":
                    count += 1
            
            if count < 4:
                total += 1

print(total)


# Part 2

total = 0

remove = True

while remove:
    iteration_count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "@":
                count = 0
                
                # Find neighbouring addition in format (row, col)
                if row == 0 and col == 0:
                    n = [(0, 1), (1, 0), (1, 1)] # checked
                elif row == 0 and col == len(lines[row]) - 1:
                    n = [(0, -1), (1, 0), (1, -1)] # checked
                elif row == len(lines) - 1 and col == 0:
                    n = [(0, 1), (-1, 0), (-1, 1)] # checked
                elif row == len(lines) - 1 and col == len(lines[row]) - 1:
                    n = [(0, -1), (-1, 0), (-1, -1)] # checked
                elif row == 0:
                    n = [(0, 1), (1, 0), (1, 1), (0, -1), (1, -1)] # checked
                elif row == len(lines) - 1:
                    n = [(0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1)] # checked
                elif col == 0:
                    n = [(1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)] # checked
                elif col == len(lines[row]) - 1:
                    n = [(1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1)] # checked
                else:
                    n = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)] # checked
                
                for displacement in n:
                    if lines[row + displacement[0]][col + displacement[1]] == "@":
                        count += 1
                        
                
                if count < 4:
                    total += 1
                    iteration_count += 1
                    # Replace with "x" to signify that it has to be removed
                    temp = list(lines[row])
                    temp[col] = "x"        
                    lines[row] = "".join(temp)
                    
                    
                
    if iteration_count == 0:
        remove = False             
    # remove the "x"s which have been removed for another pass
    for i in lines:
        i.replace("x", ".")
    
 
print(total)
