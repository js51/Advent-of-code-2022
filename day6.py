with open(file="./input/day6") as file:
    lines = file.read().splitlines()
 
line = lines[0]
 
for i in range(0, len(line), 1):
    part = line[i:i+14]
    if len(part) >= 14:
        distinct = len(set(part))
        print(part)
        if distinct == 14:
            print(i+14)
            break