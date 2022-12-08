with open(file="./input/day8") as file:
    lines = file.read().splitlines()
    
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
    
trees = [[int(tree) for tree in line] for line in lines]
visible = [[0 for tree in line] for line in lines]

for r, row in enumerate(trees):
    for c, tree in enumerate(row):
        try:
            left = max(trees[r][:c])
            right = max(trees[r][c+1:])
            top = max([trees[x][c] for x in range(0,r)])
            bottom = max([trees[x][c] for x in range(r+1,len(trees))])
        except ValueError:
            visible[r][c] = 1
        try:
            all_sides = [left, right, top, bottom]
            for side in all_sides:
                if side < tree:
                    visible[r][c] = 1
        except:
            pass

print(sum(x for y in visible for x in y))

# part 2:

scores = [[0 for tree in line] for line in lines]

for r, row in enumerate(trees):
    for c, tree in enumerate(row):
        left = list(reversed(trees[r][:c]))
        right = trees[r][c+1:]
        top = list(reversed([trees[x][c] for x in range(0,r)]))
        bottom = [trees[x][c] for x in range(r+1,len(trees))]
        all_sides = [left, right, top, bottom]
        viewing_scores = [int(len(x) > 0) for x in all_sides] #0 for empty lisrt
        for s, side in enumerate(all_sides):
            if viewing_scores[s] > 0:
                if side[0] < tree: # can see beyond
                    for i, T in enumerate(side[1:]):
                        viewing_scores[s] += 1
                        if T >= tree:
                            break
        product = 1
        for score in viewing_scores:
            product *= score
        scores[r][c] = product
        
print(max([max(s) for s in scores]))
