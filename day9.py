with open(file="./input/day9") as file:
    lines = file.read().splitlines()

visited = [[0 for _ in range(2001)] for _ in range(2001)]
visited[1001][1001] = 1
headpos = [1001, 1001]
tailpos = [1001, 1001]

for line in lines:
    direction, steps = line.split(' ')
    for step in range(int(steps)):
        # Move head
        d = 0
        if direction in {'U', 'L'}:
            d = -1
        else:
            d = 1
        
        if direction in {'U', 'D'}:
            if tailpos[0] == headpos[0]: # Same row
                pass
            elif tailpos[0] == headpos[0] + d*1: # Tail is where head is going
                pass
            elif tailpos[1] == headpos[1]: # same column 
                tailpos = [tailpos[0] + d*1, tailpos[1]] # just move up or down with the head
            else: # diagonal
                tailpos = [tailpos[0] + d*1, headpos[1]] # move to same column and move up or down with the head
            headpos = [headpos[0] + d*1, headpos[1]]
                
        if direction in {'L', 'R'}:
            if tailpos[1] == headpos[1]: # Same column
                pass
            elif tailpos[1] == headpos[1] + d*1: # Tail is where head is going
                pass
            elif tailpos[0] == headpos[0]: # same row 
                tailpos = [tailpos[0], tailpos[1] + d*1] # just move up or down with the head
            else: # diagonal
                tailpos = [headpos[0], tailpos[1] + d*1] # move to same column and move up or down with the head
            headpos = [headpos[0], headpos[1] + d*1]
        
        visited[tailpos[0]][tailpos[1]] = 1
        
print(sum(sum(y for y in x) for x in visited))


visited = [[0 for _ in range(2001)] for _ in range(2001)]
visited[1001][1001] = 1
parts = [[1001, 1001] for _ in range(10)]

for line in lines:
    direction, steps = line.split(' ')
    for step in range(int(steps)):
        # Move head
        d = 0
        if direction in {'U', 'L'}:
            d = -1
        else:
            d = 1
            
            
        newparts = [[1001, 1001] for _ in range(10)]
        
        if direction in {'U', 'D'}:
            newparts[0] = [parts[0][0], parts[0][1] + d*1]
        if direction in {'L', 'R'}:
            newparts[0] = [parts[0][0] + d*1, parts[0][1]]
        
        for p in range(1, len(parts)):
            if direction in {'U', 'D'}:
                if parts[p][0] == parts[p-1][0]: # Same row
                    pass
                elif parts[p][0] == parts[p-1][0] + d*1: # Tail is where head is going
                    pass
                elif parts[p][1] == parts[p-1][1]: # same column 
                    newparts[p] = [parts[p][0] + d*1, parts[p][1]] # just move up or down with the head
                else: # diagonal
                    newparts[p] = [parts[p][0] + d*1, parts[p-1][1]] # move to same column and move up or down with the head
                
            if direction in {'L', 'R'}:
                if parts[p][1] == parts[p-1][1]: # Same column
                    pass
                elif parts[p][1] == parts[p-1][1] + d*1: # Tail is where head is going
                    pass
                elif parts[p][0] == parts[p-1][0]: # same row 
                    newparts[p] = [parts[p][0], parts[p][1] + d*1] # just move up or down with the head
                else: # diagonal
                    newparts[p] = [parts[p-1][0], parts[p][1] + d*1] # move to same column and move up or down with the head
                
            if p == len(parts) - 1: # The tail
                visited[newparts[p][0]][newparts[p][1]] = 1
        
        parts = newparts
        
print(sum(sum(y for y in x) for x in visited))
